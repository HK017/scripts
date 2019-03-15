import pandas as pd
import numpy as np
import time
from sklearn.datasets.samples_generator import make_classification
import matplotlib.pyplot as plt

def shuffleData(data):
    np.random.shuffle(data)
    y = data[:,-1]
    X = data[:,:-1]
    print('shuffle ', X.shape, theta.shape)
    return X, y


def sigmoid(X, theta):
    '''
    In[4]: import numpy as np
    In[5]: np.exp([1,2,3,4])
    Out[5]: array([ 2.71828183,  7.3890561 , 20.08553692, 54.59815003])
    :param X: x_data   x_data.shape[0]行 x_data.shape[1]列
    :param theta: parameter  x_data.shape[1] 行 1列
    :return:  x_data.shape[0] 行 1列
    '''
    return 1/(1 + np.exp((-1)*np.dot(X, theta)))  #

def loss(X, y, theta):
    print('loss ', X.shape, theta.shape)
    left = np.multiply(-y, np.log(sigmoid(X, theta)))
    right = np.multiply(1-y, np.log(1-sigmoid(X, theta)))
    return np.sum(left - right)/m

def gradient(X, y, theta):
    # 初始化梯度
    grad = np.zeros(theta.shape)
    print('grad ',X.shape, theta.shape)
    diff = sigmoid(X ,theta) - y
    for row in range(theta.shape[0]):
        term = np.multiply(diff, X[:, row])
        grad[row, 0] = np.sum(term)/len(X)

    return grad




def stopCriterion(type, value, threshold):
    # 设定三种不同的停止策略
    if type == STOP_ITEM:
        return value > threshold  # value为迭代次数
    if type == STOP_COST:
        return abs(value[-1]-value[-2]) < threshold
    if type == STOP_GRAD:
        return np.linalg.norm(value) < threshold   # 求范数，默认为二范数

# 进行参数theta更新
def gradient_descent(data, X, y, theta, batchsize, stopType, thresh, alpha):

    init_time = time.time()
    i = 0   # 记录迭代次数
    k = 0   # 记录batch的大小，用于判断
    losses = [loss(X, y, theta)]       # 存放每次迭代的平均损失值

    while True:
        grad = gradient(X[k:k+batchsize], y[k:k+batchsize], theta)
        k += batchsize
        if k >= n:
            X, y = shuffleData(data)
            k = 0
        theta = theta - alpha*grad     # 参数更新
        losses.append(loss(X, y, theta))
        i += 1    #迭代次数加1

        if stopType == STOP_ITEM:
            value = i
        elif stopType == STOP_COST:
            value = losses
        elif stopType == STOP_GRAD:
            value = grad
        print('value:',value)
        if stopCriterion(stopType, value, thresh):
            break

    return theta, i-1, losses, grad, time.time() - init_time


if __name__ == '__main__':
    X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_classes=2, n_clusters_per_class=1)
    plt.scatter(X[:,0], X[:,1], marker='o', c=y)
    plt.show()
    one_array = np.ones([X.shape[0], 1])
    X = np.concatenate([one_array, X], axis=1)
    y = y[:,np.newaxis]

    m = X.shape[0]
    data = np.concatenate((X, y), axis=1)
    X = data[:,:-1]
    y = data[:,-1][:,np.newaxis]

    STOP_ITEM = 0
    STOP_COST = 1
    STOP_GRAD = 2
    # 设置参数
    alpha = 0.1
    n = 100
    iter_num = 1000
    theta = np.zeros([3, 1])
    theta, iter, cost, grad, dur = gradient_descent(data, X, y, theta, n, 0, iter_num, alpha)
    print(theta)
    print(iter)
    print(cost)
    print(grad)
    print(dur)