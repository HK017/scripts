# os库
import os  # os模块提供了不少与操作系统相关联的函数
os.sep 可以取代操作系统特定的路径分隔符。windows下为 '\\'
os.name 字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux / Unix用户，它是 'posix'
os.getcwd() 函数得到当前工作目录，即当前Python脚本工作的目录路径
os.getenv() 获取一个环境变量，如果没有返回none
os.putenv(key, value) 设置一个环境变量值
os.listdir(path) 返回指定目录下的所有文件和目录名
os.remove(path) 函数用来删除一个文件
os.system(command) 函数用来运行shell命令
os.linesep 字符串给出当前平台使用的行终止符。例如，Windows使用 '\r\n'，Linux使用 '\n' 而Mac使用 '\r'
os.path.split(path)  函数返回一个路径的目录名和文件名
os.path.isfile() 和os.path.isdir()函数分别检验给出的路径是一个文件还是目录
os.path.exists() 函数用来检验给出的路径是否真地存在
os.curdir  返回当前目录('.')
os.mkdir(path) 创建一个目录
os.makedirs(path) 递归的创建目录
os.chdir(dirname) 改变工作目录到dirname
os.path.getsize(name) 获得文件大小，如果name是目录返回0L
os.path.abspath(name) 获得绝对路径
os.path.normpath(path) 规范path字符串形式
os.path.splitext()  分离文件名与扩展名
os.path.join(path, name) 连接目录与文件名或目录
os.path.basename(path) 返回文件名
os.path.dirname(path) 返回文件路径
os.walk(top, topdown=True, onerror=None)  遍历迭代目录
os.rename(src, dst)  重命名file或者directory src到dst 如果dst是一个存在的directory, 将抛出OSError. 在Unix, 如果dst在存且是一个file, 如果用户有权限的话，它将被安静的替换. 操作将会失败在某些Unix 中如果src和dst在不同的文件系统中. 如果成功, 这命名操作将会是一个原子操作(这是POSIX 需要). 在 Windows上, 如果dst已经存在, 将抛出OSError，即使它是一个文件. 在unix，Windows中有效。
os.renames(old, new) 递归重命名文件夹或者文件。像rename()

# shutil库
import shutil  # 针对日常的文件和目录管理任务
shutil.copyfile(src, dst) 从源src复制到dst中去。当然前提是目标地址是具备可写权限。抛出的异常信息为IOException. 如果当前的dst已存在的话就会被覆盖掉
shutil.move(src, dst)  移动文件或重命名
shutil.copymode(src, dst) 只是会复制其权限其他的东西是不会被复制的
shutil.copystat(src, dst) 复制权限、最后访问时间、最后修改时间
shutil.copy(src, dst)  复制一个文件到一个文件或一个目录
shutil.copy2(src, dst)  在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了，类似于cp –p的东西
shutil.copy2(src, dst)  如果两个位置的文件系统是一样的话相当于是rename操作，只是改名；如果是不在相同的文件系统的话就是做move操作
shutil.copytree(olddir, newdir, True / Flase)
把olddir拷贝一份newdir，如果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接
shutil.rmtree(src) 递归删除一个目录以及目录内的所有内容

# glob库
import glob  # 文件通配符,glob模块提供了一个函数用于从目录通配符搜索中生成文件列表:
1、通配符

星号(*)匹配零个或多个字符

import glob
for name in glob.glob('dir/*'):
    print(name)
输出：
dir / file.txt
dir / file1.txt
dir / file2.txt
dir / filea.txt
dir / fileb.txt
dir / subdir

列出子目录中的文件，必须在模式中包括子目录名：

import glob

# 用子目录查询文件
print('Named explicitly:')
for name in glob.glob('dir/subdir/*'):
    print('\t', name)
#用通配符* 代替子目录名
print('Named with wildcard:')
for name in glob.glob('dir/*/*'):
    print('\t', name)
输出：
Named explicitly:
    dir / subdir / subfile.txt
Named with wildcard:
    dir / subdir / subfile.txt
2、单个字符通配符

用问号(?)匹配任何单个的字符。

import glob

for name in glob.glob('dir/file?.txt'):
    print(name)
