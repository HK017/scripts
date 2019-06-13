import tensorflow as tf


def Conv_layer(input, filter, kernel, stride, padding, activation, scope):
    with tf.variable_scope(scope):
        return tf.layers.conv2d(inputs=input,
                                filters=filter,
                                kernel_size=kernel,
                                strides=stride,
                                padding=padding,
                                activation=activation,
                                use_bias=False)


def BatchNorm(x, scope):
    with tf.variable_scope(scope):
        mean, variance = tf.nn.moments(x, [0,1,2], keep_dims=True)
        x = tf.nn.batch_normalization(x, mean, variance, offset=0, scale=1, variance_epsilon=1e-4)
    return x


def Relu(x, scope):
    with tf.variable_scope(scope):
        return tf.nn.relu(x)


def Dropout(x, keep_prob):
    return tf.nn.dropout(x, keep_prob=keep_prob, name='drop_out')


def Global_average_pooling(x, scope):
    with tf.variable_scope(scope):
        return tf.reduce_mean(x, axis=[1, 2], keepdims=True)


def GroupNorm(x, G, gamma, beta, eplsion=1e-5):
    """GN 把通道分为组，并计算每一组之内的均值和方差，以进行归一化,GN 的计算与批量大小无关，其精度也在各种批量大小下保持稳定"""
    with tf.variable_scope('Gropu_Norm'):
        N, H, W, C = x.get_shape()
        x = tf.reshape(x, [N, H, W, G, C // G])
        mean, var = tf.nn.moments(x, [1, 2, 5], keep_dims=True)
        x = (x - mean) / tf.sqrt(var + eplsion)
        x = tf.reshape(x, [N, H, W, C])

        return x * gamma + beta


def Average_pooling(x, ksize, stride, scope):
    with tf.variable_scope(scope):
        return tf.nn.avg_pool(x, ksize=[1, ksize, ksize, 1], strides=[1, stride, stride, 1], padding='SAME')


def transition_layer(x, scope):
    with tf.variable_scope(scope):
        x = BatchNorm(x, scope + 'bn1')
        x = Relu(x, scope + 'relu1')
        in_channel = x.get_shape()[-1]

        x = Conv_layer(x, filter=int(in_channel // 2), kernel=1, stride=1, scope='conv1')
        x = Dropout(x, 0.2)

        x = Average_pooling(x, 2, 2, scope + 'global_pooling')

        return x


def bottleneck_layer(x, scope):
    with tf.variable_scope(scope):
        x = BatchNorm(x, scope + 'bn1')
        x = Relu(x, scope + 'relu1')
        x = Conv_layer(x, filter=32 * 4, kernel=1, stride=1, scope='conv_1x1')
        x = Dropout(x, 0.2)
        x = BatchNorm(x, scope + 'bn2')
        x = Relu(x, scope + 'relu2')
        x = Conv_layer(x, filter=32, kernel=3, stride=1, scope='conv_3x3')
        x = Dropout(x, 0.2)

    return x


def dense_block_layer(x, nb_layers, scope):
    with tf.variable_scope(scope):
        layer_concat = list()
        layer_concat.append(x)

        x = bottleneck_layer(x, scope='bottleneck_layer_0')

        layer_concat.append(x)

        for i in range(nb_layers - 1):
            x = tf.concat(layer_concat, axis=3)
            x = bottleneck_layer(x, 'bottleneck_layer_' + str(i + 1))
            layer_concat.append(x)

    return tf.concat(layer_concat, axis=3)


def Max_pooling(x, ksize, stride, scope):
    with tf.variable_scope(scope):
        return tf.layers.max_pooling2d(x, pool_size=ksize, strides=stride, padding='SAME', name='max_pooling')


def Flatten(x, scope):
    with tf.variable_scope(scope):
        return tf.layers.flatten(x)


def Fc_layers(x, class_num, scope):
    with tf.variable_scope(scope):
        return tf.layers.dense(x, units=class_num)

