"""
当排序的列表是不是整数，或者最大值和最小值相差太大的时候，就可以考虑桶排序
"""
import time


def bucketSort(data):
    """
    桶排序
    :param data:
    :return:
    """
    import numpy as np
    n = len(data)
    max_value = data[0]
    min_value = data[0]
    for i in range(n):
        if max_value < data[i]:
            max_value = data[i]
        if min_value > data[i]:
            min_value = data[i]

    gap = (max_value - min_value) / (n - 1)

    # 几个数字就是几个桶
    # bucket_list = [[]] * n   注意这样创建的每个字列表的地址id是一样的,故会出现莫名的坑
    bucket_list = [[] for _ in range(n)]

    for i in range(n):
        index = int((data[i] - min_value) / gap)  # 获取每个元素在哪个桶里面
        bucket_list[index].append(data[i])

    for i in range(n):
        if bucket_list:
            bucket_list[i].sort()
    result_list = []
    for i in range(n):
        result_list.extend(bucket_list[i])

    print(result_list)

if __name__ == '__main__':
    bucketSort([4.5, 0.84, 3.25, 2.18, 0.5,9.78,10,2.7])