# KSU_Spring_2018_senior_design

#library requirement depencies are

(1) Raspberry Pi 3 B GPIO Python library
(2) Numpy
(3) Tenorflow or Theano
(4) Keras
(5) Keyboard
(6) OpenCV 3
(7) Python 3


#Description of python source code files included

(1) CV_system_validation_test.py

save predicted three images to a file with each one rated 120 degrees apart from the next and with the  same label since the blue disk
is invariant about rotations of 120 degrees then rotation of 120 degrees do not matter so if one of the three images has the slit shown in the similar position as the one shown in the image then we can say the system is working properly. So the reason of this python script is to check and make sure the Machine Vision system is working and make any changes if needed. 

(2) Computer_Vision_validation_test.py

This script will show the error on either the training or validation set of the Computer Vision system there will be a graph displaying the error for each ground_truth position of angle on the blue disk. Script was wrtitten for checking the error from a trained convolutional neural network model but it can be quickly changed for other machine learning approaches or traditional computer vision algorithms.

(3) Computer_Vision_video_test.py


Python Script to make sure the computer vision system is working properly saves a image of the predicted angle of the blue disk as part of the filename and saves the blue disk image as a .png image file.

(4) angle_detection_img_subtraction.py

Finds the angle of the blue disk via a naive approach. First the image is resized to a size of (215,215) then the current image is subtracted from every single training image, then the average absolute value is used to append each of them to a list and the index of the min value is used to find the angle that most closely matches the current angle position of the blue disk. This approach is highly prove to noise and error though and is quite slow so other methods would be preffered.

(5) blob_detection.py

Thresholding methods that can be used choosing the right values to detect blobs in the blue disk and then use the calculated blobs of the blue disk to find the blue disk angle relative to a inital frame of the blue disk. This solution was explored for finding the angle of the blue disk but another solution was chosen instead by using Machine Learning instead.

(6) blue_disk_test_segment.py

displays images from the chosen parameters for segmenting the blue disk and if nessesary one can change the parameters to get the best cropped image of only the blue disk. 

(7) computer_vision_pipeline.py


pipeline of detecting the angle of the blue disk on the raspberry pi this is old code and a different python script was being used for this task but this python script is still included for completness

(8) debug_error.py

test computer vision performance and accuracy and make any changes if needed

(9) int_main.py

main program python script to get the complete computer vision pipeline needed to detect the angle on the blue disk running on the raspberry pi 3.

(10) o.py

check to make sure the webcam is working properly with opencv and make any changes or fixes if needed to fix a problem of the webcam not working how it was intended to work

(11) opencv_machine_vision_test.py


python script for use in saving images for use as training images for the Machine Vision system

(12) processing_libs.py


additional functions written in this python script to increase code readibility and make debugging possible errors in the code easier this will be imported into other scipts as needed

(13) rpi_io.py

Rapsberry Pi functions for turning the blue disk in angle in 15 degree increments in the radial direction. Also includes a function to get the digital value of a number between 1 and 7 given the angle value needed to rotate within the range of 0 degrees to 120 degrees. Also defines the input pins used and the output pins used on the raspberry pi. 

(14) segment_blue_disk.py

contains function for cropping the region of the image that contains the blue disk via the HoughCircles algorithm written in OpenCV 3

(15) show_image_video.py

shows video feed from the webcamera

(16) show_video_image.py

shows video feed from the webcamera

(17) template_matching.py

uses built function for template matching in opencv to find the location of the slit in the blue disk and then uses geometry to get the calculated angle deviation of the blue disk

(18) test_angle_prediction.py

predicted angle deviation value of the blue disk based on the trained keras neural network this is used for testing purposes to see if the system is generalizing to cases that are outside of the training set of images

(19) test_webcam_working.py

test to ensure that the webcamera is working properly

(20) training_cv_system.py

training of computer vision system with variety of methods the one most focused on in this project was the one of using convolutional neural networks. And this script is where the keras convolutional neural network model gets trained on the data.

(21) training_data creator.py

creates artifical data by rotating the image around in 1 degree increments to give data to train the computer vision system via machine learning with regression to classify the angle of the blue disk correctly within a 15 degree tolerance level. Two different images were used with rotations from 0 to 359 degrees for training purposes.







