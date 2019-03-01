import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

x = tf.placeholder(tf.float32,shape=[None,784])
y = tf.placeholder(tf.float32,shape=[None,10])
keep_prob = tf.placeholder(dtype=tf.float32)

def weight_varibales(shape):
    init = tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(init)

def bias_variables(shape):
    init = tf.constant(0.1,shape=shape)
    return tf.Variable(init)

def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')

def max_pool_2x2(x):
    """
    最大池化
    :param x: 卷积结果
    :return: 2x2的池化，步长为2x2
    """
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')


x_image = tf.reshape(x,[-1,28,28,1])

w_conv1 = weight_varibales([5,5,1,32])
b_conv1 = bias_variables([32])
h_conv1 = tf.nn.relu(conv2d(x_image,w_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)  # [-1,14,14,32]


w_conv2= weight_varibales([5,5,32,64])
b_conv2 = bias_variables([64])
h_conv2 = tf.nn.softmax(conv2d(h_pool1,w_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2) # [-1,7,7,64]

# 全连接层1
w_f1 = weight_varibales([7*7*64,1024])
b_f1 = bias_variables([1024])

h_pool2_flat = tf.reshape(h_pool2,[-1,7*7*64])
h_f1 = tf.nn.relu(tf.matmul(h_pool2_flat,w_f1) + b_f1)
h_f1_drop_out1 = tf.nn.dropout(h_f1,keep_prob=keep_prob)

# 全连接层2
w_f2 = weight_varibales([1024,10])
b_f2 = bias_variables([10])
h_f2 = tf.nn.softmax(tf.matmul(h_f1_drop_out1,w_f2) + b_f2)


# loss
cross_entropy = -tf.reduce_sum(y*tf.log(h_f2))

train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(h_f2,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

init  = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(1,2001):
        batch = mnist.train.next_batch(50)
        sess.run(train_step,feed_dict={x:batch[0],y:batch[1],keep_prob:0.7})
        if i%100 == 0:
            print(i,sess.run(accuracy,feed_dict={x:batch[0],y:batch[1],keep_prob:0.7}))
    print("test accuracy %g" % accuracy.eval(feed_dict={x: mnist.test.images, y: mnist.test.labels, keep_prob:1.0}))