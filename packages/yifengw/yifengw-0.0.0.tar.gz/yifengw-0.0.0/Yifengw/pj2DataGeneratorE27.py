__author__ = 'Haohan Wang'

#import cv2
#from PIL import Image
import torch
from torch.utils.data import Dataset
#import pandas as pd
import numpy as np
from os.path import join
from copy import copy
import math
import numpy as np
import torchio as tio
import torch
from os.path import join
import random
from dataAugmentation import MRIDataAugmentation
import scipy.ndimage
import scipy.linalg as linalg
import nibabel as nib

def sphere(shape, radius, position):
    semisizes = (radius,) * 3
    grid = [slice(-x0, dim - x0) for x0, dim in zip(position, shape)]
    position = np.ogrid[grid]
    arr = np.zeros(shape, dtype=float)
    for x_i, semisize in zip(position, semisizes):
     arr += (np.abs(x_i/semisize) ** 2)
    return arr <= 1.0


def loc_convert(loc, axis, radian):
    '''
	实现点按某个轴旋转一定度数后得到新点坐标
    :param loc:原始坐标
    :param axis: 绕旋转的轴（点）
    :param radian: 角度
    :return: 新坐标
    '''
    radian = np.deg2rad(radian)
    rot_matrix = linalg.expm(np.cross(np.eye(3), axis / linalg.norm(axis) * radian))
    new_loc = np.dot(rot_matrix, loc)
    return new_loc

def extract_slice(img, c, v, radius):
    '''
    :param V:3d 图像
    :param center-c: 中心（x,y,z）
    :param normal-v: 法向量（v1,v2,v3）
    :param radius: 半径，即边长的一半
    :return:
    slicer：得到的2d切片
    loc: 得到切片对应的原3d坐标
    '''
    # 设置初始面
    epsilon = 1e-12
    x = np.arange(-radius, radius, 1)
    y = np.arange(-radius, radius, 1)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)
    loc = np.array([X.flatten(), Y.flatten(), Z.flatten()])

    # 设置初始平面，垂直于Z轴，将向量变为单位向量
    hspInitialVector = np.array([0, 0, 1])
    h_norm = np.linalg.norm(hspInitialVector)
    h_v = hspInitialVector / h_norm
    h_v[h_v == 0] = epsilon
    v = v / np.linalg.norm(v)
    v[v == 0] = epsilon

    # 计算初始法线与最后法线的角度
    hspVecXvec = np.cross(h_v, v) / np.linalg.norm(np.cross(h_v, v))
    acosineVal = np.arccos(np.dot(h_v, v))
    hspVecXvec[np.isnan(hspVecXvec)] = epsilon
    acosineVal = epsilon if np.isnan(acosineVal) else acosineVal

    # 得到旋转后的坐标
    loc = loc_convert(loc, hspVecXvec, 180 * acosineVal / math.pi)
    sub_loc = loc + np.reshape(c, (3, 1))
    loc = np.round(sub_loc)
    loc = np.reshape(loc, (3, X.shape[0], X.shape[1]))

    # 生成初始切片，以及对应的索引值
    sliceInd = np.zeros_like(X, dtype=float)
    #sliceInd[sliceInd == 0] = np.nan
    slicer = np.copy(sliceInd)
    #print("loc",loc)
    # 将3D图像对应的像素值以及对应的坐标赋值给对应的切片
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            if loc[0, i, j] >= 0 and loc[0, i, j] < img.shape[0] and loc[1, i, j] >= 0 and loc[1, i, j] < img.shape[1] and loc[2, i, j] >= 0 and loc[2, i, j] < img.shape[2]:
            #if loc[0, i, j] < img.shape[0] and loc[1, i, j] >= 0 and loc[1, i, j] < img.shape[1] and loc[2, i, j] >= 0 and loc[2, i, j] < img.shape[2]:
                slicer[i, j] = img[
                    loc[0, i, j].astype(int), loc[1, i, j].astype(int), loc[2, i, j].astype(int)]
    #slicer[np.isnan(slicer)]=0
    #print("shape",slicer.shape)
    #print("slicer",slicer)
    return slicer, sub_loc, loc

def is_point_in_block(point, block_min, block_max):
    #for p, min_val, max_val in zip(point, block_min, block_max):
    #print("this is p",point)
    p=point
    min_val=block_min
    max_val=block_max
    if ((min_val[0]<=p[0][0]<=max_val[0] and min_val[1]<=p[0][1]<=max_val[1] and min_val[2]<=p[0][2]<=max_val[2]) and
    (min_val[0]<=p[1][0]<=max_val[0] and min_val[1]<=p[1][1]<=max_val[1] and min_val[2]<=p[1][2]<=max_val[2]) and
    (min_val[0]<=p[2][0]<=max_val[0] and min_val[1]<=p[2][1]<=max_val[1] and min_val[2]<=p[2][2]<=max_val[2]) and 
    (min_val[0]<=p[3][0]<=max_val[0] and min_val[1]<=p[3][1]<=max_val[1] and min_val[2]<=p[3][2]<=max_val[2])):
        return True
    return False

