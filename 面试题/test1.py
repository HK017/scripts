import tensorflow as tf
#获取变量的方式主要有以下两种，实践中tf.get_variable产生的变量一定要搭配tf.variable_scope使用，不然运行脚本会报错
v = tf.get_variable('v',shape= [1],initializer = tf.constant_initializer(1.0))
# v1 = tf.get_variable('v1',shape= [1],initializer = tf.constant_initializer(1.0))
print(v)
#使用直接定义变量不会报错，可以一直调用
vc = tf.Variable(tf.constant(1.0,shape = [1]),name = 'v')
print(vc)
#以下使用with语法，将tf.get_variable与tf.variable_scope搭配使用,且reuse=True时，之前必须定义V
with tf.variable_scope('',reuse = True):
    v = tf.get_variable('v',shape= [1],initializer = tf.constant_initializer(1.0))
    print(v)
    v1 = tf.get_variable('v1',shape= [1],initializer = tf.constant_initializer(1.0))
    print(v1==v)

# 如果tf.get_variable()获取一个已经创建的变量，需要通过tf.variable_scope()函数生成一个上下文管理器，并明确指定tf.get_variable()将直接获取已经生成的变量
# 并且是 tf.variable_scope('',reuse = True) 其中第一个参数是命名空间名称
# 当 reuse 设置为 True 或者 tf.AUTO_REUSE 时，表示这个scope下的变量是重用的或者共享的，也说明这个变量以前就已经创建好了。但如果这个变量以前没有被创建过，则在tf.variable_scope下调用tf.get_variable创建这个变量会报错。
with tf.variable_scope('test'):
    print(tf.get_variable('v',shape= [1],initializer = tf.constant_initializer(1.0)))

# tensorflow中创建variable的2种方式：
# 1.tf.Variable()：只要使用该函数，一律创建新的variable，如果出现重名，变量名后面会自动加上后缀1，2….
# 2.tf.get_variable()：如果变量存在，则使用以前创建的变量，如果不存在，则新创建一个变量。

# tensorflow中的两种作用域
# 1.命名域(name scope)：通过tf.name_scope()来实现；
# 2.变量域（variable scope）：通过tf.variable_scope()来实现；可以通过设置reuse 标志以及初始化方式来影响域下的变量。
# 这两种作用域都会给tf.Variable()创建的变量加上词头，而tf.name_scope对tf.get_variable()创建的变量没有词头影响，代码如下：

# 使用slim.arg_scope 参数域分为两个步骤
# 定义你要对哪些函数使用默认参数
# 定义你要使用的默认参数的具体值

import tensorflow.contrib.slim as slim


# from collections import Counter,deque,defaultdict,namedtuple,ChainMap,OrderedDict
# d = dict([('a', 1), ('d', 2), ('c', 3), ('b',2)])
# od = OrderedDict(d)
#
# od = OrderedDict(sorted(od.items(), key=lambda x:x[1]))
# for i in od.items():
#     print(i)