import tensorflow as tf
from utils import Conv_layer,Max_pooling

def rpn(net, scope='RPN'):
    with tf.variable_scope(scope):
        with tf.variable_scope('conv2d_256'):
            net = Conv_layer(net, 512, [3,3], 2, 'same', tf.nn.relu, 'conv2d_256')
            rpn_cls_score_net = Conv_layer(net, 18, [1,1], 1, 'same', None, 'conv2d_18')
            rpn_bbx_pred_net = Conv_layer(net, 36, [1,1], 1, 'same', None, 'conv2d_36')

            return rpn_cls_score_net, rpn_bbx_pred_net


