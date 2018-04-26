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
import cv2
import matplotlib.pyplot as plot

def set_keras_backend(backend):       #change the backend of keras to theano or tensorflow

    if K.backend() != backend:
        os.environ['KERAS_BACKEND'] = backend;
        reload(K);
        assert K.backend() == backend;

set_keras_backend("tensorflow");

def SVM_model():
    
    pass  #TODO
    
def OpenCV_model():
    
    pass   #TODO
    
def naive_bayes_model():
    
    pass   #TODO
    
    
def random_forest_model():
    
    pass    #TODO
    
    
def enesmble_model():
    
    pass   #TODO


def base_model(): #function create convolutional neural network model
    
    '''
    #trains the neural network with only the angle ground truts and not the 2-tuple
    #value of both sin(theta) and cos(theta) where theta is the angle value of the
    #blue disk that is relative to an inital refrence frame
    '''
    

    optimizer=keras.optimizers.SGD(lr=0.01,momentum=0.005);    #optimzer
    model = Sequential();                #set variable model equal to Sequental
    model.add(Conv2D(32, kernel_size=(3, 3), activation='elu'  #add convolutional layer
,input_shape=(215,215,3)));
    model.add(Conv2D(32, kernel_size=(3,3) ,  activation='elu'));  #add convolutional layer
    model.add(Conv2D(32, kernel_size=(3,3) ,  activation='elu' ));  #add convolutional layer
    model.add(MaxPooling2D((2,2)))
    model.add(Conv2D(32,kernel_size=(3,3), activation='elu'));     #add convolutional layer
    model.add(Conv2D(32,kernel_size=(3,3), activation='elu'));     #add convolutional layer
    model.add(Conv2D(32,kernel_size=(3,3), activation='elu'));     #add convolutional layer
    model.add(MaxPooling2D(2,2));
    model.add(Flatten());
    model.add(Dense(32 ,activation='softsign'));                    #add fully connected layer
    model.add(Dense(32,activation='softsign'));                        #add fully connected layer
    model.add(Dropout(0.5))                                       #add dropout
    model.add(Dense(32,activation='tanh'));                    #add fully connected layer
    model.add(Dense(32,activation='tanh'));                    #add fully connected layer
    model.add(Dropout(0.5))                                       #add dropout
    model.add(Dense(1,activation='linear'));                      #linear outp for linear regression
    
    # 2 output nodes
    model.compile(optimizer, loss='mean_absolute_error',
                  metrics=['mae']);
    # Loss MSE and metric MAE 

    return model    

def std_model():  #CNN with SGD and two output classes the sine and cosine of the angle theta
                  #which is what the network will try to predict
                  


    optimizer=keras.optimizers.Adam();
    model=Sequential();
    model.add(Conv2D(32,kernel_size=(3,3),input_shape=(215,215,3),activation='relu'));
    model.add(Conv2D(32,kernel_size=(3,3),activation='relu'));
    model.add(Conv2D(32,kernel_size=(3,3),activation='relu'));
    model.add(MaxPooling2D(2,2));
    model.add(Conv2D(32,kernel_size=(3,3),activation='relu'));
    model.add(Conv2D(32,kernel_size=(5,5),activation='relu'));
    model.add(Conv2D(32,kernel_size=(5,5),activation='relu'));
    model.add(Conv2D(32,kernel_size=(5,5),activation='relu'));
    model.add(MaxPooling2D(2,2));
    model.add(Flatten());
    model.add(Dense(32,activation='elu'));
    model.add(Dense(32,activation='elu'));
    model.add(Dense(32,activation='elu'));
    model.add(Dense(32,activation='elu'));
    model.add(Dropout(0.5));
    model.add(Dense(2,activation='tanh'))
    model.compile(optimizer,loss='mse',metrics=['mae']);
    
    return model