def getposition_1(check):
    final_list=[]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                block_min_coords = (i*5, j*5, k*5)
                block_max_coords = (i*5+9, j*5+9, k*5+9)
                #checkin=True
                checkin=is_point_in_block(check,block_min_coords,block_max_coords)
                if checkin==True:
                    #print("this",i,j,k)
                    final_list.append(i*9+j*3+k*1)
    #print(len(final_list))
    return final_list
                
def getposition_2(block_min_coord,check):
    #print(block_min_coords)
    final_list=[]
    origin_min_coords=block_min_coord
    for i in range(3):
        for j in range(3):
            for k in range(3):
                block_min_coords = (origin_min_coords[0]+i*2,origin_min_coords[1]+j*2,origin_min_coords[2]+k*2)
                block_max_coords = (block_min_coords[0]+5, block_min_coords[1]+5, block_min_coords[2]+5)
                #checkin=True
                checkin=is_point_in_block(check,block_min_coords,block_max_coords)
                if checkin==True:
                    final_list.append(i*9+j*3+k*1)
    return final_list

def getposition_3(block_min_coords,check_point1,check_point2,check_point3,check_point4):
    #print(block_min_coords)
    #print(check_point1)
    #print(check_point2)
    #print(check_point3)
    #print(check_point4)
    origin_min_coords=block_min_coords
    re1=re2=re3=re4=[]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                block_min_coords = (origin_min_coords[0]+i,origin_min_coords[1]+j,origin_min_coords[2]+k)
                #block_max_coords = (block_min_coords[0]+4, block_min_coords[1]+4, block_min_coords[2]+4)
                #checkin=True
                #print(block_min_coords)
                if block_min_coords[0]==int(check_point1[0]) and block_min_coords[1]==int(check_point1[1]) and block_min_coords[2]==int(check_point1[2]):
                    re1=[i,j,k]
                if block_min_coords[0]==int(check_point2[0]) and block_min_coords[1]==int(check_point2[1]) and block_min_coords[2]==int(check_point2[2]):
                    re2=[i,j,k]
                if block_min_coords[0]==int(check_point3[0]) and block_min_coords[1]==int(check_point3[1]) and block_min_coords[2]==int(check_point3[2]):
                    re3=[i,j,k]
                if block_min_coords[0]==int(check_point4[0]) and block_min_coords[1]==int(check_point4[1]) and block_min_coords[2]==int(check_point4[2]):
                    re4=[i,j,k]
    #print(re1,re2,re3,re4)
    return re1,re2,re3,re4

