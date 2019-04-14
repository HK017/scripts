# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 19:11:18 2018
@author: houkai
"""
'''
np.random.rand(10)   #生成0-1的随机数
np.random.randn(10)  #生成正态分布的随机数
'''
################列表############
#任何数据都可以

'''生成器'''
'''通过列表生成式，我们可以直接创建一个列表。
但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
那后面绝大多数元素占用的空间都白白浪费了。
所以，如果列表元素可以按照某种算法推算出来，
那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。
在Python中，这种一边循环一边计算的机制，称为生成器（Generator）'''

L = [x * x for x in range(10)]
L
'''返回值[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]'''
g = (x * x for x in range(10))
g
'''<generator object <genexpr> at 0x104feab40>'''
'创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator,'
'如果要一个一个打印出来，可以通过generator的next()方法'
'正确的方法是使用for循环，因为generator也是可迭代对象'
g = (x * x for x in range(10))
for n in g:
    print n

'''字典转化为list和pd.Series'''
dict1 = {'a':1,'b':2}
list(dict1)
pd.Series(dict1)


######深拷贝和浅拷贝  https://www.cnblogs.com/work115/p/5619541.html
# -*- config=utf-8 -*-
#数据的拷贝
a=[1,2,3,4,5,6,"a","C"];
b=a;# a 与 b 的地址空间相同
a.append("b");
b.append("f");
print(b,a);#[1, 2, 3, 4, 5, 6, 'a', 'C', 'b', 'f'] [1, 2, 3, 4, 5, 6, 'a', 'C', 'b', 'f'] 当改变a的时候b也变 改变b a也变
print(id(b),id(a)); # 11075528 11075528 地址空间相同
###############################################
import copy;
#拷贝就是对内存中数据的应用
# 这就是浅拷贝
list=[1,2,3,4,["a","b","c"]];
list_1=copy.copy(list);
print(list,list_1)
print(id(list),id(list_1)); #11367752 10970440 地址空间不同 彼此的地址空间不同
list.append("5");
print(list,list_1);#[1, 2, 3, 4, ['a', 'b', 'c'], '5']  [1, 2, 3, 4, ['a', 'b', 'c']] list 改变 但 list_1 并没有变
print(id(list[0]),id(list_1[0]));# 1394274096  1394274096 他们各自元素的地址空间还是相同的
list[4].append("d");
print(list,list_1);#[1, 2, 3, 4, ['a', 'b', 'c', 'd'], '5']  [1, 2, 3, 4, ['a', 'b', 'c', 'd']] 都变了

# 深拷贝
list_2=[1,2,3,4,["a","b","c"]];
list_3=copy.deepcopy(list_2);
print(id(list_2),id(list_3));#17402824 17402248 地址不同
print(id(list_2[4]),id(list_3[4])); #11241032 11242056  地址不同
list_2[4].append("d");
print(list_2,list_3);#[1, 2, 3, 4, ['a', 'b', 'c', 'd']] [1, 2, 3, 4, ['a', 'b', 'c']]  list_3 没改变


##########################################################黑马程序元的笔记###############################
python2.x和python3.x的数据类型唯一的区别在于int
python2.x中 有int（2 ** 32）和long(2 ** 64 输出时会加上L在末尾)
python2.x中 只有int 都没有L在末尾


不同变量之间的计算（数字型数据可以直接计算）
布尔型  True 是 1 参与运算 False 是0 参与运算
int + float = float

字符串变量使用 '+' 进行拼接
print('=' * 100)  # 100个=号

数字型变量和字符串不能进行计算

数据类型转化
int('123')  # 不报错
int('a1')  # 报错

float('123') # 不报错


格式化输出
%s 为字符串输出 
%06d 整型输出 print('%06d' % 1)
%.2f 为浮点型输出 表示小数点后只显示2位


标识符 就是变量名和函数名(区分大小写)
名字需要见名知意
字母、下划线和数字组成，不能以数字开头
不能使用关键字重名

逻辑运算
and or not 
name = True
if not name:
	print(True)

赋值运算符 = += -= *= /= //= 

函数定义前面要有两个空行
函数的返回值 函数的return后面的代码不会执行

函数的嵌套调用 -- 函数中调用函数

pyc文件 __pycache__目录（cache表示缓存文件.pyc编译过的文件）


高级变量类型
-列表
-元组
-字典
-字符串
-公共方法
	len()
	del(变量) # 删除变量
	max()


-变量高级

数据类型 分为 数字型和非数字型
空对象的len为0
l = (1, 2, [])
print(len(l))  # 输出3

数字型
	int
	float
	str
	布尔型
非数字型
	--列表 可变类型、有序、可储存不同类型的数据，可遍历
	排序 列表.sort() 默认升序
	列表的操作 11个
	1.增加 insert(index, 数据)，append(),extend() 
		append和extend的区别 
		l = [1, 'a']
		l.extend([1, 2, 3])
		输出 [1, 'a', 1, 2, 3]
		l.extend([1, 2, 3]) # 合并列表,合并列表和元组，只要是一个可迭代对象，都可以合并为一个类型
		输出 [1, 'a', [1, 2, 3]]

	2.修改 索引即可
	3.删除 clear(),pop(),
		   del 列表[索引] 也可以删除变量,
		   列表.remove(), 
		   clear() 列表清空
	4.统计 列表.count(),len(列表)
	5.排序 列表.sort(),列表.sort(reverse=True),列表.reverse() 翻转
		sort()函数 可以对字典中的key和value排序   ---------------很重要
	6.查找 列表.index() 获取数据第一次出现的索引位置 不在列表中会报错

	--元组 不可变类型、有序、可储存不同类型的数据，可遍历，格式化
		不能进行增删改的操作
		可以索引
		1.计数 元组.count()
		2.查找 元组.index()

	-字典 可变类型、无序、键值对、可遍历，不能切片 （字典的键只能是不可变类型 字符串或者数字类型）
		
		1.取值
			字典[key]     # 没有key会报错
			字典.get(key) # 不会报错
		2.增加/修改
			字典[key] = 值   # 没有key就增加
			字典.set(key,值) # 增加或修改
		3.删除
			字典.pop(key)
		4.排序
			sort(key=)
		5.合并
			字典.update(字典2)  # 同名的键，会覆盖原有的键的值
		6.清空字典
			字典.clear()
		7.遍历	
			for k in 字典：
				print('%s-%s' %(k,字典[k]))
			字典.keys() 所有value的列表
			字典.values() 所有key的列表
			字典.items() 所有（key,value）元组列表
	-字符串 不可变类型、有序、可遍历（一个一个字母遍历）、双引号和单引号可以相互包起来
		len(字符串)
		字符串.index(元素)
		字符串.count(元素)
		字符串[索引] 或 字符串[开始索引:结束索引:步长] 
		常见的方法:
		  string.startswith()
		  string.endswith()
		  string.replace() # 不赋值就不会修改原有的字符串
		  string.isspace()  
		  string.isalnum()  
		  string.lower() # 转小写
		  string.upper() # 转大写
		  string.strip() # 去掉左右的空格，不能去掉中间的空格  
		  string.split(符号,) # 根据某一个符号分割，返回列表，不传入指定分割符号，默认用空白字符（包括制表符，换行符，回车，空格）分割
		  '指定符号'.join(可迭代对象)  # 用符号链接可迭代对象的每个元素
		  string.index(元素) # 查找的元素不存在会报错
		  string.find(元素)  # 查找的元素不存在，不会报错返回-1

		  字符串的逆序（步长为-1,开始索引为-1）
		  l = "'a',1"
		  print(l[-1::-1])
元组和列表之间的转化
list(元组)
tuple(列表)

列表中可以嵌套字典和元组

所有的切片都有两把刀切取中间的数据，故取不到最后一个数据，左闭右开区间
倒序索引从末尾索引  即开始索引为-1 ,反序输出

l = "'a',1"
print(l[-1::-1]) # 输出 1,'a'

空白字符包含
\t  制表符
\n  换行符
\r  回车
空格


{}中没有键值对的话，它的类型是一个set

运算符
[1,2]*5  # 返回[1,2,1,2,1,2,1,2,1,2]
(1,2)*5  # 返回(1,2,1,2,1,2,1,2,1,2)
'a' * 5  # 返回'aaaaa'
{'a':1,'b':2}*3 # 报错，因为字典的键必须是唯一的

拼接操作 列表、元组、字符串都可以拼接,但字典不行
[1,2] + [3,4] # 返回 [1,2,3,4] 
(1,2) + (3,4) # 返回 (1,2,3,4)
 'a' + 5


*              支持 字符串、列表、元组
+ 			   支持 字符串、列表、元组
in 和 not in   支持 字符串、列表、元组、字典（只能判断key）
for i in 迭代对象:
	print(i)
else:
	没有通过break退出循环，循环结束后，会执行的代码；如果break结束的，不会执行else
应用场景： 如果不满足条件，则得到统一的提示

shebang
#! /usr/bin/python3 (python3的解释器)  结论这句可以直接在终端直接启动程序

变量引用 变量中记录数据的地址
a = 1
a指向储存1的地址 id


列表、字典   使用赋值=时，会改变id，但是对列表本身增删改不改变id
全局变量 可以在函数中使用，但是不能在函数中修改，除非在函数内部使用global，可修改全局变量
		如果函数传递的是全局变量是可变类型的参数，在函数修改参数的值，同样也会修改全局变量的值

缺省参数 参数给定默认值
注意事项 ，1.缺省参数必须在参数列表的末尾，如果后面有形参，会报错
		  2.缺省参数必须以键值对的形式传入

多值参数
  参数名前增加1个*可以接受元组  即*args
  参数名前增加2个**可以接受字典 即**kwargs

例子： 
def demo(num, *args, **kwargs):
	print(num)
	print(*args)
	print(**kwargs)
demo(1,2,3,4,5)                          # 1对应num的值，而2,3,4,5是一个元组会传给*args，**kwargs没有传入值
demo(1,2,3,4,5, name='小明',age=18)       # 1对应num的值，而2,3,4,5是一个元组会传给*args，{'name':'小明','age':18}传给**kwargs


元组和字典的拆包
在调用带有多值参数的函数时，如果希望：
	将一个元组变量，直接传递给args
	将一个字典变量，直接传递给**kwargs
就可以使用拆包，简化参数的传递，拆包的方式是：
	在传递的实参元组变量的前面，增加一个*
	在传递的实参字典变量的前面，增加一个**

demo(*args, **kwargs):
	print()
tup1 = 1,2,3,4
dict1 = {'name':'zs','age':54}
demo(*tup1, **dict1)


面向对象
dir(标识符) # 查看对象的属性和方法
__名字__  针对对象的内置方法和属性
__doc__ 对象文档
__new__ 创建对象时，会自动调用
	使用类名创建对象时，Python的解释器首先会调用，首先会调用__new__方法为对象分配内存空间
	主要作用：1.在内存中为对象分配空间；2.返回对象的引用
	python的解释器获取对象的引用后，将引用作为第一个参数,传递给__init__方法中的self

	重写__new__方法一定要return super().__new__(cls),否则python的解释器得不到分配的对象引用，就不会调用对象的初始化方法
	注意：__new__是一个静态方法，在调用时需要主动传递cls参数
__name__ 	

单例设计模式
目的 -- 让类创建的对象，在系统中只有一个唯一的一个实例
每一次执行 类名() 返回的对象，内存地址是相同的


###############################################################################
empty = []
empty.append(1)
len(empty)
empty.extend([1,2,3,4])    #添加可迭代对象
empty.insert(1,2)
empty.extend(['a',1])
#从该列表中获取元素
empty[2]
#从该列表中删除元素
empty.remove('a')
del empty[2]
#计数
empty.count()
empty.sort()
empty.sort(reverse = True)
empty.pop(1)
#列表切片
empty[:3]
#列表的拷贝,不改变元列表
empty1 = empty[:]
empty1[1] = 'a'
empty.copy()
#以下赋值不规范，会导致错误
empty1 = empty

#################################333##############################################

#列表的操作
in
not in

'小甲鱼' in empty
'小甲鱼' not in empty
list = [123,['小甲鱼','牡丹'],456]
'小甲鱼' in list

dir(list)
list[1].index('小甲鱼')
#######################元组#################################
#对列表进行限制
区别：元组不能修改，列表可以随便修改
创建元组
tup = (1,2,3,4,5,6,7,8)

tup[1]
tup1 = tup[:]  #拷贝
tup1[1] = '小甲鱼'  #报错
tup = 2,3,4
tup1 = (1,)  #只有一个元素的要加上逗号才会为元组
#更新和删除元组的元素
temp= ('小甲鱼','黑夜','小不点')
temp = temp[:2] + ('一点',) + temp[2:]   #拼接操作
temp *8
in
not in
######################内置方法#########################
#字符串和元组一样不能修改
str1 = '  i love fishc.com   '
str1[:6]
#字符串的方法:
str1.join('222')  #将str1加入到222中去
str1.capitalize()  #使首字母大写
str1.lower()
str1.upper()

str1.find('c')  #找到返回字符串，否则返回-1
str1.index('i')
str1 = '  i love fishc.com   '
str1.strip()    #去掉字符串两边所有的空格
str1.strip('i') #去掉字符串两边所有的i
str1.lstrip()   #去掉左边的所有空格
str1.rstrip()   #去掉右边的所有空格
str1.replace('i','替换的字符')   #替换所有的i
str1.split(' ')   #分割字符串,返回一个列表
##index和find的区别在于：如果找不到字符串,index将会引发一个异常（而不是返回-1）
str1.index('i')
str1.find('i')

#字符串的格式化
"{} love {}.{}".format('i','fishc','com')
#位置参数
"{0} love {1}.{2}".format('i','fishc','com')

#关键字参数,其必须带有关键字民称
"{a} love {b}.{c}".format('i','fishc','com')   #报错

"{a} love {b}.{c}".format(a= 'i',b = 'fishc',c = 'com')   #报错

#位置参数和关键字参数的混用，位置参数必须在关键字参数之前
"{0} love {b}.{c}".format('i',b = 'fishc',c = 'com')

"{0:0.1f}{1}".format(56.78,'GB')  #必须有位置参数民称

"%.2f%s" %(0.75,'GB')  #必须有位置参数民称
'%d%s' %(2,'GB')


#字符转义

####################序列#########################
a = 'i love fishc.com'
a = list(a)  #将a这个可迭代对象转化为列表
tuple(a)     #将a这个可迭代对象转化为元组
numbels =[1,18,56,43,56,-1]
max(numbels)
min(numbels)
sum(numbels)
sorted(numbels)

enumerate(numbels)  #返回对象我们可以应用list强制转化为list
list(enumerate(numbels))

a = [1,2,3,4,5,6,7,8]
b = [4,5,6,7,8]

list(zip(a,b))  #生成最小长度的list

zip_list = list(zip(a,b))  #生成最小长度的list
zip_list.sort(key = lambda x:x[0],reverse = True)   #根据第一个位置降序
zip_list.sort(key = lambda x:x[1],reverse = False)  #根据第一个位置升序


##############内嵌函数#################
函数里面内套函数
##############闭包####################
在函数内用外部变量调用的函数称为闭包
def func(x):
    def funy(y):
        return x * y
    return funy
#调用
i = func(5)
i(8)
#非全局变量的外部变量不能够调用函数
def funx():
    '''这里的x不是全局变量，他是非全局变量的外部变量'''
    x = 5
    def funy():
        x *= x
        return x
    return funy()
funx()
'这么调用报错'
'local variable 'x' referenced before assignment'

但是可以用容器去做
1.
def funx():
    '''这里的x不是全局变量，将它改为容器类型'''
    x = [5]
    def funy():
        x[0] *= x[0]
        return x
    return funy()
funx()
2.使用关键字nonlocal
def funx():
    '''这里的x不是全局变量，他是非全局变量的外部变量'''
    x = 5
    def funy():
        nonlocal x
        x *= x
        return x
    return funy()
funx()

#############lambda 表达式（匿名函数）#############
def ds(x):
    return 2*x+1
'''lambda的冒号前是参数，后面是函数的返回值'''
lambda x:x*2+1

def add(x,y):
    return x+y
add = lambda x,y:x+y
add(1,2)

##########BIF#############
list(filter(None,[1,2,0,True,False]))  #过滤任何非0和假的数出来

def odd(x):
    return x%2
list(filter(odd,[1,2,0,True,False]))  #过滤掉不能被2整除的数出来

temp = range(10)
list(filter(lambda x:x%2,temp))

list(map(lambda x:x*2,range(10)))  #把range（10）的每个元素放入x中去进行运算之后返回一个序列

def orde(x):
    return sorted(x,reverse = True)
temp = [2,3,7,5,4]
list(filter(lambda x:x*2,temp))   #做过滤
list(map(lambda x:x*2,temp))      #做运算得到返回值

##################递归###################### 分治思想
树结果用递归
函数调用自身就是递归
迭代比递归速度快

100层递归
import sys
sys.setrecursionlimit(100)

'''用递归求阶乘'''
1.非递归版本
def jie_cheng(n):
    result = n
    for i in range(1,n):
        result *= i
    return result
number = int(input('请输入一个整数:'))
jie_cheng(number)
2.递归版本
def jie_cheng(n):
    if n ==1:
        return 1
    else:
        return n * jie_cheng(n-1)
number = int(input('请输入一个整数:'))
result = jie_cheng(number)
print('%d 的阶乘是：%d' % (number,result))
'''实现费波纳契数列'''
1 2 3 4 5 6  7  8  9  10
1 1 2 3 5 8 13 21 34  55

1.迭代版本
def fob(n):
    a = 1
    b = 1
    result = [1,1]
    for i in range(2,n):
        result.append((a+b))
        a,b = b,a+b
    return result,result[n-1]
number = int(input('请输入一个整数:'))
sque, result= fob(number)
result
2.递归版本
def fob1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fob1(n-1) + fob1(n-2)
number = int(input('请输入一个整数:'))
fob1(number)


###############字典（映射）######################
1.创建字典
dict1 = {'李宁':'一切皆有可能','耐克':'just do it'}
dict2 = dict(李宁='一切皆有可能',耐克='just do it')
2.索引
dict1['李宁']
3.赋值和添加元素
dict1['周杰伦'] = '七里香'
dict1['爱迪生'] = '天才就是99%的汗水+1%的灵感,但这1%的灵感更重要'
dict1['耐克'] = 'Just do it!'
4.属性
list(dict1.keys())
list(dict1.values())
list(dict1.items())
for x,y in dict1.items():
    print(x,'-->',y)
len(dict1)
5.批量创建字典
dict3 = {}
dict3.fromkeys((1,2,3),'Number')
dict3 = dict3.fromkeys(range(1,32),'赞')
6.查找是否存在某个键
in
not in
print(dict3.get(32,'木有这个键'))  #不存在32的键，打印木有这个键
32 in dict3
7.清除字典
dict3.clear()
8.前拷贝
dict4 = dict3.copy()
id(dict4) == id(dict3)   #返回False
9.pop 和 popitem
dict3.pop(31)
dict3.popitem()  #随机弹出一个数据
###############set(集合)就是唯一###########
num = {1,2,3,4}
type(num)

1.set类型不支持索引'''TypeError: 'set' object does not support indexing'''
num[2]
2.创建集合
一。用花括号直接把一堆元素括起来即可
num = {1,2,3,4,5}
二。用set()工厂函数
num1 = set((1,2,3,4,5))
num2 = set([1,2,3,4,5,5,2])

'''练习'''
要求:去掉列表中重复的元素
l = [0,1,2,3,4,5,5,3,1]
list(set(l))           #用list会排序
3.访问集合中的值
一。用for循环
for i in num2:



二。可以通过in和not in判断一个元素是否在集合中
1 in num2

4.集合的add方法
num2.add(6)
num2.remove(5)
5.不可变集合
num3 = frozenset([1,2,3,4,5])
num3.add(6)
'''AttributeError: 'frozenset' object has no attribute 'add''''
################文件#####################
.exe  .txt  .avi  .jpg .mp4 .ppt

1.打开文件
mode = r
mode = w
mode = a
2.文件方法
file.close()
file.read()
file.readline()
file.readlines()
f.write(str)    #将字符串写入到file中
f.writelines()  #将字符串序列即list写入文件中
f = open('record.txt','r',encoding = 'utf-8')
list(f)        #将内容转化为list
f.read()
f.close()
3.文件指针
f.tell()   #返回文件指针的位置
f.seek(0,0)   #0表示从文件起始位置  1表示从当前位置  2 表示文件末尾
4.读取文件的每一行
f = open('record.txt','r',encoding = 'utf8')
for each_line in f:
    print(each_line)
f.tell()
f.seek(0,0)
f.close()

5.写东西
f = open('text.txt','w',encoding = 'utf8')
f.write('这是我写入文件的内容')
f.close()      #关闭之后才能看到
6.一个任务
将文件（record.txt）中的数据进行分割并按照以下规则保存起来：
-小甲鱼的对话单独保存在boy_*.txt的文件（去掉’小甲鱼：’）
-小客服的对话单独保存在girl_*.txt的文件（去掉‘小客服：’）
-文件中总共有三段对话，分别保存为boy_1.txt,boy_2.txt,boy_3.txt,girl_1.txt,girl_2.txt,girl_3.txt共六个文件（提示：
文件中不同的对话间已经使用‘=========’分割）
问题
1.怎么计数
2.怎么讲list写入文件中

####代码1
f = open('record.txt','r',encoding = 'utf-8')
boy = []
girl = []
#计数的count很重要
count = 1
for each_line in f:
    if each_line.startswith('='):
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'
        boy_file = open(file_name_boy,'w')
        girl_file = open(file_name_girl,'w')
        #将list用writelines写入文件中
        boy_file.writelines(boy)
        girl_file.writelines(girl)
        #文件写完之后一定要关闭
        boy_file.close()
        girl_file.close()
        #写完每一段对话之后要初始化
        boy = []
        girl = []
        #计数
        count +=1
    else:
        role,speak_word = each_line.split(':')
        if role == '小甲鱼':
            boy.append(speak_word)
        else:
            girl.append(speak_word)
#对最后一段对话进行单独保存
file_name_boy = 'boy_' + str(count) + '.txt'
file_name_girl = 'girl_' + str(count) + '.txt'
boy_file = open(file_name_boy,'w')
girl_file = open(file_name_girl,'w')
#将list用writelines写入文件中
boy_file.writelines(boy)
girl_file.writelines(girl)
#文件写完之后一定要关闭
boy_file.close()
girl_file.close()
f.close()

####代码2
def file_write(boy,girl,count):
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'
    boy_file = open(file_name_boy,'w')
    girl_file = open(file_name_girl,'w')
    #将list用writelines写入文件中
    boy_file.writelines(boy)
    girl_file.writelines(girl)
    #文件写完之后一定要关闭
    boy_file.close()
    girl_file.close()
def split_write(file_name):
    boy = []
    girl = []
    #计数的count很重要
    count = 1
    f = open(file_name,'r',encoding = 'utf-8')
    for each_line in f:
        if each_line.startswith('='):
            file_write(boy,girl,count)
            #写完每一段对话之后要初始化
            boy = []
            girl = []
            #计数
            count +=1
        else:
            role,speak_word = each_line.split(':')
            if role == '小甲鱼':
                boy.append(speak_word)
            else:
                girl.append(speak_word)
    file_write(boy,girl,count)
split_write('record.txt')

###############文件系统os和os.path##########
import os
print('当前工作目录为：',os.getcwd())
print('当前工作目录下所有的文件：',os.listdir())
print('改变当前工作目录',os.chdir('C:\\Users\\Administrator\\.spyder-py3'))
print('创建一个目录',os.mkdir('c:\\users\\administrator\\.spyder_py\\a'))
print('创建一个目录',os.system('cmd'))
print('当前系统',os.sep)

#返回文件名
os.path.basename('e:\\a\\b\\a.avi')
#返回路径名
os.path.dirname('e:\\a\\b\\a.avi')
#将多个参数整合为路径
os.path.join('c:\\','a','b','c')
#路径分割
os.path.split('e:\\a\\a.avi')
os.path.split('e:\\a\\ab')
#分割文件的后缀文
os.path.splitext('e:\\a\\ab\\a.mp4')

#pwd下是否存在1.txt
os.path.exists('1.txt')
.表示当前路径
..表示上级目录

课后作业

###############pickle模块##############
将对象转化为二进制苏数据存储起来
1.使用dump保存起来
import pickle
my_list = [123,'a',[1,2,3]]
pickle_file = open('my_list.pkl','wb')
pickle.dump(my_list,pickle_file)
pickle_file.close()

2.用load方法加载进来
pickle_file = open('my_list.pkl','rb')
my_list2 = pickle.load(pickle_file)
print(my_list2)
pickle_file.close()

############异常处理############
my_list = ['a']
assert len(my_list) > 0
AssertionError  assert
SyntaxError
TypeError   1+'1'
NameError
OSError     没有文件
ValueError  int('abc')

1.try-except语句
try:
    检测范围
except Exception[as reason]:
    出现异常后的处理代码
举例：
try:
    int('abc')
    sum = 1 +'1'
    f = open('我为什么是一个文件.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错了，\n错误的原因是：' + str(reason))
except TypeError as reason:
    print('类型出错了，\n错误的原因是：' + str(reason))
.当你不知道什么错误时：
try:
    int('abc')      #这里出错下面的语句不会运行
    sum = 1 +'1'
    f = open('我为什么是一个文件.txt')
    print(f.read())
    f.close()
except:
    print('出错了')
2.try-finally语句
try:
    检测范围
except Exception[as reason]:
    出现异常后的处理代码
finally:
    无论如何都会被会执行的语句
例子：
try:
    f = open('我为什么是一个文件.txt','w')
    print(f.write('我存在了！'))
    sum = 1 + '1'
except:
    print('出错了')
finally:
    f.close()

3.raise
raise ZeroDivisionError('除数为0的异常')


##############else语句和with语句###############
try:
    print(int('123'))
except ValueError as reason:
    print('出错了：' +str(reason))
else:
    print('没有任何异常！')


with语句
try:
    f =open('data.txt','w')
    for each_line in f:
        print(each_line)
except OSError as reason:
    print(reason)
finally:
    f.close()


try:
    with open('data.txt','w') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print(reason)

#################图形用户界面入门：EasyGui#################
import easygui as g
import sys

while 1:
    g.msgbox('这是我的第一个游戏界面！')


    msg = '请问你希望玩什么游戏？'
    title = '小游戏互动'
    choices = ['谈恋爱','学习c语言','打lol','看电视']
    choice = g.choicebox(msg,title,choices)
    g.msgbox('你的选择是：' +str(choice),'结果')


    msg = '你希望重新开始小游戏吗？'
    title = '请选择：'

    if g.ccbox(msg,title):    #show a continue/cancel gui
        pass
    else:
        sys.exit(0)

################类和对象###############
类即封装 继承 多态（多个类可以拥有同一个函数，不会出错）
对象 = 属性 + 方法
self 是什么? 类似指针
魔法方法以 __ 打头



class Ball():
    #属性
    def __init__(self,name,girl_friend):  #如果这里有默认参数可以不传入参数有也可以
        self.name = name
        self.girl_friend = girl_friend
    #方法即函数
    def kick(self):
        print('我叫%s' % self.name)
ball = Ball(name = '候凯',girl_friend = '丽娃')  #如果没有默认参数必须要给name和girl_friend赋值
ball.name
ball.kick()

共有和私有？
在python中定义私有变量只需要在变量名或函数名前加‘__’两个下划线,那么这个函数或变量就会为私有的了。
class Person:
    __name = '小甲鱼'
p = Person()
p.name
p.__name
#以上两种调用方法都会报错，只能从内部方法中进行调用

class Person:
    __name = '小甲鱼'
    def getName(self):
        return self.__name
p = Person()
#返回'小甲鱼'
p.getName()  #返回'小甲鱼'
p._Person__name

继承
class Parent:
    def hello(self):
        print('正在调用父类的方法...')
class Child(Parent):  #变量名称为父类名称
    pass

p = Parent()
p.hello()
c = Child()
c.hello()
#如果子类继承了父类，但子类hello方法会覆盖父类的hello方法
class Child:

    def hello(self):
        print('正在调用子类的方法...')
c = Child()
c.hello()


##############类代码#################
import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
    def move(self):
        self.x -= 1
        print('我的位置是:',self.x,self.y)
class GoldFish(Fish):
    pass
class Carp(Fish):
    pass
class Salmon(Fish):
    pass
class Shark(Fish):
    #子类重写了父类的方法，会覆盖掉父类的方法
    def __init__(self):
        super().__init__()     #用super继承父类的__init__属性
        self.hungry = True
    def eat(self):
        if self.hungry == True:
            print('吃货的梦敢就是天天有的吃...')
            self.hungry = False
        else:
            print('太撑了,吃不下了!!!')

#多重继承
class Base1:
    def foo1(self):
        print('我是foo1，我为Base1代言...')
class Base2:
    def foo2(self):
        print('我是foo2，我为Base2代言...')
class C(Base1,Base2):
    pass
c = C()
c.foo1()
c.foo2()

#拾遗
组合
现在要求定义一个类，叫水池，水池里面有乌龟和鱼。
class Turtle:
    def __init__(self,x):
        self.num = x
class Fish:
    def __init__(self,x):
        self.num = x
class Pool:
    def __init__(self,x,y):
        self.turtle = Turtle(x)  #self.turtle是实例化对象
        self.fish = Fish(y)
    def print_num(self):
        print('水池里总共有乌龟 %d 只,小鱼 %d 条!' %(self.turtle.num,self.fish.num))
pool = Pool(2,3)
pool.print_num()


###########类相关的BIF############
class A:
    pass
class B(A):
    pass
issubclass(B,A)           #B是否继承了A
issubclass(B,object)      #object是所有类的基类

isinstance(object,classinfo)   #检查object是否为classinfo的实例化对象
b = B()
isinstance(b,B)
isinstance(b,A)

#检查一个对象是否有某种属性
class C:
    def __init__(self,x=0):
        self.x = x
c = C()
hasattr(c,'x')      #c这个实例化对象是否有x这个属性
getattr(c,'x')      #得到c的x属性的值
getattr(c,'y','没有y这个属性')
setattr(c,'y','fishc')   #设置属性
getattr(c,'y')


delattr(c,'z')  #删除属性

1.可以直接赋值上不写size
class C:
    def __init__(self):
        self.size = 10     #可以直接赋值上不写size
    def getsize(self):
            return self.size
    def setsize(self,value):
            self.size = value
    def delsize(self):
            del self.size
c = C()
2.实例化时赋值
class C:
    def __init__(self,size):
        self.size = size
    def getsize(self):
        return self.size
    def setsize(self,value):
        self.size = value
    def delsize(self):
        del self.size
c = C(size =10)
3.定义时进行初始化
class C:
    def __init__(self,size =10):
        self.size = size
    def getsize(self):
        return self.size
    def setsize(self,value):
        self.size = value
    def delsize(self):
        del self.size
c = C()

####property

class C:
    def __init__(self,size = 10):
        self.size = size
    def getsize(self):
        return self.size
    def setsize(self,value):
        self.size = value
    def delsize(self):
        del self.size
    x = property(getsize,setsize,delsize)  #用属性去设置属性

c = C()
c.getsize()
c.x = 18
c.getsize()

魔法方法
__init__(为什么有时候写__init方法,有时候不写，原因在于需求)
class Rectange:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getPeri(self):
        return (self.x +self.y)*2
    def getArea(self):
        return self.x * self.y
rect = Rectange(3,4)
rect.getPeri()

__new__

class CapStr(str):
    def __new__(cls,string):
        string = string.upper()
        return str.__new__(cls,string)

a = CapStr('i love you')
a

__del__(self)


############迭代器###########
for i in "fishc":
    print(i)

links = {'1':'com','2':'cn','3':'blob','4':'baidu'}
for each in links:
    print(each)

string = 'fishc'
for each in links:
    print(each)


#生成器  ---------函数中加入一个yield --协调程序

def myGen():
    print('生成器被执行!')
    yield 1
    yield 2
myg =myGen()
next(myg)
for i in myGen():
    print(i)


#文件的读写
text = 'this is first test.'


'''copy和deepcopy'''
1.这种直接赋值a改变，会改变b
import copy
a = [1,2,3]
b = a
a[1] = 'a'
b[1]
2.用copy
c = copy.copy(a)
print(id(c) == id(a))
a = [1,2,[3,4]]

b = copy.copy(a)
id(a[2]) == id(b[2])   #返回True

#这种浅赋值也可能被改变
a = [1,2,[3,4]]
b = copy.copy(a)
a[0] = 11
a[2][0] = 333
b
3.copy.deepcopy
e = copy.deepcopy(a)
id(e[2]) == id(a[2])


#################numpy################
import numpy as np
'''矩阵定义'''
array= np.array([[1,2,3],[2,3,4]])
print(array.shape[1])
print(array.size)
print(array.ndim)
'''numpy 创建array'''
a = np.array([2,23,4],dtype = np.int)   #int32,int64,int16
a = np.array([2,23,4],dtype = np.float) #float32,float64
print(a.dtype)

a = np.array([[2,23,4],[1,2,3]],dtype = np.int)
a.astype(np.float)

a = np.zeros([3,4],dtype = np.int)
a = np.empty([3,4])
a = np.arange(10,20)
a = np.arange(12).reshape([3,4])
a = np.linspace(1,10,20)   #1-10的20个数
a = np.linspace(1,10,20).reshape([4,5])
'''numpy 基础计算'''
a = np.array([10,20,30,40])
b = np.arange(4)
a-b
a+b
a ** 2
a * b          #对应位置相乘
a.dot(b)       #点乘
np.dot(a,b)
np.floor()
np.ceil()
np.rint(0.56)

'''找到满足条件的下标'''
10 * np.sin(a)
b.sort()
b < 3
b[np.where(b<3)]
'''列表中使用index方法'''

arr=np.array([1,1,1,134,45,3,46,45,65,3,23424,234,12,12,3,546,1,2])
np.where((arr>3) & (arr<100))         # 找出arr中大于3且小于100的索引
arr[np.where((arr>3) & (arr< 100))]   # 找出arr中大于3且小于100的值
'''三元操作符'''
x if condition else y
np.where(arr>3,1,0)  #满足条件返回1，否则返回0
np.unique([1,2,3,4,2,3])

b = np.arange(4).reshape([2,2])
'''生成0-1的随机数字'''
a = np.random.random([2,4])
'''生成mean = 0,方差 = 1的2行4列服从正态分布的随机矩阵'''
a1 = np.random.normal(0,1,[2,4])
np.sum(a1,axis = 0)   #列求和
np.sum(a1,axis = 1)   #行求和
np.min(a1)
np.max(a1)
'''生成1-10的20个随机整数'''
a2 = np.random.randint(1,10,20)
'''生成1-10的3行4列的整数矩阵'''
a3 = np.random.randint(1,10,[3,4])

A = np.arange(2,14).reshape([3,4])
np.argmin(A)
np.argmax(A)
np.mean(A)
np.median(A)
np.argwhere(A == 4) #等于4在矩阵中的位置
np.sort(A)
np.transpose(A)  #矩阵的转置
A.T              #矩阵的转置
np.complex(1,2)  #复数,返回(1+2j)
np.clip(A,4,9)  #所有小于4的数都替换为4，所有大于9的数都替换为9
'''numpy索引'''
A = np.arange(3,15)
A[3]
A1 = np.arange(3,15).reshape([3,4])
A1[2]  #第二行
A1[1][1]
A1[1,1]
A1[2,:]
A1[:,1]
A1[1,1:3]
'''打印每行的数据'''
for row in A1:
    print(row)
'''打印每列的数据'''
for col in np.transpose(A1):
    print(col)
'''将矩阵转化为一行序列'''
for item in A1.flat:
    print(item)

'''numpy 两个array合并'''
'''以下三个函数都可以将两个或多个array合并起来'''
np.vstack
np.hstack
np.concatenate

A = np.array([1,1,1])
B = np.array([2,2,2])
C = np.vstack([A,B]);C   #上下合并
D = np.hstack([A,B]);D   #左右合并
#将A变为列向量
A = np.array([1,1,1])  #A.T不能转化为1个列向量
A[:,np.newaxis]
A[np.newaxis,:]        #变为矩阵的shape
A[:,np.newaxis].shape

E = np.hstack([A[:,np.newaxis],B[:,np.newaxis]])

'''concatenate'''
A1 = np.array([1,1,1])[:,np.newaxis]
B1 = np.array([2,2,2])[:,np.newaxis]
F = np.concatenate([A1,B1,B1,A1],axis = 0);F
F1 = np.concatenate([A1,B1,B1,A1],axis = 1);F1



''''''numpy array 分割''''''
a1 = np.arange(12).reshape([3,4])
np.split(a1,2,axis = 1)   #按照列分割成两个array
np.split(a1,3,axis = 0)   #按照行分割成三个array
'''不等量的分割'''
np.array_split(a1,3,axis = 1)   #按照列分割成两个array
np.vsplit(a1,3)
np.hsplit(a1,2)

'''numpy array 的copy 和 deepcopy'''
a = np.arange(4)
b =a
c =a
d =b
a[0] = -1
a

b is a  #返回True，存在和列表一样的赋值原理
========想要赋值的话用copy
b = a.copy()  #这就是deepcopy
a[3] = 44
b is a
#################pandas###############
import pandas as pd
import numpy as np
s =pd.Series([1,2,3,np.nan,44])
#以天为间隔
dates = pd.date_range('20180715',freq='D',periods = 6);dates
#以月为间隔
month = pd.date_range('20180715',freq='M',periods = 6)


'''DataFrame'''
df = pd.DataFrame(np.random.randn(6,4),index = dates,columns = ['a','b','c','d'])
df1 = pd.DataFrame(np.arange(12).reshape(3,4))

1.定义DataFrame
df2 = pd.DataFrame({'A':1.,
                    'B':pd.Timestamp('20180715'),
                    'C':pd.Series(1,index = list(range(4)),dtype = np.float),
                    'D':np.array([3] * 4 ,dtype = np.int),
                    'E':pd.Categorical(['a','b','a','b']),
                    'F':'foo'})
df2.dtypes
df2.index
df2.columns
df2.describe()
df2.values   #每行的值
df2.T
df2.sort_index(axis = 1,ascending = False)
df2.sort_values(by = 'E')




dates = pd.date_range('20180715',periods = 6)
df3 = pd.DataFrame(np.arange(24).reshape([6,4]),index = dates,columns = ['A','B','C','D'])
#列索引
df3['A']
df3.A
#行取值
df3[0:3]

#loc标签索引
df3.loc['20180715',['A','B']]
#iloc位置索引
df3.iloc[0,2]
#混合索引
df3.ix[0:2,['A','B']]

#多条件筛选
df3[(df3.A > 8) & (df3.B >13)]
df3[(df3.A > 8) | (df3.B >13)]


改变某个值
import pandas as pd
import numpy as np
dates = pd.date_range('20180715',periods = 6)
df3 = pd.DataFrame(np.arange(24).reshape([6,4]),index = dates,columns = ['A','B','C','D'])
#以下两中方式很不一样
df3[df3.A>4] = 'A>4'
df3.A[df3.A>4] = 'A>4'
#定义一个空列
df3['E'] = np.nan
df3.loc['20180718','B']  =2222
df3['E'] = pd.Series([2,2,3,4,5,6])   #这种赋值方法不行，会赋值为np.nan
df3['E'] = pd.Series([2,2,3,4,5,6],index = dates)   #这种赋值方法正确,必须加index
df3['E'] = [2,2,3,4,5,6]


'''如何处理缺失值'''
dates = pd.date_range('20180715',periods = 6)
df = pd.DataFrame(np.arange(24).reshape([6,4]),index = dates,columns = ['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan

#按照行删除
df.dropna(axis = 0,how = 'any')  #how = ['any','all']

df.fillna(value = '?')

df.isnull()
df.isna()
#数据太多时，我需要看看是或有缺失值产生

np.any(df.isnull()) == True         #返回True有缺失值,否则没有

'''pandas 导入导出数据'''
data = pd.read_excel('C:\\Users\\Administrator\\Desktop\\aaa.xlsx')
data.to_excel()
data.to_csv()
data.shape
#保存
data.to_pickle('aaa.pkl')   #文件后缀以什么都可以
#读取
pd.read_pickle('aaa.pickle')

'''合并多个dataframe'''
'''原理是按照相同列名或者index名进行合并处理'''

#concatenatin
df1 = pd.DataFrame(np.ones([3,4]) *0,columns =['a','b','c','d'])
df2 = pd.DataFrame(np.ones([3,4]) *1,columns =['a','b','c','d'])
df3 = pd.DataFrame(np.ones([3,4]) *2,columns =['a','b','c','d'])
1.上下合并
res1 = pd.concat([df1,df2,df3],axis = 0,ignore_index = True)
res2 = pd.concat([df1,df2,df3],axis = 0,ignore_index = False)   #index 不同

res1 = pd.concat([df1,df2,df3],axis = 1)

2.join ['inner','outer']
df4 = pd.DataFrame(np.ones([3,4]) *0,columns =['a','b','c','d'],index = [1,2,3])
df5 = pd.DataFrame(np.ones([3,4]) *1,columns =['b','c','d','e'],index = [2,3,4])

res = pd.concat([df4,df5],join ='outer')
res1 = pd.concat([df4,df5],join ='inner',ignore_index = True)

3.join_axes
df1 = pd.DataFrame(np.ones([3,4]) *0,columns =['a','b','c','d'],index = [1,2,3])
df2 = pd.DataFrame(np.ones([3,4]) *1,columns =['b','c','d','e'],index = [2,3,4])
#按照df1的index进行左右合并
res = pd.concat([df1,df2],axis = 1 ,join_axes = [df1.index])

4.append
df1 = pd.DataFrame(np.ones([3,4]) *0,columns =['a','b','c','d'],index = [1,2,3])
df2 = pd.DataFrame(np.ones([3,4]) *1,columns =['b','c','d','e'],index = [2,3,4])
df3 = pd.DataFrame(np.ones([3,4]) *2,columns =['b','c','d','e'],index = [2,3,4])
res = df1.append(df2,ignore_index = True)
res = df1.append([df2,df3],ignore_index = True)

df1 = pd.DataFrame(np.ones([3,4]) *0,columns =['a','b','c','d'],index = [1,2,3])
s1 = pd.Series([1,2,3,4])
res = df1.append(s1,ignore_index = True)
5.merge
import pandas as pd
import numpy as np
一个共同字段
left = pd.DataFrame({'key':['K0','K1','K2','K3'],
                    'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                    'A':['C0','C1','C2','C3'],
                    'B':['D0','D1','D2','D3']})
res = pd.merge(left,right,on ='key',how = 'left')
两个共同字段
left = pd.DataFrame({'key2':['K0','K1','K0','K1'],
                     'key1':['K0','K0','K1','K2'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key2':['K0','K0','K0','K0'],
                      'key1':['K0','K1','K1','K2'],
                      'A':['C0','C1','C2','C3'],
                      'B':['D0','D1','D2','D3']})
#how  on
res = pd.merge(left,right,on =['key1','key2'],how = 'left')
res = pd.merge(left,right,on =['key1','key2'],how = 'inner')
res = pd.merge(left,right,on =['key1','key2'],how = 'right')
res = pd.merge(left,right,on =['key1','key2'],how = 'outer')
# indicator显示那个表有
res = pd.merge(left,right,on =['key1','key2'],how = 'outer',indicator = True)
# merge by index 
left = pd.DataFrame({'A':['A0','A1','A2'],
                     'B':['B0','B1','B2']},
                     index = ['K0','K1','K2'])
right = pd.DataFrame({'A':['C0','C1','C2'],
                      'B':['D0','D1','D2']},
                      index = ['K0','K2','K3'])
res = pd.merge(left,right,left_index = True,right_index = True,how = 'outer')

'''apply方法进行某种计算或映射（对于DataFrame有效）'''
1.通过apply方法将函数应用到每行或每列上，注意指定轴的方向，默认axis = 0
df = pd.DataFrame(np.random.randn(5,4)-1)
np.abs(df)
print(df.apply(lambda x:x.max()))
print(df.apply(lambda x:x.max(),axis =1))  #每行最大值

def f(x):
    return x.min()
print(df.apply(f))


2.通过applymap 方法将函数应用到每个数据上
f2 = lambda x:'%.2f' % x
print(df.applymap(f2))

'''Series上的map函数'''
data = pd.DataFrame({'data1':np.random.randint(1,10,5,dtype = np.int),
                     'B':['a','b','a','b','c'],
                     'C':['f','m','f','m','f'],
                     'data2':np.random.normal(0,1,5)})
data['B'].map(str.upper)
data['data2'].map(lambda x:'%.2f' %x)

'''更改index和columns的名字'''
data = pd.DataFrame({'data1':np.random.randint(1,10,5,dtype = np.int),
                     'B':['a','b','a','b','c'],
                     'C':['f','m','f','m','f'],
                     'data2':np.random.normal(0,1,5)})
data.rename(columns = {'C':'gender'})
data.rename(index = {0:'first'})
'''数据的离散化'''
ages = [20,22,25,27,21,23,37,31,61,45,41,32]
bins = [18,25,35,60,100]
group_names = ['Youth','YoungAdult','middleAged','Senior']
cats = pd.cut(ages,bins,labels =group_names)  #默认为左开右闭区间
cats.value_counts()



'''排序'''
1.索引排序
df = pd.DataFrame(np.random.randn(5,4)-1)
df.sort_index(ascending = False)
2.按值排序
df.sort_values(by = [0,1],ascending = True)     #按0这一列排

'''随机重排序和随机采样'''
df = pd.DataFrame(np.arange(20).reshape(5,4))
sample = np.random.permutation(df.shape[0])
#以下两种方法等价
df.iloc[sample]
df.take(sample)
'''求数据框的行数'''
len(df)
df.shape[0]

'''数据分组与聚合'''
层级索引
在MultiIndex对象中选取子集
    外层选取 df['一级index']
    内层选取 df[:,'二级index']

df = pd.Series(np.random.randn(12),
                  index = [['a','a','a','b','b','b','c','c','c','d','d','d'],
                           [0,1,2,0,1,2,0,1,2,0,1,2]])
type(df.index)   #返回pandas.core.indexes.multi.MultiIndex
df.index
'''选取子集'''
'''外层选取'''
df['c']
'''内层index选取'''
df[:,1]
'''内层columns选取'''

data = pd.DataFrame({'data1':np.random.randint(1,10,5,dtype = np.int),
                     'B':['a','b','a','b','c'],
                     'C':['f','m','f','m','f'],
                     'data2':np.random.normal(0,1,5)})
temp = data.groupby('B').agg(['sum','mean','count','max','min'])
temp = temp.reset_index()
temp['data1']['sum']


#分组groupby
Groupby对象：DataFrameGroupby,SeriesGroupby
size()返回每个分组的元素个数
按列分组
    obj.groupby(['列名'])
按多个列分组
    obj.groupby(['列名1','列名2'])
按自定义的key分组
    obj.groupby(self_def_key)
    自定义的key可为列表或多层列表
unstack 可以将多层索引的结果转化为单层的dataframe

1.分组统计
df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})
df.groupby(['key1'])['data1'].min()
df.groupby(['key1'])['data1'].count()   #求行数
df.groupby(['key1']).size()             #求行数
df.groupby(['key1']).mean()             #求行数
grouped1 = df.groupby(['key1'])
grouped2 = df.groupby(['key1'])['data1']

2.对groupby对象迭代
grouped1 = df.groupby(['key1'])
grouped2 = df.groupby(['key1'])['data1']

for group_name,group_data in grouped1:
    print(group_name)
    print(group_data)

for group_name,group_data in grouped2:
    print(group_name)
    print(group_data)
3.groupby对象转化为list
list(grouped1)[0]
dict(list(grouped1))['a']
dict(list(grouped1))['b']
4.函数进行分组
5.字典进行分组
6.索引级别进行分组



7.聚合
内置的聚合函数
'''注意聚合函数运算返回的是Series格式的数据，可以用unstack的方法转化为DataFrame的格式'''
sum(),mean(),min(),max(),count(),size(),describe()
可自定义函数,传入agg方法中
grouped.agg(func)
func的参数为groupby索引对应的记录

print(df.groupby(['key1']).sum())      #非NA的和
print(df.groupby(['key1']).mean())     #非NA的平均值
print(df.groupby(['key1']).min())      #非NA的最小值
print(df.groupby(['key1']).max())      #非NA的最大值
print(df.groupby(['key1']).count())    #非NA的行数
print(df.groupby(['key1']).median())   #非NA的中位数
print(df.groupby(['key1']).size())     #非NA的最小值
print(df.groupby(['key1']).describe()) #非NA的最小值


a = df.groupby(['key1']).sum()
a = a.reset_index()

自定义聚合函数
def f(df):
    return df.max() - df.min()
df.groupby(['key1']).agg(f)

多个聚合函数
a = df.groupby(['key1']).agg(['max','min',f,'mean','sum'])


聚合运算改变了原始数据的shape
如何保持原始数据的shape？
    使用merge的外连接，比较复杂
    transform
transform的计算结果和原始数据shape保持一致
   如：grouped.transform(np.mean)
   也可以传入自定义函数

grouped1 = df.groupby(['key1'])
#把计算的分组sum直接赋值给原始数据表
grouped1.transform(np.sum).add_prefix('sum_')

'''对不同的列应用不同的函数'''
grouped.agg({'列名1':函数1,'列名2':函数2})
'''数据的合并'''
#np数组的合并
np.concatenate()
#用key的方式连接两个数据框
pd.merge()
#一个对象的join是进行index的连接数据用的
object.join()
#数据框的合并，axis =1 是按照index连接，axis =0 是按照列名曲连接
#默认为outer连接，将两个数据框进行列名合并
pd.concat()
#np的竖直连接操作
np.vstack()
#np的多维数组的
np.stack()
#横向连接
np.hstack()

'''数据的重构也有melt方法，相当与R语言中的melt方法'''
1.DataFrame对象的stack方法,将列索引旋转为行索引，完成层级索引
'''stack方法将DataFrame转化为Series'''
import numpy as np
import pandas as pd
df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})

a = df.stack();a
2.unstack
a = df.stack()
type(a)                       #返回pandas.core.series.Series
b = a.unstack()
type(b)                       #返回pandas.core.frame.DataFrame
'''unstack方法将Series转化为DataFrame'''
3.数据宽转长
df_chang = df.melt(id_vars = ['key1','key2'],
        value_vars = ['data1','data2'],   # 这个是将那几列进行转化
        var_name = '我是变量名',value_name = '我是变量的值')  #对转化的列进行列命名
4.数据长转宽(pivot_table)
df_chang.pivot_table(index = ['key1','key2'],columns = ['我是变量名'],values = ['我是变量的值'])
pd.pivot_table(df_chang,index = ['key1','key2'],columns = ['我是变量名'],values = ['我是变量的值'])
'''数据转换'''
#删除重复行之后的数据
df.drop_duplicates('key1')
df[df.duplicated('key1') == False]
df.replace('a','A')

'''长数据转化为短数据'''
data = pd.DataFrame({'data1':np.random.randint(1,10,5,dtype = np.int),
                     'B':['a','b','a','b','c'],
                     'C':['f','m','f','m','f'],
                     'data2':np.random.normal(0,1,5)})
data.pivot('data1','B','data2')


#################matplotlib###############
import matplotlib.pyplot as plt
data = pd.DataFrame(np.random.randn(1000,4),index = np.arange(1000))
data = data.cumsum()
data.plot()
plt.show()
###########################

####第一幅图
#竖直的bar
np.random.seed(2018)
plt.figure(1,figsize = [14,8])
x1 = np.linspace(-1,1,10)
y1 = x1 ** 2 + 1
y2 = x1 ** 3 + 1
x_data = np.arange(0,10,dtype = np.int)
y_data = np.random.uniform(0.1,0.7,size = 10)
plt.subplot(2,2,1)
plt.bar(x_data,y_data,fc = 'red',ec = 'white')
plt.bar(x_data,-y_data,fc = 'green',ec = 'white')
plt.xticks([])
plt.yticks([])
for x,y in zip(x_data,y_data):
    plt.text(x,y-0.08,'%.2f' %y,ha = 'center',color = 'white')
for x,y in zip(x_data,y_data):
    plt.text(x,-y+0.02,'%.2f' %y,ha = 'center',color = 'white')
#水平的bar
plt.subplot(2,2,2)
plt.barh(x_data,y_data,fc = 'green',ec = 'white')
plt.subplot(2,2,3)
plt.plot(x1,y1,color = 'green',linestyle = '-',linewidth = 3)
plt.subplot(2,2,4)
plt.plot(x1,y2,color = 'red',linestyle = '--',linewidth = 3)
plt.show()

####第二幅图
plt.figure(2)
plt.subplot(2,1,1)
plt.plot(x1,y1,color = 'red',linewidth = 3,linestyle = '--',label = '1')
plt.xlabel('i am xlabel')
plt.title('i am title')
plt.scatter([0,1],[0,2])
plt.legend(loc = 'best')
plt.subplot(2,3,4)
plt.plot(x1,y2)
plt.scatter([0,1],[0,2])
plt.subplot(2,3,5)
plt.scatter([0,1],[0,2])
plt.subplot(2,3,6)
plt.scatter(x1,y2,color = 'orange')
plt.show()


zip函数
a = [1,2,3]
b = [2,3,4]
zip(a,b)
list(zip(a,b))
for i,j in zip(a,b):
    print(i/2,j*2)

'''第二种方法'''
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
#一张画布上有多条线
ax1.plot(np.random.randn(1000).cumsum(),'r',label = 'line1')
ax1.plot(np.random.randn(1000).cumsum(),'g',label = 'line2')
ax1.plot(np.random.randn(1000).cumsum(),'b',label = 'line3')
#ax1.set_xticks([])    #删除xticks
ax1.grid()
ax1.legend(loc = 'best')
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax3 = fig.add_subplot(2,2,3)
plt.plot(np.random.rand(50).cumsum(),'k--')
ax1.hist(np.random.rand(100),bins = 20 ,color = '#ffff99',alpha = 0.3,ec = 'black')
ax2.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))
ax2.set_xlabel('x')
ax1.set_title('x')
fig.show()

'''第三种方法'''
fig,ax = plt.subplots(2,2)
ax[0,0].hist(np.random.rand(500),bins = 50,color = 'k',alpha = 0.5)
ax[0,0].set_xlim(0,1)
ax[0,0].set_title('a')
ax[0,1].bar(np.arange(10),np.random.rand(10))
ax[0,1].plot(np.arange(10),np.random.rand(10))
ax[1,0].barh(np.arange(10),np.random.rand(10))
ax[1,1].scatter(np.arange(10),np.random.rand(10),color = 'red')
fig.show()
fig.savefig('C:\\Users\\Administrator\\desktop\\1.png')
'''
plt.plot()函数的一些属性：color,marker,linestyle,linewidth,markersize,lable(为plt.legend)
'''




#randn正态分布
plt.plot(np.random.randn(30).cumsum(),'ko--')
plt.plot(np.random.randn(30).cumsum(),color = 'r',marker = 'o',linestyle = 'dashed',label = 'line1')
plt.legend(loc = 'best')






####################datetime#################
'''219页 正则表达式'''
import re
re.split(pattern,string)   #字符串拆分
re.match(pattern,string)   #字符串匹配（只从开头匹配模式）,匹配到返回匹配内容，否则返回None
re.search(pattern,string)  #任何位置开始匹配
re.findall(pattern,string) #查找,匹配到返回匹配内容的list，否则返回空列表
re.sub(pattern,repl,string)#替换

总结：能用search就不要用match

re.split(r'\s+', 'a b   c')
用()表示的就是要提取的分组（Group）。比如：
^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：
>>> m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')  #match有group的方法，findall没有
>>> m.group(0)   # group(0)永远是原始字符串
'010-12345'
>>> m.group(1)  #group(1)、group(2)……表示第1、2、……个子串
'010'
>>> m.group(2)
'12345'
\   转义符，对没有任何特殊含义的字母进行转义，使之具备某种特殊含义（包括转义它自己）
^   匹配以目标模式开头的字符串
$   匹配以目标模式结尾的字符串
*   0或多次
？  0或1次
+   1或多次
.   匹配除\n之外的任何字串
[]  匹配一个组合
x|y 匹配x或y
\d  匹配数字
\w  匹配包括下划线的任何单词字符等价于[A-Za-z0-9_]
[\u4e00-\u9fa5]  #匹配中文字符串
re.findall('[\u4e00-\u9fa5]+','我是abc123')
(P|p)ython可以匹配'Python'或者'python'
如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
>>> import re
# 编译:
>>> re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
>>> re_telephone.match('010-12345').groups()
('010', '12345')
>>> re_telephone.match('010-8086').groups()
('010', '8086')


Python的字符串本身也用\转义，所以要特别注意：
s = 'ABC\\-001' # Python的字符串
# 对应的正则表达式字符串变成：
# 'ABC\-001'
因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：
s = r'ABC\-001' # Python的字符串
# 对应的正则表达式字符串不变：
# 'ABC\-001'

import re
s1='hjxxHelloxxrynxxPythonxxplk'
f1=re.findall('xx.*xx',s1)
print(f1)
f2=re.findall('xx.*?xx',s1)
print(f2)
f3=re.findall('xx(.*)xx',s1)
print(f3)
f4=re.findall('xx(.*?)xx',s1)
print(f4)
s2='''hjxxHello
xxrynxxPythonxxplk'''
g1=re.findall('xx(.*?)xx',s2)
print(g1)
g2=re.findall('xx(.*?)xx',s2,re.S)  #re.S忽略换行
print(g2)
输出为：
['xxHelloxxrynxxPythonxx']
['xxHelloxx', 'xxPythonxx']
['HelloxxrynxxPython']
['Hello', 'Python']
['ryn']
['Hello\n', 'Python']
re.findall('xx(.*?)xx',s2,re.S)[0].strip()
'Hello'

'''276页数据框分组计数时的问题'''
'''a is equal to b'''
import numpy as np
import pandas as pd
data = pd.DataFrame({'data1':np.random.randint(1,10,5,dtype = np.int),
                     'B':['a','b','a','b','c'],
                     'C':['f','m','m','m','f'],
                     'smoker':['yes','yes','no','no','yes'],
                     'data2':np.random.normal(0,1,5)})
a = data.groupby('B').mean().reset_index()

b = data.groupby('B',as_index = False).mean()

'''交叉表相当于R语言的table'''
pd.crosstab(data.B,data.C)
pd.crosstab([data.B,data.C],data.smoker,margins=True)



'''DataFrame条件赋值,pandas.core.series.Series有属性str
其中str.find方法找到返回 所匹配的文本开始位置，否则返回-1'''
data = {'city': ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Hangzhou', 'Chongqing'],
        'year': [2016,2016,2015,2017,2016, 2016],
        'population': [2100, 2300, 1000, 700, 500, 500]}
frame = pd.DataFrame(data, columns = ['year', 'city', 'population', 'debt','panduan'])
# 使用apply函数, 如果city字段包含'ing'关键词，则'判断'这一列赋值为1,否则为0
frame['panduan'] = frame.city.apply(lambda x: 1 if 'ing' in x else 0)
print(frame)

frame.ix[frame.population >= 1000,'debt'] = '>=1000'
frame.ix[frame.population < 1000,'debt'] = '<1000'
#文本匹配到ing
frame.ix[frame['city'].str.contains('ing'),'panduan']  =  '有ing'
#文本匹配不到ing
frame.ix[frame['city'].str.find('ing') == -1,'panduan']  =  '无ing'
#isin 等于多个值时使用
frame.ix[frame.city.isin(['Guangzhou']),'panduan']  =  'Guangzhou'
#使用正则表达式进行模糊匹配,*匹配0或无限次,?匹配0或1次
df_obj[df_obj['套餐'].str.contains(r'.*?语音CDMA.*')]



'''datetime库'''
from datetime import datetime

now = datetime.now()
'-'.join(str(now.year) + str(now.month) + str(now.day))


'''将字符串转化为时间格式'''
'方法一'
s = '20180715'
datetime.strptime(s,'%Y%m%d')
s = '07152018'
datetime.strptime(s,'%m%d%Y')

s = ['07152018','07142018']
[datetime.strptime(x,'%m%d%Y') for x in s]



'方法二(这种方法可以解析所有人类能够理解的日期格式--返回时间格式)'
from dateutil.parser import parse
print(parse('20180715122312').year)
print(parse('20180715122312').month)
print(parse('20180715122312').day)
print(parse('20180715122312').hour)
print(parse('20180715122312').minute)
print(parse('20180715122312').second)


'方法三用pd.to_datetime()函数将字符串转化为datetime'
data = pd.DataFrame({'data1':np.random.randint(1,10,5,dtype = np.int),
                     'B':['a','b','a','b','c'],
                     'C':['f','m','m','m','f'],
                     'smoker':['yes','yes','no','no','yes'],
                     'date':['20180215122345','20180715122356','20180716125623','20180717142356',
                             '20180718161223'],
                     'date1':pd.date_range('20180722122315',periods = 5)})
data.date = pd.to_datetime(data.date)
data.date1 = pd.to_datetime(data.date1)

data['timeduan'] = data.date1 - data.date

datetime.for x in data.timeduan

from dateutil.parser import parse
type(parse('20181215'))   #返回datetime.datetime格式

'''求时间差'''
type(parse('20181215122356') - parse('20181115102356'))  #返回timedelta
from datetime import timedelta



'''用pd.date_range 定义时间序列'''
pd.date_range('20180715122356',periods = 10,freq = '1h30s')
pd.date_range('20180715122356',periods = 10,freq = '30min')
pd.date_range('20180715122356',periods = 10,freq = '30s')




'''python操作mysql数据库'''

'''执行INSERT等操作后要调用commit()提交事务'''
1.读取
import pandas as pd
import numpy as np
import pymysql
conn = pymysql.connect(host = '127.0.0.1',port = 3307,user = 'root',passwd = '826828',db = 'mysql')
a = pd.read_sql('select * from db',conn)
conn.close()
2.插入数据（必须提交）
import pandas as pd
import pymysql
db = pymysql.connect(host = '127.0.0.1',port = 3307,user = 'root',passwd = '826828',db = 'sakila')
cursor = db.cursor()
sql = '''insert into category(category_id,name,last_update) values(17,'houkai',now())'''
cursor.execute(sql)
db.commit()  #必须要提交菜可以
db.close()
3.建表
db = pymysql.connect(host = '127.0.0.1',port = 3307,user = 'root',passwd = '826828',db = 'sakila')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)
db.close()
3.更新表
db = pymysql.connect(host = '127.0.0.1',port = 3307,user = 'root',passwd = '826828',db = 'sakila')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)
db.close()


三个模块
import queue
import threading
import time



#数据框的实际操作
data = pd.DataFrame({'国家':['中国','中国','中国','韩国','韩国','韩国','美国','美国','美国'],
                     '地区':['西安','北京','上海','首尔','大田','釜山','纽约','洛杉矶','芝加哥'],
                     'GDP':[10,10,40,26,56,42,16,56,24]})
a = data.groupby('国家', as_index = False)['GDP'].mean()
b = pd.merge(data,a,how = 'left',on='国家',suffixes = ('','_mean'))
b['subtract'] = b.GDP - b.GDP_mean
data = data.sort_values(['国家','GDP'],ascending = False)
data.index = range(data.shape[0])   #reindex会继续排序，不可用
#dense 是相同GDP有相同排名，first是对于相同的GDP是谁排在前面谁排名靠前
data['ranking'] = data.groupby('国家')['GDP'].rank(ascending=False,method = 'first').astype(np.int)
data['cha'] = 1
data.ix[data.ranking==1,'cha'] = np.nan
#标类
for index,name in zip(range(1,len(set(data.国家))+1),set(data.国家)):
    data.ix[data.国家 == name,'Type'] = index

#组内相减得到GDP的差
for index,dataframe in data.groupby('国家'):
    for i in dataframe.index[:-1]:
        data.ix[i+1,'cha'] = data.ix[i,'GDP'] - data.ix[i+1,'GDP']

data.ix[data.cha.isna(),'cha'] = data['cha'].fillna(np.nan)



###### join的用法
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
                   'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                   'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )','12. Air France', '"Swiss Air"']})
df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)
print(type(temp))
temp = df.From_To.str.split('_', expand=True)
temp.columns = ['From', 'To']
#以下两种结果相等
#1
pd.concat([df,temp],axis=1)
#2
df = df.drop('From_To', axis=1)
df = df.join(temp)
print(df)

###### 数据清洗
88. 缺失值拟合
在FilghtNumber中有数值缺失，其中数值为按 10 增长，补充相应的缺省值使得数据完整，并让数据为 int 类型。
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
                               'Budapest_PaRis', 'Brussels_londOn'],
                   'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                   'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
                               '12. Air France', '"Swiss Air"']})
df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)
df
89. 数据列拆分
其中From_to应该为两独立的两列From和To，将From_to依照_拆分为独立两列建立为一个新表。
90. 字符标准化
其中注意到地点的名字都不规范（如：londON应该为London）需要对数据进行标准化处理。
temp['From'] = temp['From'].str.capitalize()
temp['To'] = temp['To'].str.capitalize()
91. 删除坏数据加入整理好的数据
将最开始的From_to列删除，加入整理好的From和to列。
df = df.drop('From_To', axis=1)
df = df.join(temp)
print(df)
92. 去除多余字符¶
如同 airline 列中许多数据有许多其他字符，会对后期的数据分析有较大影响，需要对这类数据进行修正。
# str.extract()
# 先介绍str.extract()，可用正则从字符数据中抽取匹配的数据，只返回第一个匹配的数据。
df['Airline'] = df['Airline'].str.extract('([a-zA-Z\s]+)', expand=False).str.strip()
df
93. 格式规范
在 `RecentDelays` 中记录的方式为列表类型，由于其长度不一，这会为后期数据分析造成很大麻烦。这里将 `RecentDelays` 的列表拆开，取出列表中的相同位置元素作为一列，若为空值即用 `NaN` 代替。
delays = df['RecentDelays'].apply(pd.Series)
delays
delays.columns = ['delay_{}'.format(n)
                  for n in range(1, len(delays.columns)+1)]

df = df.drop('RecentDelays', axis=1).join(delays)
df

###### 数据预处理
94. 信息区间划分
班级一部分同学的数学成绩表，如下图所示

df=pd.DataFrame({'name':['Alice','Bob','Candy','Dany','Ella','Frank','Grace','Jenny'],'grades':[58,83,79,65,93,45,61,88]})
但我们更加关心的是该同学是否及格，将该数学成绩按照是否>60来进行划分。
df = pd.DataFrame({'name': ['Alice', 'Bob', 'Candy', 'Dany', 'Ella','Frank', 'Grace', 'Jenny'],
                   'grades': [58, 83, 79, 65, 93, 45, 61, 88]})
def choice(x):
    if x > 60:
        return 1
    else:
        return 0
df.grades = df['grades'].map(lambda x: choice(x))
# df.grades = pd.Series(map(lambda x: choice(x), df.grades))
95. 数据去重
一个列为A的 DataFrame 数据，如下图所示
df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
尝试将 A 列中连续重复的数据清除。
df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
df.loc[df['A'].shift() != df['A']]

df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7],
                  'b':[2,3,4,5,6,7,8,9,8,7,6]})
# df.loc[df['A'].shift() != df['A']]
df = df.drop_duplicates('A')
df
96. 数据归一化
有时候，DataFrame 中不同列之间的数据差距太大，需要对其进行归一化处理。
其中，Max-Min 归一化是简单而常见的一种方式，公式如下:

def normalization(df):
    numerator = df.sub(df.min())
    denominator = (df.max()).sub(df.min())
    Y = numerator.div(denominator)
    return Y

df = pd.DataFrame(np.random.random(size=(5, 3)))
print(df)
normalization(df)


'''
线程 
一个进程中可以有多个线程
任何进程默认会启动一个线程，称为主线程，主线程可以启动新的子线程

'''
import threading
import time


def run(str):
    print('子线程（%s）启动' % threading.current_thread().name)

    # 实现线程的功能
    time.sleep(2)
    print('打印 %s ' % str)
    time.sleep(2)
    print(a)

    print('子线程（%s）结束' % (threading.current_thread().name))

if __name__ == '__main__':
    print('主线程（%s）启动' % threading.current_thread().name)

    # 创建子线程
    t = threading.Thread(target=run, args=('hello world'), name='rootThread')
    t.start()

    # 等待线程结束
    t.join()


    print('主线程（%s）结束' % threading.current_thread().name)


# logging库的用法
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  #设置为info级别以上的信息
logger1 = logging.getLogger(__name__)
logger1.info('This is a log info')
logger1.debug('Debugging')
logger1.warning('Warning exists')
logger1.info('Finish')

# 接下来我们首先来全面了解一下 basicConfig 的参数都有哪些：
# filename：即日志输出的文件名，如果指定了这个信息之后，实际上会启用 FileHandler，而不再是 StreamHandler，这样日志信息便会输出到文件中了。
# filemode：这个是指定日志文件的写入方式，有两种形式，一种是 w，一种是 a，分别代表清除后写入和追加写入。
# format：指定日志信息的输出格式，其部分参数如下所示：
    # %(levelno)s：打印日志级别的数值。
    # %(levelname)s：打印日志级别的名称。
    # %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]。
    # %(filename)s：打印当前执行程序名。
    # %(funcName)s：打印日志的当前函数。
    # %(lineno)d：打印日志的当前行号。
    # %(asctime)s：打印日志的时间。
    # %(thread)d：打印线程ID。
    # %(threadName)s：打印线程名称。
    # %(process)d：打印进程ID。
    # %(processName)s：打印线程名称。
    # %(module)s：打印模块名称。
    # %(message)s：打印日志信息。
# datefmt：指定时间的输出格式。
# style：如果 format 参数指定了，这个参数就可以指定格式化时的占位符风格，如 %、{、$ 等。
# level：指定日志输出的类别，程序会输出大于等于此级别的信息。
# stream：在没有指定 filename 的时候会默认使用 StreamHandler，这时 stream 可以指定初始化的文件流。
# handlers：可以指定日志处理时所使用的 Handlers，必须是可迭代的。

import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='output.log',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)s - %(module)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info('info')
logger.debug('debug')
logger.warning('warning')
logger.error('error')


# 另外我们还可以使用其他的 Handler 进行日志的输出，logging 模块提供的 Handler 有：
#
# StreamHandler：logging.StreamHandler；日志输出到流，可以是 sys.stderr，sys.stdout 或者文件。
# FileHandler：logging.FileHandler；日志输出到文件。
# BaseRotatingHandler：logging.handlers.BaseRotatingHandler；基本的日志回滚方式。
# RotatingHandler：logging.handlers.RotatingHandler；日志回滚方式，支持日志文件最大数量和日志文件回滚。
# TimeRotatingHandler：logging.handlers.TimeRotatingHandler；日志回滚方式，在一定时间区域内回滚日志文件。
# SocketHandler：logging.handlers.SocketHandler；远程输出日志到TCP/IP sockets。
# DatagramHandler：logging.handlers.DatagramHandler；远程输出日志到UDP sockets。
# SMTPHandler：logging.handlers.SMTPHandler；远程输出日志到邮件地址。
# SysLogHandler：logging.handlers.SysLogHandler；日志输出到syslog。
# NTEventLogHandler：logging.handlers.NTEventLogHandler；远程输出日志到Windows NT/2000/XP的事件日志。
# MemoryHandler：logging.handlers.MemoryHandler；日志输出到内存中的指定buffer。
# HTTPHandler：logging.handlers.HTTPHandler；通过”GET”或者”POST”远程输出到HTTP服务器。


# 下面我们使用三个 Handler 来实现日志同时输出到控制台、文件、HTTP 服务器：
import logging
from logging.handlers import HTTPHandler,SMTPHandler
import sys

logger = logging.getlogger()
logger.setLevel(level=logging.DEBUG)

# StreamHandler
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)

# FileHandler
file_handler = logging.FileHandler('output.log')
file_handler.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s -  %(name)s - %(levelname)s - %(message)s')
logger.addHandler(file_handler)

# HTTPHandler
http_handler = HTTPHandler(host='localhost:8001', url='log', method='POST')
logger.addHandler(http_handler)

email_handler = SMTPHandler(mailhost=('smtp.163.com', 25),
                            fromaddr='kaihou2018@163.com',
                            toaddrs='kai.hou@yhouse.com',
                            subject='python 脚本报错',
                            credentials=('kaihou2018@163.com', 'women419'))  # 这里的密码是授权码，不是登陆密码
email_handler.setLevel(logging.ERROR)
logger.addHandler(email_handler)

if __name__ == '__main__':
    try:
        a = 1/0
    except:
        logger.error('脚本出错', exc_info = True)  #exc_info 的值设置为True，邮件中出现正常的python报错信息，否则不显示
    # Log
    logger.info('This is a log info')
    logger.debug('Debugging')
    logger.warning('Warning exists')
    logger.info('Finish')


# 破解验证码
from captcha.image import ImageCaptcha
from PIL import Image

text = 'it is me'
image = ImageCaptcha()
captcha = image.generate(text)
captcha_image = Image.open(captcha)
captcha_image.show()



# 数据结构与算法
# 快速排序  nlogn
def partition(data, left, right):
    temp = data[left]
    while left != right:
        while left < right and temp <= data[right]:
            right -= 1
        data[left] = data[right]
        while left < right and temp >= data[left]:
            left += 1
        data[right] = data[left]
    data[left] = temp
    return  left

def quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid-1)
        quick_sort(data, mid+1, right)

import random

data = list(range(1000))
random.shuffle(data)
quick_sort(data, 0, len(data)-1)

##############################
# https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html#example-ensemble-plot-feature-transformation-py
import numpy as np
np.random.seed(10)

import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import (RandomTreesEmbedding, RandomForestClassifier,GradientBoostingClassifier)
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.pipeline import make_pipeline
from sklearn.metrics import auc

n_estimator = 10
X, y = make_classification(n_samples=80000)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

# It is important to train the ensemble of trees on a different subset
# of the training data than the linear regression model to avoid
# overfitting, in particular if the total number of leaves is
# similar to the number of training samples
X_train, X_train_lr, y_train, y_train_lr = train_test_split(X_train, y_train, test_size=0.5)

# Unsupervised transformation based on totally random trees
rt = RandomTreesEmbedding(max_depth=3, n_estimators=n_estimator,random_state=0)

rt_lm = LogisticRegression(solver='lbfgs', max_iter=1000)
pipeline = make_pipeline(rt, rt_lm)
pipeline.fit(X_train, y_train)
y_pred_rt = pipeline.predict_proba(X_test)[:, 1]
fpr_rt_lm, tpr_rt_lm, threshold = roc_curve(y_test, y_pred_rt)

# Supervised transformation based on random forests
rf = RandomForestClassifier(max_depth=3, n_estimators=n_estimator)
rf_enc = OneHotEncoder(categories='auto')
rf_lm = LogisticRegression(solver='lbfgs', max_iter=1000)
rf.fit(X_train, y_train)
rf_enc.fit(rf.apply(X_train))
rf_lm.fit(rf_enc.transform(rf.apply(X_train_lr)), y_train_lr)

y_pred_rf_lm = rf_lm.predict_proba(rf_enc.transform(rf.apply(X_test)))[:, 1]
fpr_rf_lm, tpr_rf_lm, _ = roc_curve(y_test, y_pred_rf_lm)

# Supervised transformation based on gradient boosted trees
grd = GradientBoostingClassifier(n_estimators=n_estimator)
grd_enc = OneHotEncoder(categories='auto')
grd_lm = LogisticRegression(solver='lbfgs', max_iter=1000)
grd.fit(X_train, y_train)
grd_enc.fit(grd.apply(X_train)[:, :, 0])
grd_lm.fit(grd_enc.transform(grd.apply(X_train_lr)[:, :, 0]), y_train_lr)

y_pred_grd_lm = grd_lm.predict_proba(
    grd_enc.transform(grd.apply(X_test)[:, :, 0]))[:, 1]
fpr_grd_lm, tpr_grd_lm, _ = roc_curve(y_test, y_pred_grd_lm)

# The gradient boosted model by itself
y_pred_grd = grd.predict_proba(X_test)[:, 1]
fpr_grd, tpr_grd, _ = roc_curve(y_test, y_pred_grd)

# The random forest model by itself
y_pred_rf = rf.predict_proba(X_test)[:, 1]
fpr_rf, tpr_rf, _ = roc_curve(y_test, y_pred_rf)

plt.figure(1)
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr_rt_lm, tpr_rt_lm, label='RT + LR')
plt.plot(fpr_rf, tpr_rf, label='RF')
plt.plot(fpr_rf_lm, tpr_rf_lm, label='RF + LR')
plt.plot(fpr_grd, tpr_grd, label='GBT')
plt.plot(fpr_grd_lm, tpr_grd_lm, label='GBT + LR')
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('ROC curve')
plt.legend(loc='best')
plt.show()

plt.figure(2)
plt.xlim(0, 0.2)
plt.ylim(0.8, 1)
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr_rt_lm, tpr_rt_lm, label='RT + LR')
plt.plot(fpr_rf, tpr_rf, label='RF')
plt.plot(fpr_rf_lm, tpr_rf_lm, label='RF + LR')
plt.plot(fpr_grd, tpr_grd, label='GBT')
plt.plot(fpr_grd_lm, tpr_grd_lm, label='GBT + LR')
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('ROC curve (zoomed in at top left)')
plt.legend(loc='best')
plt.show()


import click
@click.command()
@click.option('--count', default = 1, help = 'Numbor of gretting')
@click.option('--name', nargs=2, prompt = 'your name', help = 'the person to greet.', default = '')

# @click.option('-m','--mail_to',default = '',help = 'mail to person email')
# parameters introdutions
# Click supports two types of parameters for scripts: options and arguments.
# parameter type
# If no type is provided, the type of the default value is used.
# Multi Value Options

#It automatically generates nicely formatted help pages:
# prompt varible can advocate youself you name
# default varible set per default value
# help varible can print its help document
# --name nargs=2 means name attribute have two varible
def hello(count,name):
    '''simple program that greets name for a total of count times'''
    for i in range(int(count)):
        click.echo('name1  is %s,name2 is %s' %  name)

if __name__ == '__main__':
    hello()

# we havo to run in the command line,for example:
# python env_click.py --help
# python env_click.py --count=3 --name='houkai'
# python env_click.py --count=3  after anter input you name via clue


