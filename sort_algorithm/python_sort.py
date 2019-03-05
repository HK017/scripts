import numpy as np
import random

def bubble_sort(data):
    """
    冒泡排序是最简单也是最容易理解的排序方法，其原理就是重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
    走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
    动图url:'https://img2018.cnblogs.com/blog/1078628/201810/1078628-20181011120230796-1279095919.gif'
    :return: 每次比较两个数，将大的靠右排（涉及交换两个数的位置）
    """
    print('排序之前的数列为:', data)
    n = len(data)
    for j in range(n-1):
        for i in range(n-j-1):
            left = data[i]
            right = data[i+1]
            if left >= right:
                data[i+1],data[i] = left,right
    print('排序之后的数列为:', data)
    return data

def select_sort(data):
    """
    选择排序 基本思想：第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；
    以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。
    --永远将最小的数放在坐标
    :return:
    动图url:https://mmbiz.qpic.cn/mmbiz_gif/MQ4FoG1HmnIounJsWSXZfDLJt1kG3t5VoKfh7759sP997ylM8eZBYibOGiaKTicEviaKmbsjCYBzIbKic3icibZ6VYxpA/640?wx_fmt=gif
    """
    print('排序之前的数列为:', data)
    n = len(data)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if data[j] < data[min_index]:
                min_index = j
        if i != min_index:
            data[i],data[min_index]  = data[min_index],data[i]  # 交换位置
        print('第{}次循环,数列为:{}'.format(i, data))

    print('排序之后的数列为:', data)
    return data


def insert_sort(data):
    """
    插入排序
    :return:
    """
    pass

def stack_sort(data):
    """
    堆排序
    :return:
    """
    pass

def quick_sort(data):
    """
    快速排序:
    :return:
    """
    if data == []:
        return []
    else:
        smaller = [x for x in data[1:] if x < data[0]]
        larger = [x for x in data[1:] if x >= data[0]]

        return quick_sort(smaller) + [data[0]] + quick_sort(larger)

# 冒泡    n2
# 选择    n2
# 插入    n2
# 希尔    nlogn
# 归并    nlogn
# 快速    nlogn
# 堆      nlogn
# 计数排序 n+k
# 桶排序   n+k
# 基数排序 nxk



if __name__ == '__main__':
    random.seed(0)
    l = random.sample(range(1,11),10)  # 生成1,1000的20个不重复的随机数
    print('排序之前:',l)
    a = quick_sort(l)
    print('排序之后:', a)
    import sys
    print(sys.path)
