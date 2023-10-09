# PaddleSpeech quickstart

在centos7快速启动PaddleSpeech示例

## 环境

- centos7
- python3.8

## 安装conda

```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

## 创建 conda 虚拟环境

创建一个 conda 的虚拟环境：

```
conda create -y -p tools/venv python=3.8
```

激活 conda 虚拟环境：

```
conda activate tools/venv
```

## 安装conda依赖

```
conda install -y -c conda-forge sox libsndfile bzip2
```

## 安装 C++ 编译环境

centos

```
sudo yum install gcc gcc-c++
```


## 安装 PaddleSpeech

部分用户系统由于默认源的问题，安装中会出现kaldiio安转出错的问题，建议首先安装pytest-runner：

```
pip install pytest-runner -i https://pypi.tuna.tsinghua.edu.cn/simple 
```

安装 paddlepaddle 和 paddlespeech

```
pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
pip install paddlespeech -i https://pypi.tuna.tsinghua.edu.cn/simple --use-pep517
```

## 下载 nltk_data

下载 nltk_data

```
wget https://paddlespeech.bj.bcebos.com/Parakeet/tools/nltk_data.tar.gz
```

解压到`${HOME}`目录下

```
tar -xvf nltk_data.tar.gz -C ${HOME}
```

## 运行程序

```
python main.py
```

## 运行报错解决方案

### 报错1：AttributeError: module 'numpy' has no attribute 'complex'.

如果出现下面报错，可能是librosa库的版本的问题

```
AttributeError: module 'numpy' has no attribute 'complex'.
`np.complex` was a deprecated alias for the builtin `complex`. To avoid this error in existing code, use `complex` by itself. Doing this will not modify any behavior and is safe. If you specifically wanted the numpy scalar type, use `np.complex128` here.
The aliases was originally deprecated in NumPy 1.20; for more details and guidance see the original release note at:
    https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations
```

解决方案：需要修改librosa库的版本，对于这个库的报错可忽略

```
pip install librosa==0.10.0
```

ref: https://github.com/PaddlePaddle/PaddleSpeech/issues/3291


### 报错2：ValueError: This ORT build has ['AzureExecutionProvider', 'CPUExecutionProvider'] enabled.

运行时出现如下错误

```
ValueError: This ORT build has ['AzureExecutionProvider', 'CPUExecutionProvider'] enabled. Since ORT 1.9, you are required to explicitly set the providers parameter when instantiating InferenceSession. For example, onnxruntime.InferenceSession(..., providers=['AzureExecutionProvider', 'CPUExecutionProvider'], ...)
```

解决方案：降低onnxruntime版本到1.9以下

```
pip3 install "onnxruntime<1.9"
```