class MRIDataGenerator(Dataset):
    'Generates data for Keras'

    def __init__(self, img_dir,
                 split,
                 transform=None,
                 idx_fold=0,
                 num_fold=5,
                 batchSize=16,
                 dim=(20, 20, 20),
                 n_channels=1,
                 n_classes=2,
                 augmented=False,
                 augmented_fancy=False,
                 MCI_included=True,
                 MCI_included_as_soft_label=False,
                 returnSubjectID=False,
                 dropBlock = False,
                 dropBlockIterationStart = 0,
                 gradientGuidedDropBlock=False
                 ):
        # 'Initialization'
        random.seed( 3407 )
        self.img_dir = '/home/haohanw/ADdata/AlzheimerImagingData/ADNI_CAPS'
        self.split = split
        self.transform = transform
        self.idx_fold = idx_fold
        self.num_fold = num_fold
        self.batch_size = batchSize
        self.dim = dim
        self.dim2d=(4,4)
        self.dimlabel1=(27,)
        self.n_channels = n_channels
        self.n_classes = n_classes
        self.augmented = augmented
        self.augmented_fancy = augmented_fancy
        self.MCI_included = MCI_included
        self.MCI_included_as_soft_label = MCI_included_as_soft_label
        self.returnSubjectID = returnSubjectID
        self.dropBlock = dropBlock
        #d = torch.load('/home/yifengw/ADNI_CAPS/subjects/sub-ADNI136S0186/ses-M00/deeplearning_prepare_data/image_based/t1_linear/sub-ADNI136S0186_ses-M00_T1w_space-MNI152NLin2009cSym_desc-Crop_res-1x1x1_T1w.pt').cpu().numpy().astype(np.float32)
        #self.imaged = (d - np.min(d)) / (np.max(d) - np.min(d)).squeeze()
        d=self.create_MRI()
        #d=self.create_data1()
        #print(d[0,0:20,0:20,0:20])
        #print(np.min(d),np.max(d))
        self.imaged = (d - np.min(d)) / (np.max(d) - np.min(d))
        #self.imaged=(d-np.mean(d))/np.std(d)
        #self.imaged=(d-np.log10(np.min(d)))/(np.log10(np.max(d))-np.log10(np.min(d)))
        #print(self.imaged)
        #self.imaged=d
        self.dropBlock_iterationCount = dropBlockIterationStart
        self.gradientGuidedDropBlock = gradientGuidedDropBlock
        #print("yes")
        self.parse_csv_file()
        #self._get_batch_split()
        self.on_epoch_end()

        self.dataAugmentation = MRIDataAugmentation(self.dim, 0.5)

    def create_data(self):
        random.seed(3407)
        d=np.zeros((1,160,160,160), dtype = int)
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    value_list=list(range(1,20001,40))
                    random_list=np.random.randint(0,20,size=20*5*5).tolist()
                    for z in range(20):
                        for x in range(5):
                            for y in range(5):
                                #value=random.choice(value_list)
                                pos=y*1+x*5+z*25
                                #value=value_list[pos]+random_list[pos]
                                value=value_list[pos]
                                for p in range(4):
                                    for q in range(4):
                                        d[0,i*20+x*4+q:i*20+x*4+q+1,j*20+y*4+p:j*20+y*4+p+1,k*20+z:k*20+z+1]=value
                                #value_list.remove(value)
                #for k in range(4):
                #d[0,i*20:i*20+20,j*20:j*20+20,k*20:k*20+20]=i*64+j*8+k*1
                #for k in range(4,8):
                #d[0,i*20:i*20+20,j*20:j*20+20,k*20:k*20+20]=np.random.randint(i*64+j*8+k-4,i*64+j*8+k,(20,20,20))
        return d

    def create_data1(self):
        random.seed(3407)
        d=np.ones((1,160,160,160), dtype = int)
        numbers = np.arange(20, 36)
        matrix = numbers.reshape(4, 4,1)
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    value_list=list(range(20,80,3))
                    #random_list=np.random.randint(0,2,size=20).tolist()
                    #random_list1=list(range(0,17,1))
                    for z in [19]:
                        pos=z
                        value=value_list[pos]
                        if z<=0<15:
                            d[0,i*20+z:i*20+z+4,j*20+z:j*20+z+4,k*20+z:k*20+z+1]=value
                        else:
                            #d[0,i*20+0:i*20+4,j*20+0:j*20+4,k*20+z:k*20+z+1]=40
                            d[0,i*20+16:i*20+20,j*20+16:j*20+20,k*20+z:k*20+z+1]=matrix
                #for k in range(4):
                #d[0,i*20:i*20+20,j*20:j*20+20,k*20:k*20+20]=i*64+j*8+k*1
                #for k in range(4,8):
                #d[0,i*20:i*20+20,j*20:j*20+20,k*20:k*20+20]=np.random.randint(i*64+j*8+k-4,i*64+j*8+k,(20,20,20))
        return d

    def create_data2(self):
        random.seed(3407)
        d=np.ones((1,160,160,160), dtype = int)
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    value_list=list(range(1,20001,40))
                    random_list=np.random.randint(0,20,size=20*5*5).tolist()
                    for z in range(20):
                        if z%2==0:
                            for x in range(1):
                                for y in range(1):
                                    #value=random.choice(value_list)
                                    pos=y*1+x*5+z*25
                                    #value=value_list[pos]+random_list[pos]
                                    value=value_list[pos]
                                    for p in range(4):
                                        for q in range(4):
                                            d[0,i*20+x*4+q:i*20+x*4+q+1,j*20+y*4+p:j*20+y*4+p+1,k*20+z:k*20+z+1]=value
                                #value_list.remove(value)
                #for k in range(4):
                #d[0,i*20:i*20+20,j*20:j*20+20,k*20:k*20+20]=i*64+j*8+k*1
                #for k in range(4,8):
                #d[0,i*20:i*20+20,j*20:j*20+20,k*20:k*20+20]=np.random.randint(i*64+j*8+k-4,i*64+j*8+k,(20,20,20))
        return d

    def create_MRI(self):
        d=np.zeros((1,160,160,160), dtype = int)
        path=[]
        csv_path = join(self.img_dir, f'split.pretrained.0.csv')
        text = [line.strip() for line in open(csv_path)]
        for line in text[1:]:
            items = line.split(',')
            if items[-2] == 'CN':
                image_path = join(self.img_dir, 'subjects', items[0], items[1], 'deeplearning_prepare_data',
                                  'image_based',
                                  't1_linear',
                                  items[0] + '_' + items[
                                      1] + '_T1w_space-MNI152NLin2009cSym_desc-Crop_res-1x1x1_T1w.pt')
                path.append(image_path)
                if len(path)==8*8*8:
                    break
        for i in range(len(path)):
            single_path=path[i]
            #image_MRI=torch.load('/home/yifengw/ADNI_CAPS/subjects/sub-ADNI136S0186/ses-M00/deeplearning_prepare_data/image_based/t1_linear/sub-ADNI136S0186_ses-M00_T1w_space-MNI152NLin2009cSym_desc-Crop_res-1x1x1_T1w.pt')
            image_MRI=torch.load(single_path)
            image_MRI=image_MRI[0]
            initial_shape=image_MRI.shape
            image_MRI=scipy.ndimage.zoom(image_MRI, [20/initial_shape[0],20/initial_shape[1],20/initial_shape[2]], order=3)
            z=i//64
            y=(i-z*64)//8
            x=i-z*64-8*y
            #print(image_MRI.shape)
            d[0,x*20:(x+1)*20,y*20:(y+1)*20,z*20:(z+1)*20]=image_MRI
        return d

    def create_MRI1(self):
        d=np.zeros((1,20,20,20), dtype = int)
        path=[]
        csv_path = join(self.img_dir, f'split.pretrained.0.csv')
        text = [line.strip() for line in open(csv_path)]
        for line in text[1:]:
            items = line.split(',')
            if items[-2] == 'CN':
                image_path = join(self.img_dir, 'subjects', items[0], items[1], 'deeplearning_prepare_data',
                                  'image_based',
                                  't1_linear',
                                  items[0] + '_' + items[
                                      1] + '_T1w_space-MNI152NLin2009cSym_desc-Crop_res-1x1x1_T1w.pt')
                path.append(image_path)
                if len(path)==1*1*1:
                    break
        for i in range(len(path)):
            single_path=path[i]
            image_MRI=torch.load(single_path)
            z=i//1
            y=(i-z*1)//8
            x=i-z*1-1*y
            #print(image_MRI.shape)
            '''file = open("./test_data.txt", 'x')
            for write_data in range(20):
                file.write(str(image_MRI[0,80:100,80:100,158+write_data:159+write_data]))
                file.write("\n")'''
            d[0,x*20:(x+1)*20,y*20:(y+1)*20,z*20:(z+1)*20]=image_MRI[0,80:100,80:100,158:178]
        return d

    def __len__(self):
        self.on_epoch_end()
        return math.ceil(self.totalLength/self.batch_size)

    def combine(self,image,batchSize):
        imaging=image.squeeze(dim=4)
        '''transform = tio.CropOrPad((20, 20, 20))
        imaging=transform(imaging)
        image_shape=imaging.shape'''
        #imaging=imaging[:,0:20,0:20,0:20]
        #image_shape=img.shape
        #image=imaging.unsqueeze(dim=4)
        return imaging
    
    def __getitem__(self, idx):
        if self.split == 'train':
            if not self.returnSubjectID:  # training tricks such as balance the two labels and augmentation will not happen once subject ID is required
                images_3d, images_2d_list = self._load_batch_image_train(idx)
                images = images_3d.astype(np.float32)
                images=torch.from_numpy(images)
                #print(images)
                #print(images.shape)
                images=self.combine(images,self.batch_size)
                #print(images.shape)
                #c = [random.randint(2,17),random.randint(2,17),random.randint(2,17)]
                image_2d=np.zeros((self.batch_size, *self.dim2d))
                labels1_loss1=np.zeros((self.batch_size,*self.dimlabel1),dtype=np.int64)
                #labels1_loss2=np.zeros((self.batch_size,*self.dimlabel1),dtype=np.int64)
                #labels1_loss3=np.zeros((self.batch_size,*self.dimlabel1),dtype=np.int64)
                labels2_loss=[]
                labels2=[]
                labels1=[]
                for i in range(self.batch_size):
                    image_single=images[i:i+1,:,:,:]
                    #print("3d",image_single)
                    c=images_2d_list[i]
                    n=[random.randint(0, 9),random.randint(0, 9),random.randint(0, 9)]
                    #n=[0,0,1]
                    r=2
                    arr=torch.squeeze(image_single)
                    slicer, sub_loc, slice_check = extract_slice(arr, c, n, r)
                    #print(slice_check)
                    check_point1=(slice_check[0][0][0],slice_check[1][0][0],slice_check[2][0][0])
                    check_point2=(slice_check[0][2*r-1][0],slice_check[1][2*r-1][0],slice_check[2][2*r-1][0])
                    check_point3=(slice_check[0][0][2*r-1],slice_check[1][0][2*r-1],slice_check[2][0][2*r-1])
                    check_point4=(slice_check[0][2*r-1][2*r-1],slice_check[1][2*r-1][2*r-1],slice_check[2][2*r-1][2*r-1])
                    check=[check_point1,check_point2,check_point3,check_point4]
                    #print(check)
                    label_list=getposition_1(check)
                    #print(i_30,j_30,k_30,block_min_coords)
                    #i_20,j_20,k_20,block_min_coords1=getposition_2(block_min_coords,check)
                    #pos1,pos2,pos3,pos4=getposition_3(block_min_coords1,check_point1,check_point2,check_point3,check_point4)
                    image_2d[i,:,:]=slicer
                    #labels1_single=[i_30,j_30,k_30]
                    #print(labels1_single)
                    #labels1_sin=labels1_single[0]*9+labels1_single[1]*3+labels1_single[2]*1
                    #print(image_2d.shape)
                    #labels2=[i_20,j_20,k_20]
                    #labels3=pos1+pos2+pos3+pos4
                    #print(labels1)
                    #print(labels2)
                    #print(labels3)
                    final_multi_label1=np.zeros(27)
                    #final_multi_label2=np.zeros(3)
                    #final_multi_label3=np.zeros(3)
                    #print("this",final_multi_label,label_list)
                    for label_number in label_list:
                        #print(label_number)
                        final_multi_label1[label_number]=1
                    #print("final",final_multi_label)
                    labels1_loss1[i,:] = final_multi_label1
                    labels1.append(label_list)
                    labels2_loss_mid=[]
                    labels2_mid=[]
                    for i_2 in range(len(label_list)):
                        a=label_list[i_2]//9
                        b=(label_list[i_2]-a*9)//3
                        c=label_list[i_2]-a*9-b*3
                        min_cord_2=[a*5,b*5,c*5]
                        label_list_2=getposition_2(min_cord_2,check)
                        final_multi_label_2=np.zeros(3*3*3)
                        for label_number in label_list_2:
                            final_multi_label_2[label_number]=1
                        labels2_loss_mid.append(final_multi_label_2)
                        labels2_mid.append(label_list_2)
                    labels2_loss.append(labels2_loss_mid)
                    labels2.append(labels2_mid)
                labels1_loss1=torch.from_numpy(labels1_loss1)
                #labels1_loss2=torch.from_numpy(labels1_loss2)
                #labels1_loss3=torch.from_numpy(labels1_loss3)
                #labels2 = np.array(labels2)
                #labels2=torch.from_numpy(labels2)
                #labels3 = np.array(labels3)
                #labels3=torch.from_numpy(labels3)
                #labels = labels.astype(np.float32)
                #labels=torch.from_numpy(labels)
                #labels=torch.topk(labels, 1)[1].squeeze(1)
                #print("final",labels1)
                #print("loss",labels1_loss)
                #print(labels2)
                return images_3d, image_2d, labels1,labels1_loss1,labels2,labels2_loss
        else:
            if self.split=='test':
                images_3d, images_2d_list = self._load_batch_image_test(idx)
            else:
                images_3d, images_2d_list = self._load_batch_image_val(idx)
            images = images_3d.astype(np.float32)
            images=torch.from_numpy(images)
            #print(images)
            #print(images.shape)
            images=self.combine(images,self.batch_size)
            #print(images.shape)
            #c = [random.randint(2,17),random.randint(2,17),random.randint(2,17)]
            image_2d=np.zeros((self.batch_size, *self.dim2d))
            labels1_loss1=np.zeros((self.batch_size,*self.dimlabel1),dtype=np.int64)
            #labels1_loss2=np.zeros((self.batch_size,*self.dimlabel1),dtype=np.int64)
            #labels1_loss3=np.zeros((self.batch_size,*self.dimlabel1),dtype=np.int64)
            labels2_loss=[]
            labels2=[]
            labels1=[]
            for i in range(self.batch_size):
                image_single=images[i:i+1,:,:,:]
                #print("3d",image_single)
                c=images_2d_list[i]
                n=[random.randint(0, 9),random.randint(0, 9),random.randint(0, 9)]
                #n=[0,0,1]
                r=2
                arr=torch.squeeze(image_single)
                slicer, sub_loc, slice_check = extract_slice(arr, c, n, r)
                #print(slice_check)
                check_point1=(slice_check[0][0][0],slice_check[1][0][0],slice_check[2][0][0])
                check_point2=(slice_check[0][2*r-1][0],slice_check[1][2*r-1][0],slice_check[2][2*r-1][0])
                check_point3=(slice_check[0][0][2*r-1],slice_check[1][0][2*r-1],slice_check[2][0][2*r-1])
                check_point4=(slice_check[0][2*r-1][2*r-1],slice_check[1][2*r-1][2*r-1],slice_check[2][2*r-1][2*r-1])
                check=[check_point1,check_point2,check_point3,check_point4]
                #print(check)
                label_list=getposition_1(check)
                #print(i_30,j_30,k_30,block_min_coords)
                #i_20,j_20,k_20,block_min_coords1=getposition_2(block_min_coords,check)
                #pos1,pos2,pos3,pos4=getposition_3(block_min_coords1,check_point1,check_point2,check_point3,check_point4)
                image_2d[i,:,:]=slicer
                #labels1_single=[i_30,j_30,k_30]
                #print(labels1_single)
                #labels1_sin=labels1_single[0]*9+labels1_single[1]*3+labels1_single[2]*1
                #print(image_2d.shape)
                #labels2=[i_20,j_20,k_20]
                #labels3=pos1+pos2+pos3+pos4
                #print(labels1)
                #print(labels2)
                #print(labels3)
                final_multi_label1=np.zeros(27)
                #final_multi_label2=np.zeros(3)
                #final_multi_label3=np.zeros(3)
                #print("this",final_multi_label,label_list)
                for label_number in label_list:
                    #print(label_number)
                    final_multi_label1[label_number]=1
                #print("final",final_multi_label)
                labels1_loss1[i,:] = final_multi_label1
                labels1.append(label_list)
                labels2_loss_mid=[]
                labels2_mid=[]
                for i_2 in range(len(label_list)):
                    a=label_list[i_2]//9
                    b=(label_list[i_2]-a*9)//3
                    c=label_list[i_2]-a*9-b*3
                    min_cord_2=[a*5,b*5,c*5]
                    label_list_2=getposition_2(min_cord_2,check)
                    final_multi_label_2=np.zeros(3*3*3)
                    for label_number in label_list_2:
                        final_multi_label_2[label_number]=1
                    labels2_loss_mid.append(final_multi_label_2)
                    labels2_mid.append(label_list_2)
                labels2_loss.append(labels2_loss_mid)
                labels2.append(labels2_mid)
            labels1_loss1=torch.from_numpy(labels1_loss1)
            #labels1_loss2=torch.from_numpy(labels1_loss2)
            #labels1_loss3=torch.from_numpy(labels1_loss3)
            #labels2 = np.array(labels2)
            #labels2=torch.from_numpy(labels2)
            #labels3 = np.array(labels3)
            #labels3=torch.from_numpy(labels3)
            #labels = labels.astype(np.float32)
            #labels=torch.from_numpy(labels)
            #labels=torch.topk(labels, 1)[1].squeeze(1)
            #print("final",labels)
            #print("loss",labels1_loss)
            return images_3d, image_2d, labels1,labels1_loss1,labels2,labels2_loss

    def parse_csv_file(self):
        self.file_path_train=[]
        self.file_path_val=[]
        self.file_path_test=[]
        random.seed(3407)
        #random.seed(10)
        train_big_block=range(0,8*8*8)
        val_big_block=range(0,8*8*8)
        test_big_block=range(0,8*8*8)
        '''train_small_block=random.sample(range(0,20),6)
        remain_small_block=list(set(list(range(0,20)))-set(train_small_block))
        val_small_block=random.sample(remain_small_block,2)
        test_small_block=random.sample(list(set(remain_small_block)-set(val_small_block)),2)'''
        for i in train_big_block:
            i_1=i//64
            i_2=(i%64)//8
            i_3=(i%64)%8
            train_small_piece=random.sample(range(0,17*17),100)
            remain_small_piece=list(set(list(range(0,17*17)))-set(train_small_piece))
            val_small_piece=random.sample(remain_small_piece,10)
            test_small_piece=random.sample(list(set(remain_small_piece)-set(val_small_piece)),10)
            i_6_list=random.sample(range(0,20),2)
            for t in train_small_piece:
                i_4=t//17
                i_5=t%17
                if 17>=i_4>=2 and 17>=i_5>=2:
                    for i_6 in i_6_list:
                        self.file_path_train.append([i_1,i_2,i_3,i_4,i_5,i_6])
            for t in val_small_piece:
                i_4=t//17
                i_5=t%17
                if 17>=i_4>=2 and 17>=i_5>=2:
                    for i_6 in i_6_list:
                        self.file_path_val.append([i_1,i_2,i_3,i_4,i_5,i_6])
            for t in test_small_piece:
                i_4=t//17
                i_5=t%17
                if 17>=i_4>=2 and 17>=i_5>=2:
                    for i_6 in i_6_list:
                        self.file_path_test.append([i_1,i_2,i_3,i_4,i_5,i_6])
        '''for i in val_big_block:
            i_1=i//64
            i_2=(i%64)//8
            i_3=(i%64)%8
            small_piece=random.sample(range(0,17*17),100)
            for t in small_piece:
                i_4=t//17
                i_5=t%17
                if i_4>=2 and i_5>=2:
                    for i_6 in val_small_block:
                        self.file_path_val.append([i_1,i_2,i_3,i_4,i_5,i_6])
        for i in test_big_block:
            i_1=i//64
            i_2=(i%64)//8
            i_3=(i%64)%8
            small_piece=random.sample(range(0,17*17),100)
            for t in small_piece:
                i_4=t//17
                i_5=t%17
                if i_4>=2 and i_5>=2:
                    for i_6 in test_small_block:
                        self.file_path_test.append([i_1,i_2,i_3,i_4,i_5,i_6])'''
        if self.split == 'train':
            self.totalLength = len(self.file_path_train)
            #print(len(self.file_path_train))
        elif self.split=='val':
            self.totalLength = len(self.file_path_val)
        else:
            self.totalLength = len(self.file_path_test)

    def parse_csv_file2(self):
        self.file_path_train=[]
        self.file_path_val=[]
        self.file_path_test=[]
        random.seed(3407)
        #random.seed(10)
        train_big_block=range(0,8*8*8)
        val_big_block=range(0,8*8*8)
        test_big_block=range(0,8*8*8)
        for i in train_big_block:
            i_1=i//64
            i_2=(i%64)//8
            i_3=(i%64)%8
            #train_small_piece=random.sample(range(0,4*4),15)
            train_small_piece=list(range(0,4*4))
            val_small_piece=list(range(0,4*4))
            test_small_piece=list(range(0,4*4))
            #remain_small_piece=list(set(list(range(0,17*17)))-set(train_small_piece))
            #val_small_piece=random.sample(remain_small_piece,10)
            #test_small_piece=random.sample(list(set(remain_small_piece)-set(val_small_piece)),10)
            #i_6_list=list(range(0,20,4))
            i_6_list=[19]
            for i_6 in i_6_list:
                '''self.file_path_train.append([i_1,i_2,i_3,18,18,19])
                self.file_path_val.append([i_1,i_2,i_3,18,18,19])
                self.file_path_test.append([i_1,i_2,i_3,18,18,19])
                self.file_path_train.append([i_1,i_2,i_3,2,2,19])
                self.file_path_val.append([i_1,i_2,i_3,2,2,19])
                self.file_path_test.append([i_1,i_2,i_3,2,2,19])'''
                if i_6<=15:
                    self.file_path_train.append([i_1,i_2,i_3,i_6+2,i_6+2,i_6])
                    self.file_path_val.append([i_1,i_2,i_3,i_6+2,i_6+2,i_6])
                    self.file_path_test.append([i_1,i_2,i_3,i_6+2,i_6+2,i_6])
                else:
                    self.file_path_train.append([i_1,i_2,i_3,18,18,i_6])
                    self.file_path_val.append([i_1,i_2,i_3,18,18,i_6])
                    self.file_path_test.append([i_1,i_2,i_3,18,18,i_6])
            '''for t in train_small_piece:
                i_4=t//4
                i_5=t%4
                if 17>=i_4>=2 and 17>=i_5>=2:
                    self.file_path_train.append([i_1,i_2,i_3,i_6+j,i_6+k,i_6])
                else:
                    self.file_path_train.append([i_1,i_2,i_3,17,17,i_6])'''
            '''for i_6 in i_6_list:
                if 17>=i_6 and 17>=i_6:
                    self.file_path_train.append([i_1,i_2,i_3,i_6+2,i_6+2,i_6])
                else:
                    self.file_path_train.append([i_1,i_2,i_3,17,17,i_6])'''
            '''for i_6 in i_6_list:
                if 2<=i_6<=17:
                    for j in [0,1,2]:
                        for k in [0,1,2]:
                            self.file_path_train.append([i_1,i_2,i_3,i_6+j,i_6+k,i_6])
                elif i_6>17:
                    self.file_path_train.append([i_1,i_2,i_3,17,17,i_6])
                else:
                    self.file_path_train.append([i_1,i_2,i_3,2,2,i_6])
            for t in val_small_piece:
                i_4=t//17
                i_5=t%17
                if 17>=i_4>=2 and 17>=i_5>=2:
                    for i_6 in i_6_list:
                        self.file_path_val.append([i_1,i_2,i_3,i_4,i_5,i_6])
            for t in test_small_piece:
                i_4=t//17
                i_5=t%17
                if 17>=i_4>=2 and 17>=i_5>=2:
                    for i_6 in i_6_list:
                        self.file_path_test.append([i_1,i_2,i_3,i_4,i_5,i_6])'''
        if self.split == 'train':
            self.totalLength = len(self.file_path_train)
            #print("trian",len(self.file_path_train))
        elif self.split=='val':
            self.totalLength = len(self.file_path_val)
        else:
            self.totalLength = len(self.file_path_test)

    
    def parse_csv_file1(self):
        self.file_path_train=[]
        self.file_path_val=[]
        self.file_path_test=[]
        random.seed(3407)
        #random.seed(10)
        train_big_block=range(0,1*1*1)
        val_big_block=range(0,1*1*1)
        test_big_block=range(0,1*1*1)
        for i in train_big_block:
            i_1=i//1
            i_2=(i%64)//1
            i_3=(i%64)%1
            train_small_piece=random.sample(range(0,17*17),100)
            remain_small_piece=list(set(list(range(0,17*17)))-set(train_small_piece))
            val_small_piece=random.sample(remain_small_piece,1)
            test_small_piece=random.sample(list(set(remain_small_piece)-set(val_small_piece)),1)
            #i_6_list=random.sample(range(0,20),5)
            i_6_list=list(range(0,20,2))
            for t in train_small_piece:
                i_4=t//17
                i_5=t%17
                if i_4>=2 and i_5>=2:
                    for i_6 in i_6_list:
                        self.file_path_train.append([i_1,i_2,i_3,i_4,i_5,i_6])
            for t in val_small_piece:
                i_4=t//17
                i_5=t%17
                if i_4>=2 and i_5>=2:
                    for i_6 in i_6_list:
                        self.file_path_val.append([i_1,i_2,i_3,i_4,i_5,i_6])
            for t in test_small_piece:
                i_4=t//17
                i_5=t%17
                if i_4>=2 and i_5>=2:
                    for i_6 in i_6_list:
                        self.file_path_test.append([i_1,i_2,i_3,i_4,i_5,i_6])
        if self.split == 'train':
            self.totalLength = len(self.file_path_train)
            #print(len(self.file_path_train))
        elif self.split=='val':
            self.totalLength = len(self.file_path_val)
        else:
            self.totalLength = len(self.file_path_test)

    def on_epoch_end(self):
        if self.split == 'train':
            np.random.shuffle(self.file_path_train)

    def _load_one_image(self, d,image_path):
        #print(d.shape)
        #print(image_path)
        final_3d=d[0,image_path[0]*20:image_path[0]*20+20,image_path[1]*20:image_path[1]*20+20,image_path[2]*20:image_path[2]*20+20]
        #print(final_3d.shape)
        #final_3d = np.expand_dims(final_3d, axis=3)
        #print(final_3d.shape)
        return final_3d

    def _rotate_idx(self, l, m):
        for i in range(len(l)):
            while l[i] >= m:
                l[i] = l[i] - m
        return l

    def _load_batch_image_train(self, idx):
        idxlist = [*range(idx * self.batch_size, (idx + 1) * self.batch_size)]
        #print(idxlist)
        idxlist = self._rotate_idx(idxlist, len(self.file_path_train))
        #print(idxlist)
        #print("get2")
        images_3d = np.zeros((self.batch_size, *self.dim, self.n_channels))
        images_2d_list=[]
        #print(self.imaged.shape)
        for i in range(self.batch_size):
            #print(self.file_path_train[idxlist[i]])
            images_3d[i, :, :, :, 0] = self._load_one_image(self.imaged,self.file_path_train[idxlist[i]])
            images_2d_list.append([self.file_path_train[idxlist[i]][3],self.file_path_train[idxlist[i]][4],self.file_path_train[idxlist[i]][5]])
        return images_3d,images_2d_list

    def _load_batch_image_test(self, idx):
        idxlist = [*range(idx * self.batch_size, (idx + 1) * self.batch_size)]
        idxlist = self._rotate_idx(idxlist, len(self.file_path_test))
        images_3d = np.zeros((self.batch_size, *self.dim, self.n_channels))
        images_2d_list=[]
        for i in range(self.batch_size):
            images_3d[i, :, :, :, 0] = self._load_one_image(self.imaged,self.file_path_test[idxlist[i]])
            images_2d_list.append([self.file_path_test[idxlist[i]][3],self.file_path_test[idxlist[i]][4],self.file_path_test[idxlist[i]][5]])
        return images_3d,images_2d_list

    def _load_batch_image_val(self, idx):
        idxlist = [*range(idx * self.batch_size, (idx + 1) * self.batch_size)]
        idxlist = self._rotate_idx(idxlist, len(self.file_path_val))
        images_3d = np.zeros((self.batch_size, *self.dim, self.n_channels))
        images_2d_list=[]
        for i in range(self.batch_size):
            images_3d[i, :, :, :, 0] = self._load_one_image(self.imaged,self.file_path_val[idxlist[i]])
            images_2d_list.append([self.file_path_val[idxlist[i]][3],self.file_path_val[idxlist[i]][4],self.file_path_val[idxlist[i]][5]])
        return images_3d,images_2d_list

