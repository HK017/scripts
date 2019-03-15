def count_sort(data):
    n = len(data)
    max_value = 0
    for i in range(n):
        if max_value < data[i]:
            max_value = data[i]
    count_list = [0] * (max_value+1)

    for i in range(n):
        count_list[data[i]] += 1

    output_list = []
    index = 0
    for i in range(max_value+1):
        if count_list[i] != 0:
            output_list[index:count_list[i]] = i
            index += count_list[i]

    return output_list

# output_list = count_sort([0,1,3,3,5,1,8,7,6,7,8,15,19,99,99,100])

def count_sort(data):
    """
    用字典减少空间复杂度
    :param data:
    :return:
    """
    n = len(data)
    count_dict = {}
    for i in range(n):
        if data[i] in count_dict:
            count_dict[data[i]] += 1
        else:
            count_dict[data[i]] = 1
    print(count_dict)
    count_list = sorted(count_dict.items(), key=lambda x:x[0])
    output_list = []
    print(count_list)
    for word in count_list:
        output_list += [word[0]] * int(word[1])

    return output_list

a = count_sort([0,1,3,3,5,1,8,7,6,7,8,15,19,99,99,100])
print(a)