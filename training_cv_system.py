# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:22:40 2018

@author: Jeremy
"""


import matplotlib.pyplot as plot
import numpy as np
import os
import keras
from keras.optimizers import Adam
from keras.layers.convolutional import Conv2D
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D
import pickle
from sklearn.preprocessing import StandardScaler
import gc
from processing_libs import get_data,normalize,resize


def base_model():

    model = Sequential();
    model.add(Conv2D(16, kernel_size=(5, 5),
                 activation='relu',
                 input_shape=(240,227,3)));
    model.add(Conv2D(16, kernel_size=(5, 5), activation='relu',input_shape=(240,227,3)));
    model.add(MaxPooling2D(pool_size=(2, 2)));
    model.add(Conv2D(16,kernel_size=(5,5),activation='relu',input_shape=(240,227,3)))
    model.add(Flatten());
    model.add(Dense(16,activation='relu'));
    #model.add(Dropout(0.1))
    model.add(Dense(2,activation='linear'))                  # 2 output nodes
    model.compile(keras.optimizers.SGD(lr=0.02,momentum=0,decay=0), 'mean_squared_error', ['mae'])  # Loss MSE and metric MAE  

    return model                # Train for 1 epoch


filename="training_data.pkl";
os.chdir("C:\\Users\\Jeremy");
scaler=StandardScaler();
data=get_data(filename);
angle=data[0];
im=np.array(data[1]);
im=normalize(im);
im=im[0]
labels_list=data[2];
model=base_model();
gc.collect();
hist=model.fit(im,labels_list,epochs=1);
gc.collect();

while hist.history['mean_absolute_error'][0] > 0.015: # Go again if MAE too high
    hist = model.fit(im,labels_list,epochs=2);               # Train another epoch
    gc.collect();
    
model.save('model.h5');
        