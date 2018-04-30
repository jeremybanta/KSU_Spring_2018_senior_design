# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 09:02:13 2018

@author: Jeremy
"""


import numpy as np
from operator import itemgetter
import cv2
import os
import pickle
import time
from segment_blue_disk import segment_blue_disk



def get_angle_value(current_image,image_vector): #get angle value by image subtraction and getting index of lowest avg image difference

    
    my_vector=[];
    
    for image in image_vector:
        
        
        my_vector.append(np.abs(np.mean(current_image-image)))
        
        
    return min(enumerate(my_vector), key=itemgetter(1))[0] 


def chdir(pathname):
    
    os.chdir("C:\\Users\\Jeremy\\Desktop\Senior Project Design");
        
def load_image_list():
    
    
    

    filename=open("blue_disks_grayscale.pkl","rb");   #file name of pickle file of training_data
    return pickle.load(filename)


def process_frame(frame): #crop region of image where the blue disk is in the image automatically

    frame=segment_blue_disk(frame)
    frame=cv2.resize(frame,(215,215))
    #frame=cv2.medianBlur(frame,5)
    frame = cv2.fastNlMeansDenoisingColored(frame,None,10,10,7,21)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    return frame



chdir("C:\\Users\\Jeremy\\Desktop\Senior Project Design");  #change directory

img_list=load_image_list();   #load list of images

cam = cv2.VideoCapture(1)  #video caputre object

cv2.namedWindow("test")

img_counter = 0

while True:
    
    start_time=time.time();
    ret, frame = cam.read()
    
    
    if(ret):   #if opencv reads iamge from camera
        
        
        
        frame=process_frame(frame)           #segment region where blue disk is at
        angle=get_angle_value(frame,img_list)  #get the angle value
        
        
        
        end_time=time.time()
    
        print(np.mod(angle,360))          #angle value
        print(float(end_time-start_time))  #time of program in seconds
        
        
    
    cv2.imshow("test", frame)
    k=cv2.waitKey(1);
    
    if not ret:
        break
    

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        
        break;

cam.release()
cv2.destroyAllWindows()




    
    
