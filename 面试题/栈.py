class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def isEmpty(self):
        return self.items == []

    def pop(self):
        if self.items == []:
            return []
        else:
            return self.items.pop()

    def peek(self):
        if self.items == []:
            return []
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)


stack = Stack()

# 案例简单括号匹配
# 十进制转化为二进制

def divideBy2(num):
    while num > 0:
        remainder = num % 2
        num = num // 2
        stack.push(remainder)

    result = ''
    while not stack.isEmpty():
        result = result + str(stack.pop())

    print(result)

from pythonds.basic.stack import Stack

if __name__ == '__main__':
    divideBy2(10)