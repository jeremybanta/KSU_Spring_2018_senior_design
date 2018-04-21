# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:22:40 2018

@author: Jeremy
"""


import numpy as np                             #import numpy
import os                                      #operating system
import keras                                   #import keras                #Adam optimizer
from keras.layers.convolutional import Conv2D        #Conv2D
from keras.models import Sequential                 #Sequential
from keras.layers import Dense, Dropout, Flatten     #keras.layers
from keras.layers.pooling import MaxPooling2D        #keras.layers.pooling
import gc                                             #import garbage collector
from processing_libs import get_data,normalize #processing_libs functions
from keras import backend as K
from importlib import reload
from keras import regularizers





def set_keras_backend(backend):

    if K.backend() != backend:
        os.environ['KERAS_BACKEND'] = backend
        reload(K)
        assert K.backend() == backend

#set_keras_backend("theano")
        

        
        
        
def SVM_model():
    
    pass
    
    
    
    
    
    
    
def OpenCV_model():
    
    pass
    
def naive_bayes_model():
    
    pass
    
    
def random_forest_model():
    
    pass
    
    
def enesmble_model():
    
    pass


def base_model(): #function create convolutional neural network model

    model = Sequential();                #set variable model equal to Sequental
    model.add(Conv2D(16, kernel_size=(3, 3), activation=keras.layers.LeakyReLU(alpha=0.3)
,input_shape=(215,215,3)));
    model.add(Conv2D(16, kernel_size=(3,3),  activation=keras.layers.LeakyReLU(alpha=0.3)
))
    model.add(MaxPooling2D((2,2)))
    model.add(Conv2D(32,kernel_size=(3,3),activation=keras.layers.LeakyReLU(alpha=0.3)
))
    model.add(Conv2D(32,kernel_size=(3,3),activation=keras.layers.LeakyReLU(alpha=0.3)
))
    model.add(MaxPooling2D((2,2)))
    model.add(Dropout(.1))
    model.add(Flatten());
    model.add(Dense(360,activation=keras.layers.LeakyReLU(alpha=0.3)
))
    model.add(Dropout(0.2))
    model.add(Dense(120,activation=keras.layers.LeakyReLU(alpha=0.3)
))
    model.add(Dropout(0.2))
    model.add(Dense(60,activation='tanh'))

    
    model.add(Dense(2,activation='linear')) 
    # 2 output nodes
    model.compile(keras.optimizers.SGD(lr=.02,decay=0,momentum=0.05), 'mean_squared_error', 
                  ['mae'])  
    # Loss MSE and metric MAE 

    return model                


filename="training_data.pkl";   #file name of pickle file of training_data
os.chdir("C:\\Users\\Jeremy\\Desktop\Senior Project Design");  #change python 
data=get_data(filename);                                      #training data
angle=data[0];                                                #training angle data                               
im=np.array(data[1]);                                         #training image data
im=normalize(im)                                 

# between 0 and 1 
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
        