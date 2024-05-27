import numpy as np


# 计算准确率
def accuracy(pred, label):
    return np.mean(pred == label)


# 计算混淆矩阵
def confusion_matrix(pred, label):
    cm = np.zeros((max(label)+1, max(label)+1), dtype='int32')
    for y, x in zip(pred, label):
        cm[y, x] += 1
    return cm
