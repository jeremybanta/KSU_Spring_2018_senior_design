



import cv2;
import RPi.GPIO as GPIO;
from operator import itemgetter;
import time;
import os;
import gc;
import copy;
import numpy as np;
import pickle;
from rpi_io import get_output, define_inputs_and_out_puts;

def get_angle_value(img_vector,current_image):


    average_img_difference=[];
    
    for image in img_vector:

        average_img.append(np.abs(np.mean(image-current_image)));

#def normalize(im):


    #return (im-np.min(im))/(np.max(im)-np.min(im));


def segment_blue_disk(Image):
    
    start_time=time.time();                          #time object name start_time
    #IM=cv2.medianBlur(Image,15)
    IM=cv2.cvtColor(Image,cv2.COLOR_BGR2HSV)[:,:,0];   #convert RGB to HSV colorspace only get Hue
    #which corresponds to the true color of a particular image
    IM = cv2.medianBlur(IM,25);                         #compute medianblur with (9,9) kernel size
    IM=cv2.Canny(IM,45,140);                          
    circles = cv2.HoughCircles(IM,cv2.HOUGH_GRADIENT,dp=1.5,minDist=7,param1=115);
    #houghcircl transform to find circles in image
    #this is used primarly to find the roi of where the bluedisk is in the image
    #and then cut out areas outside this region this will be able to make the
    #system more robust
    
    if circles is not None: #if there are circles found with the HoughCircles transform then 
        

        circles = np.uint16(np.around(circles));
        #round the values of circles
        circles=circles[0];
        #get back circles from tuple of list of lists
    
        for i in circles:
            
            #for each elements in circles do the following
        
            if(i[2]==np.max(circles[:,2])):
                
                #if the second element of i is equal to max possible value of i[2]
                
                i=np.int32(i);  #convert i to int32
            
                
                xmax=i[0]+i[2];            #xmax value
                ymax=i[1]+i[2];            #ymax value
                
                if(i[1]-i[2]<0):           #if miny outside the screen window
                    
                    ymin=0;                #then set ymin equal to zero
                    
                else:
                    
                    ymin=i[1]-i[2];      #if miny inside screen then get actuall value of miny
                    
                if(i[0]-i[2]<0):          #if minx outside screen
                    
                    xmin=0;               #then set xmin equal to zero
                    
                else:
                    
                    xmin=i[0]-i[2];      #if xmin inside screen then get actuall value of minx
                    
    else:
        
            
        return Image;   #return entire image

gc.collect()
define_inputs_and_out_puts();
os.chdir("/home/pi/Desktop/Senior_Project_Design");
filename=open("blue_disks_grayscale.pkl","rb");   #file name of pickle file of training_data
images_list=pickle.load(filename)

def get_angle_of_bdisk(images_list):    


    cap=cv2.VideoCapture(0)
    ret,frame=cap.read();

    if ret:
    
        frame=segment_blue_disk(frame);
        frame=cv2.resize(frame,(215,215));
        frame=cv2.medianBlur(frame,3)
        frame = cv2.fastNlMeansDenoisingColored(frame,None,10,10,7,21)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        angle=get_degree_value(new_IM,im);
        get_output(angle);
        print(angle);
        cv2.imshow('frame',frame);
        cv2.waitKey(0);
        cap.release();
        cv2.DestroyAllWindows()
        

gc.collect();

while(True):



    #if(GPIO.input(0)):

    get_angle_of_bdisk(images_list);

    gc.collect();


