# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 17:08:30 2018

@author: Jeremy
"""

import numpy as np                  #import numpy module
import cv2                          #import openCV module
import segment_blue_disk            #import segment_blue_disk module
import os                           #import os module
import gc                           #import garbage collector module
import time                         #import time module
import matplotlib.pyplot as plot    #import matplotlib.pyplot module
import keras                        #import keras module
import pickle                       #import pickle module
from processing_libs import normalize,getAngle,resize   #import functions to getAngle, resize,
#and to normalize the Image
from keras.models import load_model               #import load_model module from keras

os.chdir("C:\\Users\Jeremy\\Desktop\\Senior Project Design");                    #change current directory to C:\Users\Jeremy
start_time=time.time();                           #set variable of start_time to inital value

#of object time.time()

def get_same_angle_values(theta_degrees):
    
    
    #function to get same anglular positions rotated by some multiple of 120 degrees
    #since the blue festo disk has symetrry of rotation about 120 degrees we do not really care 
    #which is because they are considered the same for all practical purposes
    

    theta_degree_vector=[];  #intalize the variable theta_degree_vector to empty list 
                             #this will hold the numpy arrays of three values each of which is a 
                             #angle value
    
    for element in theta_degrees:                #theta_degrees is an iterable object which contains
                                                 #all predicted angle values by the CNN
    
        temp=[element,element+120,element+240];  #get three angle values where the disk will
                                                 #be invariant for practical purposes
                                                 
                                                 
        temp=np.mod(temp,360)                    #get modules of temp and the value 360         
        temp=np.unique(temp)                     #unique values of temp
        temp=np.array(temp,dtype=np.int16)       #convert result to numpy array with type of int16
        theta_degree_vector.append(temp)         #append the 3 tuple numpy array to the list
            
            
            
    return theta_degree_vector;                  #return the list of 3-tuple angle values (in degrees)
        
my_index=0;                                      #set index to value of zero for the inital value
Image_vector=[];                                 #intalize Image_vector to empty list
IM_plot_vector=[];                               #intalize IM_plot_vector to empty list

while(True):                                     #while loop load images if they exist then stop                             
    
    
    
    
    if(not os.path.exists("C:\\Users\\Jeremy\\disk"+str(int(my_index+2))+"\\"+"_0.png")):
        
        break;          #break out of the loop iff the file path for the image does not exist
        
    IM=cv2.imread("C:\\Users\\Jeremy\\disk"+str(int(my_index+2))+"\\_0.png");
    
    #load in image with OpenCV imread read method
    IM=segment_blue_disk.segment_blue_disk(IM);
    #call segment_blue_disk method to crop the image only containing the blue disk
    Image_vector.append(resize(IM))
    #call size function set to resize image to a size of (227,240,3)
    IM_plot_vector.append(IM);
    #add a element of the image numpy array to the IM_plot_vector list
    my_index=my_index+1;
    #increment index by positive value of one

Image_vector=normalize(Image_vector);             #normalize the Image_vector
end_time_pre_process=time.time();                 #get value for use for computing end time

print("elapsted time preprocessing"+" "+str(my_index)+" number of images is: "+
      str(float(end_time_pre_process-start_time))+" seconds")  

#print the time elapsed during program execution

gc.collect();                                   #call the garbage collector
Image_vector=Image_vector[0];                   #extract tuple of list of numpy arrays
comparison_IM_vector=[];                        #comparison_IM_vector initalize to the empty list

for var in range(len(Image_vector)):
    
    
    
    
    
    image=IM_plot_vector[var];
    image=np.flip(image,2);
    plot.figure(var+1);
    plot.imshow(image);
    


gc.collect();                                  #call the garbage collector
model=load_model("model.h5");                  #load trained keras CNN model
prediction_values=model.predict(Image_vector);   #predict the values [sin(theta),cos(theta)]
#for each of the Images which will yield a (n,2) numpy array where n is the number of test
#or validation images

theta_values=getAngle(prediction_values)
theta_values=get_same_angle_values(theta_values);

def makeDirectory(number):                       #function to makeDirectory 
    
    directory="C:\\Users\\Jeremy\\Validation_set"+str(number);

    if not os.path.exists(directory):
        os.makedirs(directory)


count1=0                                          #initial value for count1 set to zero

for elements in theta_values:                     #for each value 
    
    makeDirectory(count1);
    
    for count in range(3):
    
    
        im=cv2.imread("C:\\Users\\Jeremy\\disk0\\_"+str(elements[count])+".png")
        cv2.imwrite("C:\\Users\\Jeremy\\Validation_set"+str(count1)+"\\"+str(count)+".png",im)
        
    count1=count1+1;
    
del prediction_values
del IM_plot_vector
