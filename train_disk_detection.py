# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import tensorflow as tf
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras.optimizers import SGD
import numpy as np
import cv2
from importlib import reload
from keras import backend as K


def set_keras_backend(backend):

    if K.backend() != backend:
        os.environ['KERAS_BACKEND'] = backend
        reload(K)
        assert K.backend() == backend




isdisk="C:\\Users\\Jeremy\\Desktop\\Senior Design Capstone Project\\is_disk"
isdisk_filenames=os.listdir(isdisk)
isdisk=isdisk+"\\"
notdisk="C:\\Users\\Jeremy\\Desktop\\Senior Design Capstone Project\\not_disk"
not_disk_filename=os.listdir(notdisk)
notdisk=notdisk+"\\"
ground_truth_values=[]
image_vector=[]


def normalize(image):
    
    return (image-np.min(image))/(np.max(image)-np.min(image))

for fname in isdisk_filenames:
    
    image_vector.append(cv2.resize(normalize(cv2.imread(isdisk+fname)),(160,120)))
    ground_truth_values.append(1)
    
for fname in not_disk_filename:
    
    image_vector.append(cv2.resize(normalize(cv2.imread(notdisk+fname)),(160,120)))
    ground_truth_values.append(0)
    
def shuffle_in_unison(a, b):
    rng_state = np.random.get_state()
    np.random.shuffle(a)
    np.random.set_state(rng_state)
    np.random.shuffle(b)
    
    
for var in range(0,4):
    
    image_vector=image_vector+image_vector
    ground_truth_values=ground_truth_values+ground_truth_values
    
ground_truth_values=np.array(ground_truth_values)
image_vector=np.array(image_vector)

print(cv2.imread(notdisk+fname).shape)


def std_model():
    
    model=Sequential();
    model.add(Conv2D(32,(5,5),input_shape=(120,160,3),activation='elu'))
    model.add(Conv2D(32,(5,5),input_shape=(120,160,3),activation='elu'))
    model.add(MaxPooling2D((2,2)))
    model.add(Conv2D(32,(5,5),activation='elu'))
    model.add(Conv2D(32,(5,5),activation='elu'))
    model.add(MaxPooling2D((2,2)))
    model.add(Conv2D(32,(5,5),activation='relu'))
    model.add(Conv2D(32,(5,5),activation='relu'))
    model.add(MaxPooling2D((2,2)))
    model.add(Flatten())
    model.add(Dense(32,activation='elu'))
    model.add(Dense(32,activation='elu'))
    model.add(Dense(1,activation='sigmoid'))
    model.compile(optimizer=SGD(lr=0.02,momentum=0.0005),loss='binary_crossentropy',
                  metrics=['accuracy'])
    
    return model


model=std_model()


hist=model.fit(x=image_vector,y=ground_truth_values)

while hist.history['acc'][-1]<0.995:
    
    shuffle_in_unison(image_vector,ground_truth_values)
    hist=model.fit(x=image_vector,y=ground_truth_values)

model.save("detect_blue_disk.h5")