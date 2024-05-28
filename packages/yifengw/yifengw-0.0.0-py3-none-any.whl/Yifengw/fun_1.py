from torch.utils.data import TensorDataset, DataLoader
import torch
from sklearn.datasets import make_classification
import numpy as np
import dill
import warnings

warnings.filterwarnings('ignore')
def fun_1():
    with open('../train_test.pkl','rb') as f:
        a = dill.load(f)
    '''train_loader = torch.utils.data.DataLoader(dataset_save,
                                                batch_size=1,
                                                shuffle=True,
                                                pin_memory=True,
                                                num_workers=1)'''
    return a