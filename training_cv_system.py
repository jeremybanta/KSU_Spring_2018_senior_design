# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:22:40 2018

@author: Jeremy
"""


import matplotlib.pyplot as plot               #import matplotlib
import numpy as np                             #import numpy
import os                                      #operating system
import keras                                   #import keras
from keras.optimizers import Adam                  #Adam optimizer
from keras.layers.convolutional import Conv2D        #Conv2D
from keras.models import Sequential                 #Sequential
from keras.layers import Dense, Dropout, Flatten     #keras.layers
from keras.layers.convolutional import Convolution2D #keras.layers.convolutional
from keras.layers.pooling import MaxPooling2D        #keras.layers.pooling
import pickle                                       #import pickle
from sklearn.preprocessing import StandardScaler    #import StandardScaler
import gc                                             #import garbage collector
from processing_libs import get_data,normalize,resize  #processing_libs functions


def base_model(): #function create convolutional neural network model

    model = Sequential();                #set variable model equal to Sequental
    model.add(Conv2D(16, kernel_size=(5, 5),
                 activation='relu',
                 input_shape=(240,227,3)));
                     
    #add Convolution layer kernel_size is (5,5) activation 'relu' input_shape is (240,227,3)
    model.add(Conv2D(16, kernel_size=(5, 5), activation='relu',input_shape=(240,227,3)));
    #add Convolution layer kernel_size is (5,5) activation 'relu' input_shape is (240,227,3)
    model.add(MaxPooling2D(pool_size=(2, 2)));
    #add a maxpooling layer of size of (2,2)
    model.add(Conv2D(16,kernel_size=(5,5),activation='relu',input_shape=(240,227,3)))
    #add Convolution layer kernel_size is (5,5) activation 'relu' input_shape is (240,227,3)
    model.add(Flatten());
    #add flatten to the model (flatten the neural network)
    model.add(Dense(16,activation='relu'));
    #add a Dense hidden layer to the neural network
    
    model.add(Dense(2,activation='linear')) 
    # 2 output nodes
    model.compile(keras.optimizers.SGD(lr=0.02,momentum=0,decay=0), 'mean_squared_error', ['mae'])  
    # Loss MSE and metric MAE  

    return model                


filename="training_data.pkl";   #file name of pickle file of training_data
os.chdir("C:\\Users\\Jeremy\\Desktop\Senior Project Design");  #change python directory
scaler=StandardScaler();                                      #use standard scaler
data=get_data(filename);                                      #training data
angle=data[0];                                                #training angle data                               
im=np.array(data[1]);                                         #training image data
im=normalize(im);                                             #normalize the training image data
# between -1 and 1 
im=im[0]
#image is tuple now of images so get the first element to get correct dimension size
labels_list=data[2];
#labels of the data are the last element of data
model=base_model();
#create model for CNN by calling the function created called base_model
gc.collect();
#call the garbage collector
hist=model.fit(im,labels_list,epochs=1);
#fit the model
gc.collect();
#call garbage collector

while hist.history['mean_absolute_error'][0] > 0.015: # Go again if MAE too high
    hist = model.fit(im,labels_list,epochs=2);               # Train another epoch
    gc.collect();
#while the mae is greater than 0.015 continue training the CNN if the mae becomes less than this 
#than break out of the while loop
    
model.save('model.h5');   #save thre trained CNN to a file called "model.h5"
        