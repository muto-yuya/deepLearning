#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random
import numpy as np
import tensorflow as tf

IMAGE_SIZE = 112
INPUT_SIZE = 112
DST_INPUT_SIZE = 112
NUM_CLASS = 8
NUM_EXAMPLES_PER_EPOCH_FOR_TRAIN = 120

MEMBER_NAMES = {
    0: ["高城れに", "reni"],
    1: ["百田夏菜子", "kanako"],
    2: ["玉井詩織", "shiori"],
    3: ["佐々木彩夏", "arin"],
    4: ["有安杏果", "momoka"],
}

def load_data_for_test(csv, batch_size):
    return load_data(csv, batch_size, shuffle = False, distored = False)

def load_data(csv, batch_size, shuffle = True, distored = True):
    queue = tf.train.string_input_producer(csv, shuffle=shuffle)
    reader = tf.TextLineReader()
    key, value = reader.read(queue)
    filename, label = tf.decode_csv(value, [["path"],[1]], field_delim=" ")

    label = tf.cast(label, tf.int64)
    label = tf.one_hot(label, depth = NUM_CLASS, on_value = 1.0, off_value = 0.0, axis = -1)

    jpeg = tf.read_file(filename)
    image = tf.image.decode_jpeg(jpeg, channels=3)
    image = tf.cast(image, tf.float32)
    image.set_shape([IMAGE_SIZE, IMAGE_SIZE, 3])

    if distored:
        cropsize = random.randint(INPUT_SIZE, INPUT_SIZE + (IMAGE_SIZE - INPUT_SIZE) / 2)
        framesize = INPUT_SIZE + (cropsize - INPUT_SIZE) * 2
        image = tf.image.resize_image_with_crop_or_pad(image, framesize, framesize)
        image = tf.random_crop(image, [cropsize, cropsize, 3])
        image = tf.image.random_flip_left_right(image)
        image = tf.image.random_brightness(image, max_delta=0.8)
        image = tf.image.random_contrast(image, lower=0.8, upper=1.0)
        image = tf.image.random_hue(image, max_delta=0.04)
        image = tf.image.random_saturation(image, lower=0.6, upper=1.4)

    image = tf.image.resize_images(image, [DST_INPUT_SIZE, DST_INPUT_SIZE])
    image = tf.image.per_image_standardization(image)

    # Ensure that the random shuffling has good mixing properties.
    min_fraction_of_examples_in_queue = 0.4
    min_queue_examples = int(NUM_EXAMPLES_PER_EPOCH_FOR_TRAIN * min_fraction_of_examples_in_queue)

    return _generate_image_and_label_batch(
        image,
        label,
        filename,
        min_queue_examples, batch_size,
        shuffle=shuffle)

def _generate_image_and_label_batch(image, label, filename, min_queue_examples,
                                    batch_size, shuffle):

    # Create a queue that shuffles the examples, and then
    # read 'batch_size' images + labels from the example queue.
    num_preprocess_threads = 16
    capacity = min_queue_examples + 3 * batch_size

    if shuffle:
        images, label_batch, filename = tf.train.shuffle_batch(
            [image, label, filename],
            batch_size=batch_size,
            num_threads=num_preprocess_threads,
            capacity=capacity,
            min_after_dequeue=min_queue_examples)
    else:
        images, label_batch, filename = tf.train.batch(
            [image, label, filename],
            batch_size=batch_size,
            num_threads=num_preprocess_threads,
            capacity=min_queue_examples + 3 * batch_size)

    # Display the training images in the visualizer.
    tf.image_summary('image', images, max_images = 100)

    labels = tf.reshape(label_batch, [batch_size, NUM_CLASS])
    return images, labels, filename