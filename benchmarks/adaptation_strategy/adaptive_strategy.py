#!/usr/bin/env python

from tensorflow.python.util import deprecation
from kungfu.tensorflow.ops import (all_reduce, barrier, current_cluster_size,
                                   get_init_checkpoint, reshape_strategy)
import tensorflow as tf
import argparse
import time


# disable eager execution for tf2 compat
# tf.compat.v1.disable_eager_execution()

deprecation._PRINT_DEPRECATION_WARNINGS = False

p = argparse.ArgumentParser(description='Adaptation Benchmark.')

args = p.parse_args()


def show_duration(duration):
    if duration < 1:
        return '%.2fms' % (duration * 1e3)
    if duration < 60:
        return '%.2fs' % duration
    sec = int(duration)
    mm, ss = sec / 60, sec % 60
    if duration < 3600:
        return '%dm%ds' % (mm, ss)
    return '%dh%dm%ds' % (mm / 60, mm % 60, ss)


# x = tf.Variable(tf.ones([], dtype=tf.int32))
x = tf.ones((10,1), dtype=tf.int32)
print(x.numpy())

steps = 10
for i in range(steps):
    t0 = time.time()
    v = all_reduce(x)
    print('step %d, took %s' %
            (i, show_duration(time.time() - t0)))

    t0 = time.time()
    keep = reshape_strategy()
    print('reshape took %s' %
            (show_duration(time.time() - t0)))
    if not keep:
        break
