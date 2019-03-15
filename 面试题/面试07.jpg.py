# # 面试题2-1
lx = [1, 0, 0, 0, 1, 1, 1]
ly = [1, 1, 0, 0, 0, 1, 1]
def calu_acc_recall(lx, ly):
    n = len(lx)
    TP = 0
    FN = 0
    FP = 0
    TN = 0

    for i in range(n):
        if lx[i] == 1 and ly[i] == 1:
            TP += 1
        elif lx[i] == 1 and ly[i] == 0:
            FN += 1
        elif lx[i] == 0 and ly[i] == 0:
            TN += 1
        elif lx[i] == 0 and ly[i] == 1:
            FP += 1

    recall_score = TP / (TP + FN)
    accuracy = TP / (TP + FP)
    print(recall_score)
    print(accuracy)


# 面试题2-2
# data = [1, 2, 3, 2, 5, 0, 2, 0, 2, 1]
# print([i for i in data if i != 0])

# 面试题2-3
# 方法一：
# from pythonds.basic.stack import Stack
#
# str1 = 'i like you'
# l = str1.split(' ')
#
# s = Stack()
# for i in l:
#     s.push(i)
# result = []
# while not s.isEmpty():
#     result.append(s.pop())
# print(''.join(result))

# 方法二
# str1 = 'i like you'
# l = str1.split(' ')
# l.reverse()
# print(l)