def classification_model():
    
    
    model=Sequential();
    model.add(Conv2D(16,kernel_size=(3,3),input_shape=(215,215,3),activation='selu'));
    model.add(Conv2D(16,kernel_size=(3,3),activation='selu'));
    model.add(Conv2D(16,kernel_size=(3,3),activation='selu'));
    model.add(Conv2D(16,kernel_size=(3,3),activation='selu'));
    model.add(MaxPooling2D(2,2));
    model.add(Conv2D(16,kernel_size=(3,3),activation='selu'));
    model.add(Conv2D(16,kernel_size=(3,3),activation='selu'));
    model.add(Conv2D(16,kernel_size=(3,3),activation='selu'));
    model.add(Conv2D(16,kernel_size=(3,3),activation='selu'));
    model.add(MaxPooling2D(2,2));
    model.add(Flatten());
    model.add(Dense(32,activation='elu'));
    model.add(Dense(32,activation='elu'));
    model.add(Dense(32,activation='elu'));
    model.add(Dropout(0.7));
    model.add(Dense(32,activation='elu'));
    model.add(Dense(32,activation='elu'));
    model.add(Dense(32,activation='elu'));
    model.add(Dropout(0.7))
    model.add(Dense(360,activation='softmax'));
    model.compile(loss=keras.losses.categorical_crossentropy,optimizer=keras.optimizers.SGD(lr=0.02
                                                   , momentum=0.005),
    metrics=['categorical_crossentropy']);
    
                  
    return model

def histogram_equilization(img):
    
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV);

    # equalize the histogram of the Y channel
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0]);

    # convert the YUV image back to RGB format
    #img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    
    #img_output = cv2.cvtColor(img_output,cv2.COLOR_BGR2HSV)
    
    return img_yuv
    

def set_up_data(user_string):
    
    
      filename="training_data.pkl";   #file name of pickle file of training_data
      os.chdir("C:\\Users\\Jeremy\\Desktop\Senior Project Design");  #change python 
      data=get_data(filename);                                      #training data
      angle=data[0];                                                #training angle data                               
      im=np.array(data[1]);                                         #training image data
      im=normalize(im);   
      labels_list=data[2];
      if(user_string=='base_model'):
                      
          im=np.concatenate((im,im));
          angle=np.concatenate((angle,angle));
          labels_list=np.concatenate((labels_list,labels_list));
      rng_state=np.random.get_state();
      np.random.shuffle(im);
      np.random.set_state(rng_state);
      np.random.shuffle(angle);
      np.random.set_state(rng_state);
      np.random.shuffle(labels_list);
       # between 0 and 1 
       #image is tuple now of images so get the first element to get correct dimension size
      
      
      return angle,im,labels_list
  
    
  

  
user_string=input("which model do you want to train with ? ");

if(user_string=='std_model'):
    
    model=std_model();
    metrics_used='mean_absolute_error'
    
    
elif(user_string=='base_model'):
    
    model=base_model();
    metrics_used='mean_absolute_error';
    
elif(user_string=='classification_model'):
    
    model=classification_model();
    metrics_used='categorical_crossentropy';
    
else:
    
    raise ValueError(user_string+" is not a function for any model try again");
        


angle,im,labels_list=set_up_data(user_string);
    
try:
    
    
    for var in range(0,im.shape[0]):
    
        im[var]=histogram_equilization(im[var]);
        
except:
    
    pass;
    
    
    
    
#create model for CNN by calling the function created called base_model
gc.collect();
#call the garbage collector



if user_string=='base_model':
    
    comparor=0.05
    hist=model.fit(im,np.array(angle));
    
elif user_string=='classification_model':
    
    angle=keras.utils.np_utils.to_categorical(angle)
    hist=model.fit(im,np.array(angle));
    
    
else:
    
    
    hist=model.fit(im,labels_list);
#fit the model
gc.collect();
#call garbage collector

count=0;
epcohs=[]
mean_absolute_error_vector=[];

while hist.history[metrics_used][0] > 0.005: # Go again if error too high
    
    if user_string=='base_model':
        
        hist = model.fit(im,angle,epochs=1);        # Train another epoch
        
        
    elif user_string=='classification_model':
        
        hist=model.fit(im,angle,epochs=1);
        
    else:
        
        hist=model.fit(im,labels_list,epochs=1);
    
    count=count+1;
    epcohs.append(count)
    mean_absolute_error_vector.append(hist[metrics_used][0])
    gc.collect();
    rng_state=np.random.get_state();
    np.random.shuffle(im);
    np.random.set_state(rng_state);
    np.random.shuffle(angle);
    np.random.set_state(rng_state);
    np.random.set_state(rng_state);
    np.random.shuffle(labels_list);
    
#while the mae is greater than 0.015 continue training the CNN if the mae becomes less than this 
#than break out of the while loop
    
model.save('model_experemntial.h5');   #save thre trained CNN to a file called "model.h5"
        