from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import os
import logging

# tensorflow imports
import tensorflow as tf

# tf.keras imports
from tensorflow.keras import Model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Activation, Flatten, Dropout
from tensorflow.keras.layers import BatchNormalization, AveragePooling2D, Input, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def Conv4_model(x_train, num_classes):

    model = Sequential()
    model.add(Conv2D(32, (3, 3), padding='same',
                     input_shape=x_train.shape[1:], name="conv_1"))
    model.add(Activation('relu'))
    model.add(Conv2D(32, (3, 3), name="conv_2"))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), padding='same', name="conv_3"))
    model.add(Activation('relu'))
    model.add(Conv2D(64, (3, 3), name="conv_4"))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes))
    model.add(Activation('softmax'))

    return model
