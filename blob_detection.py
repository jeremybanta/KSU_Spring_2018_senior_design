import numpy as np
import cv2
import os


os.chdir("C:/Users/Jeremy/Desktop/Senior Project Design")

#boolean=input("load image or use live real-time camera for blob detection ? : ");

boolean='image'

if(boolean=='camera'):


    cap = cv2.VideoCapture(1)

    while(True):
    # Capture frame-by-frame
        ret, frame = cap.read()

    # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray=cv2.medianBlur(gray,5)
        gray=cv2.fastNlMeansDenoising(gray,None,10,7,21)
        ret,th1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
        th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
        th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
    # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
        
            cap.release();
            cv2.destroyAllWindows();
        
            break
        
        
if(boolean=='image'):
    
    image=cv2.imread("opencv_frame_0.png")
    cv2.imshow('image',image)
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    hue=hsv[:,:,0]
    hue=cv2.medianBlur(hue,5)
    cv2.imshow('hue',hue);
    ret,thresh1 = cv2.threshold(hue,115,135,cv2.THRESH_BINARY)
    cv2.imshow('binary_image',thresh1)
    th3 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
    cv2.imshow('adaptive thresholding',th3);
    