dir/file1.txt
dir/file2.txt
dir/filea.txt
dir/fileb.txt
3、字符范围

当需要匹配一个特定的字符，可以使用一个范围

import glob
for name in glob.glob('dir/*[0-9].*'):
    print(name)
输出：
dir / file1.txt
dir / file2.txt


# PIL库
from PIL import Image


# sys库
import sys     # 通用工具脚本经常调用命令行参数
例如在命令行中执行 "python demo.py one two three" 后可以得到以下输出结果:
>> > import sys
>> > print(sys.argv)
['demo.py', 'one', 'two', 'three']
>> > arg = sys.argv[0]
>> > print(arg)
one


# random库
import random  # random提供了生成随机数的工具。
>> > import random
>> > random.choice(['apple', 'pear', 'banana'])
'apple'
>> > random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>> > random.random()    # random float
0.17970987693706186
>> > random.randrange(6)    # random integer chosen from range(6)
4

# datetime
import datetime  # datetime模块为日期和时间处理同时提供了简单和复杂的方法。
datetime 有四个模块 date，time，datetime，timedelta
笔记目录
http: // localhost: 8889 / notebooks / python / Untitled1.ipynb

# time库
import time

# logging 日志库
import logging

# matplotlib.pyplot 库
# 直方图
import matplotlib.pyplot as plt
import numpy as np
mu = 100
sigma = 20
x = mu + sigma * np.random.randn(20000)  # 样本数量
plt.hist(x, bins=100, color='green', normed=True)   # bins显示有几个直方,normed是否对数据进行标准化
plt.show()
# 条形图
import matplotlib.pyplot as plt
import numpy as np
y = [20, 10, 30, 25, 15]
index = np.arange(5)
plt.bar(left=index, height=y, color='green', width=0.5)
plt.show()
# 折线图
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 100)
y = x**3
plt.plot(x, y, linestyle='--', color='green', marker='<')
plt.show()
# 散点图
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(1000)
y = x + np.random.randn(1000) * 0.5
plt.scatter(x, y, s=5, marker='<')  # s表示面积，marker表示图形
plt.show()
# 饼状图

import matplotlib.pyplot as plt
import numpy as np
labels = 'A', 'B', 'C', 'D'
fracs = [15, 30, 45, 10]
plt.axes(aspect=1)  # 使x y轴比例相同
explode = [0, 0.05, 0, 0]  # 突出某一部分区域
plt.pie(x=fracs, labels=labels, autopct='%.0f%%', explode=explode)  # autopct显示百分比
plt.show()
# 箱形图 主要用于显示数据的分散情况。图形分为上边缘、上四分位数、中位数、下四分位数、下边缘。外面的点时异常值
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(100)
data = np.random.normal(size=(1000, 4), loc=0, scale=1)
labels = ['A', 'B', 'C', 'D']
plt.boxplot(data, labels=labels)
plt.show()
二、图像的调整
1、23种点形状
"."  point     ","  pixel     "o" circle      "v" triangle_down
"^"  triangle_up     "<" triangle_left     ">" triangle_right     "1"  tri_down
"2"  tri_up       "3"  tri_left      "4"  tri_right       "8"  octagon
"s"  square     "p"  pentagon     "*"  star     "h"  hexagon1     "H"  hexagon2
"+"  plus     "x"  x      "D"  diamond      "d"  thin_diamond
2、8种內建默认颜色的缩写

b: blue         g: green       r: red       c: cyan
m: magenta      y: yellow      k: black     w: white
3、4种线性
- 实线 - -虚线 - .点划线   ：点线
4、一张图上绘制子图
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 100)
plt.subplot(221)  # 2行2列第1个图
plt.plot(x, x)
plt.subplot(222)
plt.plot(x, -x)
plt.subplot(223)
plt.plot(x, x * x)
plt.subplot(224)
plt.plot(x, np.log(x))
plt.show()
5、生成图例
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 11, 1)
plt.plot(x, x * 2)
plt.plot(x, x * 3)
plt.plot(x, x * 4)
plt.legend(['Normal', 'Fast', 'Faster'])
plt.show()