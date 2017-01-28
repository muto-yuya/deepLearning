#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
import tensorflow as tf

import mcz_input
import mcz_model

def main(ckpt_path, csv = 'test2.txt'):
    with tf.Graph().as_default():
        images, labels, filename = mcz_input.load_data_for_test([csv], 610)
        #print 'start', images, labels
        keep_prob = tf.placeholder("float")

        logits = mcz_model.inference_deep(images, keep_prob, mcz_input.DST_INPUT_SIZE, mcz_input.NUM_CLASS)
        acc = mcz_model.accuracy(logits, labels)
        sess = tf.Session()
        #print("logits: ",sess.run(logits))

        saver = tf.train.Saver()
        sess = tf.Session()
        sess.run(tf.initialize_all_variables())
        saver.restore(sess, ckpt_path)
        tf.train.start_queue_runners(sess)

        acc_res, filename_res, actual_res, expect_res = sess.run([acc, filename, logits, labels], feed_dict={keep_prob: 1.0})
        print('accuracy', acc_res)

        goods = []
        bads = []
        print(actual_res)
        for idx, (act, exp) in enumerate(zip(actual_res, expect_res)):
            if np.argmax(act) == np.argmax(exp):
                goods.append(filename_res[idx])
            else:
                bads.append(filename_res[idx])
        print('good')
        for f in goods:
            print('cp',f,'out_goods')
        print('bad')
        for f in bads:
            print('cp',f,'out_bads')
        #correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(labels, 1))

        return


if __name__ == '__main__':
    ckpt_path = '/tmp/data.2017-01-10T00:13:28.209623/model.ckpt-0' #sys.argv[1]
    #csv = sys.argv[2]
    #print ckpt_path
    main(ckpt_path)

