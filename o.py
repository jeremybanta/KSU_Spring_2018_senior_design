import numpy as np
import time
import cv2

cap = cv2.VideoCapture(0)

if not(cap.isOpened()):
    cap.open()

count=0;

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    k= cv2.waitKey(1)
    if k == 32:#when u press spacebar display that frame in another window
        cv2.imshow('new',frame)
    elif k == ord('q'):#press q to quit

        break

    elif k == ord('s'): #press the s key to save the image

        count=count+1;
        cv2.imwrite("/home/pi/Desktop/blue_disk_img"+str(count)+".png",frame);

        continue;

cap.release()
cv2.destroyAllWindows()
