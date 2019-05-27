import tensorflow as tf
from utils import Conv_layer,Max_pooling,Global_average_pooling,Fc_layers,Flatten


def ResNet50(inputs, class_num, end_point='Average_pool/average_pooling', scope='ResNet50'):

    end_points = {}
    """每一个stage_layer 为3,4,6,3 个Block"""
    with tf.variable_scope(scope):
        with tf.variable_scope('Head_layer'):
            net = Conv_layer(inputs, filter=64, kernel=[7,7], stride=2, pddding='valid', activation=tf.nn.relu, scope='conv2d_7x7_2')
            net = Max_pooling(net, ksize=3, stride=2, scope='max_pooling_3x3_2')
            end_points['Head_layer/max_pooling_3x3_2'] = net
            if end_point == 'Head_layer/max_pooling_3x3_2':
                return net, end_points

        with tf.variable_scope('Stage_layer_1'):
            with tf.variable_scope('Block1'):
                net1 = Conv_layer(net, filter=64, kernel=[1, 1], stride=1, pddding='valid',activation=tf.nn.relu, scope='conv2d_a_1x1_1')
                net1 = Conv_layer(net1, filter=64, kernel=[3, 3], stride=1, pddding='same',activation=tf.nn.relu, scope='conv2d_b_3x3_1')
                net1 = Conv_layer(net1, filter=256, kernel=[1, 1], stride=1, pddding='valid',activation=tf.nn.relu, scope='conv2d_c_1x1_1')
                identify_net = Conv_layer(net, filter=256, kernel=[1, 1], stride=1, pddding='valid',activation=tf.nn.relu, scope='conv2d_d_1x1_1')
                net = tf.add(identify_net, net1, name='add')
                net = tf.nn.relu(net, name='relu')
                end_points['Stage_layer_1/Block1/relu'] = net
                if end_point == 'Stage_layer_1/Block1/relu':
                    return net, end_points

            with tf.variable_scope('Block2'):
                net2 = Conv_layer(net, filter=64, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu, scope='conv2d_a_1x1_1')
                net2 = Conv_layer(net2, filter=64, kernel=[3, 3], stride=1, pddding='same', activation=tf.nn.relu, scope='conv2d_b_3x3_1')
                net2 = Conv_layer(net2, filter=256, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu, scope='conv2d_c_1x1_1')
                net = tf.add(net, net2, name='add')
                net = tf.nn.relu(net, name='relu')
                end_points['Stage_layer_1/Block2/relu'] = net
                if end_point == 'Stage_layer_1/Block2/relu':
                    return net, end_points

            with tf.variable_scope('Block3'):
                net3 = Conv_layer(net, filter=64, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu, scope='conv2d_a_1x1_1')
                net3 = Conv_layer(net3, filter=64, kernel=[3, 3], stride=1, pddding='same', activation=tf.nn.relu, scope='conv2d_b_3x3_1')
                net3 = Conv_layer(net3, filter=256, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu,scope='conv2d_c_1x1_1')
                net = tf.add(net, net3, name='add')
                net = tf.nn.relu(net, name='relu')
                end_points['Stage_layer_1/Block3/relu'] = net
                if end_point == 'Stage_layer_1/Block3/relu':
                    return net, end_points

        with tf.variable_scope('Stage_layer_2'):
            with tf.variable_scope('Block1'):
                net1 = Conv_layer(net, filter=128, kernel=[1, 1], stride=2, pddding='valid', activation=tf.nn.relu, scope='conv2d_a_1x1_2')
                net1 = Conv_layer(net1, filter=128, kernel=[3, 3], stride=1, pddding='same', activation=tf.nn.relu, scope='conv2d_b_3x3_1')
                net1 = Conv_layer(net1, filter=512, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu, scope='conv2d_c_1x1_1')
                identify_net = Conv_layer(net, filter=512, kernel=[1, 1], stride=2, pddding='valid', activation=tf.nn.relu, scope='conv2d_d_1x1_1')
                net = tf.add(identify_net, net1, name='add')
                net = tf.nn.relu(net, name='relu')
                end_points['Stage_layer_2/Block1/relu'] = net
                if end_point == 'Stage_layer_2/Block1/relu':
                    return net, end_points

            with tf.variable_scope('Block2'):
                net2 = Conv_layer(net, filter=128, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu, scope='conv2d_a_1x1_1')
                net2 = Conv_layer(net2, filter=128, kernel=[3, 3], stride=1, pddding='same', activation=tf.nn.relu, scope='conv2d_b_3x3_1')
                net2 = Conv_layer(net2, filter=512, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu, scope='conv2d_c_1x1_1')
                net = tf.add(net, net2, name='add')
                net = tf.nn.relu(net, name='relu')
                end_points['Stage_layer_2/Block2/relu'] = net
                if end_point == 'Stage_layer_2/Block2/relu':
                    return net, end_points

            with tf.variable_scope('Block3'):
                net3 = Conv_layer(net, filter=128, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu, scope='conv2d_a_1x1_1')
                net3 = Conv_layer(net3, filter=128, kernel=[3, 3], stride=1, pddding='same', activation=tf.nn.relu, scope='conv2d_b_3x3_1')
                net3 = Conv_layer(net3, filter=512, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu,scope='conv2d_c_1x1_1')
                net = tf.add(net, net3, name='add')
                net = tf.nn.relu(net, name='relu')
                end_points['Stage_layer_2/Block3/relu'] = net
                if end_point == 'Stage_layer_2/Block3/relu':
                    return net, end_points

            with tf.variable_scope('Block4'):
                net4 = Conv_layer(net, filter=128, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu, scope='conv2d_a_1x1_1')
                net4 = Conv_layer(net4, filter=128, kernel=[3, 3], stride=1, pddding='same', activation=tf.nn.relu, scope='conv2d_b_3x3_1')
                net4 = Conv_layer(net4, filter=512, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu,scope='conv2d_c_1x1_1')
                net = tf.add(net, net4, name='add')
                net = tf.nn.relu(net, name='relu')
                end_points['Stage_layer_2/Block4/relu'] = net
                if end_point == 'Stage_layer_2/Block4/relu':
                    return net, end_points

        with tf.variable_scope('Stage_layer_3'):
            with tf.variable_scope('Block1'):
                net1 = Conv_layer(net, filter=256, kernel=[1, 1], stride=2, pddding='valid', activation=tf.nn.relu,scope='conv2d_a_1x1_2')
                net1 = Conv_layer(net1, filter=256, kernel=[3, 3], stride=1, pddding='same', activation=tf.nn.relu,scope='conv2d_b_3x3_1')
                net1 = Conv_layer(net1, filter=1024, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu,scope='conv2d_c_1x1_1')
                identify_net = Conv_layer(net, filter=1024, kernel=[1, 1], stride=2, pddding='valid',activation=tf.nn.relu, scope='conv2d_d_1x1_1')
                net = tf.add(identify_net, net1, name='add')
                net = tf.nn.relu(net, name='relu')
                end_points['Stage_layer_3/Block1/relu'] = net
                if end_point == 'Stage_layer_3/Block1/relu':
                    return net, end_points

            with tf.variable_scope('Block2'):
                net2 = Conv_layer(net, filter=256, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu,scope='conv2d_a_1x1_1')
                net2 = Conv_layer(net2, filter=256, kernel=[3, 3], stride=1, pddding='same', activation=tf.nn.relu,scope='conv2d_b_3x3_1')
                net2 = Conv_layer(net2, filter=1024, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu,scope='conv2d_c_1x1_1')
                net = tf.add(net, net2, name='add')
                net = tf.nn.relu(net, name='relu')
                end_points['Stage_layer_3/Block2/relu'] = net
                if end_point == 'Stage_layer_3/Block2/relu':
                    return net, end_points

            with tf.variable_scope('Block3'):
                net3 = Conv_layer(net, filter=256, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu,scope='conv2d_a_1x1_1')
                net3 = Conv_layer(net3, filter=256, kernel=[3, 3], stride=1, pddding='same', activation=tf.nn.relu,scope='conv2d_b_3x3_1')
                net3 = Conv_layer(net3, filter=1024, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu,scope='conv2d_c_1x1_1')
                net = tf.add(net, net3, name='add')
                net = tf.nn.relu(net, name='relu')
                end_points['Stage_layer_3/Block3/relu'] = net
                if end_point == 'Stage_layer_3/Block3/relu':
                    return net, end_points

            with tf.variable_scope('Block4'):
                net4 = Conv_layer(net, filter=256, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu,scope='conv2d_a_1x1_1')
                net4 = Conv_layer(net4, filter=256, kernel=[3, 3], stride=1, pddding='same', activation=tf.nn.relu,scope='conv2d_b_3x3_1')
                net4 = Conv_layer(net4, filter=1024, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu,scope='conv2d_c_1x1_1')
                net = tf.add(net, net4, name='add')
                net = tf.nn.relu(net, name='relu')
                end_points['Stage_layer_3/Block4/relu'] = net
                if end_point == 'Stage_layer_3/Block4/relu':
                    return net, end_points

            with tf.variable_scope('Block5'):
                net5 = Conv_layer(net, filter=256, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu,scope='conv2d_a_1x1_1')
                net5 = Conv_layer(net5, filter=256, kernel=[3, 3], stride=1, pddding='same', activation=tf.nn.relu,scope='conv2d_b_3x3_1')
                net5 = Conv_layer(net5, filter=1024, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu,scope='conv2d_c_1x1_1')
                net = tf.add(net, net5, name='add')
                net = tf.nn.relu(net, name='relu')
                end_points['Stage_layer_3/Block5/relu'] = net
                if end_point == 'Stage_layer_3/Block5/relu':
                    return net, end_points

            with tf.variable_scope('Block6'):
                net6 = Conv_layer(net, filter=256, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu,scope='conv2d_a_1x1_1')
                net6 = Conv_layer(net6, filter=256, kernel=[3, 3], stride=1, pddding='same', activation=tf.nn.relu,scope='conv2d_b_3x3_1')
                net6 = Conv_layer(net6, filter=1024, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu,scope='conv2d_c_1x1_1')
                net = tf.add(net, net6, name='add')
                net = tf.nn.relu(net, name='relu')
                end_points['Stage_layer_3/Block6/relu'] = net
                if end_point == 'Stage_layer_3/Block6/relu':
                    return net, end_points

        with tf.variable_scope('Stage_layer_4'):
            with tf.variable_scope('Block1'):
                net1 = Conv_layer(net, filter=512, kernel=[1, 1], stride=2, pddding='valid', activation=tf.nn.relu,scope='conv2d_a_1x1_2')
                net1 = Conv_layer(net1, filter=512, kernel=[3, 3], stride=1, pddding='same', activation=tf.nn.relu,scope='conv2d_b_3x3_1')
                net1 = Conv_layer(net1, filter=2048, kernel=[1, 1], stride=1, pddding='valid',activation=tf.nn.relu, scope='conv2d_c_1x1_1')
                identify_net = Conv_layer(net, filter=2048, kernel=[1, 1], stride=2, pddding='valid', activation=tf.nn.relu, scope='conv2d_d_1x1_1')
                net = tf.add(identify_net, net1, name='add')
                net = tf.nn.relu(net, name='relu')
                end_points['Stage_layer_4/Block1/relu'] = net
                if end_point == 'Stage_layer_4/Block1/relu':
                    return net, end_points

            with tf.variable_scope('Block2'):
                net2 = Conv_layer(net, filter=512, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu,scope='conv2d_a_1x1_1')
                net2 = Conv_layer(net2, filter=512, kernel=[3, 3], stride=1, pddding='same', activation=tf.nn.relu,scope='conv2d_b_3x3_1')
                net2 = Conv_layer(net2, filter=2048, kernel=[1, 1], stride=1, pddding='valid',activation=tf.nn.relu, scope='conv2d_c_1x1_1')
                net = tf.add(net, net2, name='add')
                net = tf.nn.relu(net, name='relu')
                end_points['Stage_layer_4/Block2/relu'] = net
                if end_point == 'Stage_layer_4/Block2/relu':
                    return net, end_points

            with tf.variable_scope('Block3'):
                net3 = Conv_layer(net, filter=512, kernel=[1, 1], stride=1, pddding='valid', activation=tf.nn.relu,scope='conv2d_a_1x1_1')
                net3 = Conv_layer(net3, filter=512, kernel=[3, 3], stride=1, pddding='same', activation=tf.nn.relu,scope='conv2d_b_3x3_1')
                net3 = Conv_layer(net3, filter=2048, kernel=[1, 1], stride=1, pddding='valid',activation=tf.nn.relu, scope='conv2d_c_1x1_1')
                net = tf.add(net, net3, name='add')
                net = tf.nn.relu(net, name='relu')
                end_points['Stage_layer_4/Block3/relu'] = net
                if end_point == 'Stage_layer_4/Block3/relu':
                    return net, end_points

        with tf.variable_scope('Average_pool'):
            net = Global_average_pooling(net,'average_pooling')
            print(net.get_shape())

            end_points['Average_pool/average_pooling'] = net
            if end_point == 'Average_pool/average_pooling':
                return net, end_points


        with tf.variable_scope('Fc_layer'):
            net = Flatten(net, 'flatten')
            net = Fc_layers(net, class_num, 'fc_layer')
            end_points['Fc_layer/fc_layer'] = net
            if end_point == 'Fc_layer/fc_layer':
                return net, end_points

            return net, end_points




if __name__ == '__main__':
    x = tf.placeholder(dtype=tf.float32, shape=[100, 229,229,3], name='x')
    result,end_points = ResNet50(x, 1000)
    for i in tf.trainable_variables():
        print(i)
    print(result.get_shape())