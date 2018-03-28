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
from keras.optimizers import Adam
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D
import cv2
import pickle
from sklearn.preprocessing import StandardScaler




def get_data(path):
    
    filename=open(path,"rb");
    
    return pickle.load(filename)
    

def normalize(im):
    
    return 2*np.array([(im-np.min(im))/(np.max(im)-np.min(im))])-1

def getAngle(pred):
    
    angle=np.arctan2(pred[:,0],pred[:,1])
    angle=np.radians(angle);
    angle=np.pi+angle;
    
    return angle

def getError(pred, degree):
    angle = np.arctan2(pred[:,0],pred[:,1])*180/np.pi # Convert to angle
    angle[angle<0] = angle[angle<0] + 360             # Put in range 0 to 360°
    error = angle - degree                            # Calculate error
    error[error> 180] = error[error> 180] - 360       # Check for 1 compared to  361
    error[error<-180] = error[error<-180] + 360       # Check for 1 compared to -361
    
    return error

def base_model():

    model = Sequential();
    model.add(Conv2D(64, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(64,64,3)));
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu',input_shape=(64,64,3)));
    model.add(MaxPooling2D(pool_size=(2, 2)));
    model.add(Conv2D(64,kernel_size=(3,3),activation='relu',input_shape=(64,64,3)));
    model.add(MaxPooling2D(pool_size=(2,2)));
    model.add(Conv2D(64,kernel_size=(3,3),activation='relu',input_shape=(64,64,3)))
    model.add(Flatten());
    model.add(Dense(32,activation='relu'));
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
hist=model.fit(im,labels_list,epochs=1)

while hist.history['mean_absolute_error'][0] > 0.01: # Go again if MAE too high
    hist = model.fit(im,labels_list,epochs=5)               # Train another epoch
    

        