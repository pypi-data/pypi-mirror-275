from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="yifengw",
    #version="0.1.0",
    keywords=["test"],
    description="test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="test",
    #author_email="test",
    #url="test", # github项目连接
    license="MIT License", # 
    packages=["Yifengw"],
    install_requires=[ # 依赖包
        #"pandas", # panda包存在即可
        #"numpy >= 1.0", # numpy包要求版本 >1.0
        #"Django >= 1.11, != 1.11.1, <= 2", # 要求Django包版本在1.11至2之间，同时不等于1.11.1
        ],
    classifiers=[ # 其他配置项
        "License :: OSI Approved :: MIT License",
        # "Programming Language :: Python :: 2", # 注意现在的项目当有依赖包时支持python2是很危险的，不建议这样
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    package_data={ # 配置除了python代码外的其他数据、文件，会一起打包
        '': ['*.pkl'],
    }
)