import random


def code1_1():
    pass


def code1_2(data):
    max_sum = 0
    n = len(data)
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += data[j]
            if sum > max_sum:
                max_sum = sum
    return max_sum


# print(code1_2([-1,-2,3,4,5,16,-10,11,-12,13]))


def code1_3(str1, str2):
    """
    最长公共子串
    字符串13455 与245576的最长公共子序列为455
    字符串acdfg与adfc的最长公共子序列为adf
    注意区分最长公共子串(Longest Common Substring)最长公共字串要求连续
    :param str1:
    :param str2:
    :return:
    """
    l = []
    # 先求出所有的子序列
    for index1, i in enumerate(str1):
        all_LSD = ''
        tmp_index1 = index1
        tmp_index2 = 0
        while tmp_index2 < len(str2):
            if tmp_index1 < len(str1):
                if str1[tmp_index1] == str2[tmp_index2] and str1[tmp_index1] in str2:
                    all_LSD += str1[tmp_index1]
                    tmp_index1 += 1
                    tmp_index2 += 1
                elif all_LSD == '':
                    tmp_index1 = index1
                    tmp_index2 += 1
                    continue
                else:
                    l.append(all_LSD)
                    all_LSD = ''
                    tmp_index1 = index1
                    tmp_index2 += 1
                    continue
            else:
                l.append(all_LSD)
                all_LSD = ''
                tmp_index1 = index1
                tmp_index2 += 1
                continue
    # length = sorted(l, key=lambda x:len(x), reverse=True)
    return l


#
# result = code1_3('abcd', 'abcefbcds')
# print(result)

import numpy as np

def LCS(s1, s2):
    """
    计算两个字符串的最长公共子序列.
    Parameters
    s1：字符串
    s2：字符串
    Returns
    B：二维Numpy数组标记函数值组成的矩阵
    C：二维Numpy数组优化函数值组成的矩阵
    """
    m = len(s1) + 1
    n = len(s2) + 1
    # 优化函数值矩阵
    # C[i][j]表示s1的前i个元素和s2的前j个元素的最长公共子序列的长度
    C = np.zeros((m, n))
    # 标记函数值矩阵
    # 记录当前优化函数值是从那个方向来的
    # B中元素取值解释--0：左，1：上，2：左上
    B = np.zeros((m, n))
    for i in range(1, m):
        for j in range(1, n):
            if s1[i - 1] == s2[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
                B[i][j] = 2
            else:
                if C[i - 1][j] >= C[i][j - 1]:
                    C[i][j] = C[i - 1][j]
                    B[i][j] = 1
                else:
                    C[i][j] = C[i][j - 1]
                    B[i][j] = 0
    max_long_str = []
    i = m - 1
    j = n - 1
    while i > 0 and j > 0:
        if B[i][j] == 2.0:
            max_long_str.append(s1[i-1])
            i -= 1
            j -= 1
        elif B[i][j] == 0.0:
            j -= 1
        elif B[i][j] == 1.0:
            i -= 1
    max_long_str.reverse()
    print(''.join(max_long_str))
    print(B, '\n')
    print(C)

# LCS("ABCBDAB", "BDCABA")


def code3_1(path='abc.txt', output_file='abc_del.txt'):
    """
    面试题02.jpg
    :param path: 文件路径
    :return: 删除文件中最少的词
    """
    word_count_dict = {}
    with open(path,'r', encoding='utf8') as f:
        for row in f:
            tmp = row.strip('\n').split('\t')
            for word in tmp:
                if word in word_count_dict:
                    word_count_dict[word] += 1
                else:
                    word_count_dict[word] = 1
    # 找到最小的count,并且pop出去
    min_count = min(word_count_dict.values())
    word_count_dict = [word for word, count in word_count_dict.items() if word_count_dict[word] > min_count]

    with open(output_file, 'w', encoding='utf8') as f:
        with open(path,'r', encoding='utf8') as f1:
            for row in f1:
                for word in word_count_dict:
                    if word in row:
                        row = row.replace(word,'')
                if row.strip():
                    f.write(row)

    # print(word_count_dict)
    # word_count_dict = sorted(word_count_dict.items(), key=lambda x:x[1])  # 必须加items
    # print(word_count_dict)
    print(word_count_dict)

# code3_1()


#
# def code4_1(data):
#     """
#     面试题3
#     :param data: 数组
#     :return: 最长数组
#     """
#     n = len(data)
#     i = 0
#     while n<0:
#         if data[i]



