import numpy as np
import  tensorflow as tf

x_data = np.random.rand(100)
y_data = x_data*0.1 + 0.2

b = tf.Variable(0.)
k = tf.Variable(0.)
y = k*x_data + b
'''
使得loss最小，
1.定义代价函数
2.定义优化器
3.用优化器进行优化，优化参数的值
4.进行迭代优化使loss最小
'''



#二次代价函数
loss = tf.reduce_mean(tf.square(y_data-y))

#定义一个梯度下降法来进行训练的优化器
optimizer = tf.train.GradientDescentOptimizer(0.2)

#最小化代价函数
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

with  tf.Session() as s:
    s.run(init)
    for step in range(500):
        s.run(train)
        if step%20 == 0:
            print(step, s.run([k, b]))