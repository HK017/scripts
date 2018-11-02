'''
tensorflow 是在会话用运行，一个会话会可以有多张图，一个图中会有操作op


'''

import tensorflow as tf
#创建一个变量
a = tf.Variable([[1,2]], name='counter')  #可以命名
b = tf.Variable([[2],[3]])
#创建一个常量
c = tf.constant([[1,2]])
d = tf.constant([[2],[3]])

x = tf.Variable([1,2])
e = tf.constant([2,3])



init = tf.global_variables_initializer()
# 定义一个会话，启动默认图
with tf.Session() as sess:
    result = tf.matmul(a, b)    #矩阵乘法
    result1 = tf.multiply(a, b) #对应位置相乘
    result2 = tf.matmul(c, d)
    sub = tf.subtract(x, e)     #张量减法
    add = tf.add(x, sub)

    sess.run(init)
    print(sess.run(result))
    print(sess.run(result1))
    print(sess.run(result2))
    print(sess.run(sub))
    print(sess.run(add))


# 对变量进行赋值,不能用=号，初始化为0
state = tf.Variable(0, name='count')
new_value = tf.add(1, state)
update = tf.assign(state, new_value) # 讲new_value 赋值给state

init1 = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init1)                               #一个init不能在很多sess中共用
    print(sess.run(state))
    for _ in range(5):
        sess.run(update)
        print(sess.run(state))