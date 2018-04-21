# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 02:31:26 2018

@author: Jeremy
"""




# -*- coding: utf-8 -*-


import numpy as np;                  #import numpy
import cv2;                          #import opencv
import gc                            #import garbage collector
import pickle;                       #import pickle
import time;                         #import time
import segment_blue_disk             #import segment_blue_disk script
from processing_libs import resize   #import resize from processing_libs script of functions

start=time.time();                                     #intalize variable to time program
pathname="C:/Users/Jeremy/Desktop/Blue_disk_training_images";           #change pathname
theta_list=[];                                         #intalize thet_list to empty list
how_many_disks=2;
number_value=['3','4']
Start_Image_vector=[];                                        #intalize list of images to empty
file_names=["blue_disk_img3","blue_disk_img4"];                    #filename to load

for var in range(0,how_many_disks):                           #for each disk append the image to the list
    
    Start_Image_vector.append(cv2.imread(pathname+"/"+file_names[var]+".png"));
    

training_IM_list=[];          #list for the training Images inital value to empty list
labels_list=[];               #labels list initalize to empty list
centroid_IM=lambda IM: np.array(np.array(np.shape(IM)),dtype=np.int32);

#centroid function find the center of the image for computation of the image rotation for
#training the machine learning system


for var in range(0,int(how_many_disks)):   #for loop for each disk
    t11=time.time();                       #time object use for timing program speed
    initial_IM=Start_Image_vector[var];    #get Image
    print(initial_IM.shape)                #print shape of image
    initial_IM=segment_blue_disk.segment_blue_disk(initial_IM);
                                                   
    #call segment_blue_disk recursively two times
    print(initial_IM.shape)               #print image shape to the screen
    initial_IM=resize(initial_IM);        #resize image to size 
    print(initial_IM.shape);
    center=np.array(centroid_IM(initial_IM)/2,dtype=np.int32);
    center=center[0:2];                         #only first two elements of center are important for 
    #the system so slice the zeroth and first element
    center_0=center;                    #make a copy of the variable center as center_0
    center=np.flip(center,0);           #flip the center vector around axis=0
    center=tuple(center);               #convert center datatype to tuple
    t22=time.time();                     #get variable t22 of object time.time()
    print(float(t22-t11));               #print elapsted time to the screen
    t33=time.time();                      #make new time object
    for theta in range(0,360):
        
        #for each theta value in range [0,360)
        #rotate each image in the image vector and save the image in a file directory
        #for each image in the image vector for rotated angles of 0 degrees to 359 degrees
    
        
        M=cv2.getRotationMatrix2D(center,theta,1);                   #rotation matrix
        rot=cv2.warpAffine(initial_IM,M,(initial_IM.shape[1],initial_IM.shape[0]));
        #rot is the rotated image
        cv2.imwrite("C:/Users/Jeremy/Desktop/Senior Project Design/"
                    +"disk"+number_value[var]+"/_"+str(theta)+".png",rot);
        #write rotated image to a image file
        #saving with number of angle value in degrees apended to image for making labeled 
        #training data on
        training_IM_list.append(rot);
        #add the image to the list of all training images
        labels_list.append([np.sin(np.radians(theta)),np.cos(np.radians(theta))]);
        #labels_list is the outputs contain cos(theta) and sin(theta)
        #these will be the ouputs used for training the machine learning system via regression
        theta_list.append(theta);
        #add the theta angle value to the list of angle values
        gc.collect();
        #call the garbage collector
    
    
    t44=time.time();                                  #make new time object called t44
    print(float(t44-t33));                            #print elapsted time


labels_list=np.array(labels_list);                    #convert labels_list from list to np.array
file_name=open("training_data.pkl","wb")               #open file for saving pickle data
pickle.dump((theta_list,training_IM_list,labels_list),file_name) #dump pickle data
gc.collect();                                                    #call the garbage collector
labels_list=[];
end=time.time();                                              #time object created called end

print(end-start)                                        #display time elapsted of total program
