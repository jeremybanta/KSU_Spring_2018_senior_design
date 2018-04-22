import RPi.GPIO as GPIO
import time



def define_inputs_and_out_puts():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(0,GPIO.IN);
    GPIO.setup(1,GPIO.OUT);
    GPIO.setup(2,GPIO.OUT);
    GPIO.setup(3,GPIO.OUT);
    GPIO.setup(4,GPIO.OUT);
    GPIO.setup(5,GPIO.OUT);
    GPIO.setup(6,GPIO.OUT);
    GPIO.setup(7,GPIO.OUT);
    GPIO.setup(8,GPIO.OUT);


def get_output(number):

    if(number==0):

        GPIO.output(1,GPIO.LOW)
        GPIO.output(2,GPIO.HIGH)
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)

    elif(number==1):

        GPIO.output(1,GPIO.HIGH)
        GPIO.output(2,GPIO.LOW)
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)


    elif(number==2):

        GPIO.output(1,GPIO.HIGH)
        GPIO.output(2,GPIO.HIGH)
        GPIO.output(3,GPIO.LOW)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)


    elif(number==3):

        GPIO.output(1,GPIO.HIGH)
        GPIO.output(2,GPIO.HIGH)
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.LOW)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)


    elif(number==4):

        GPIO.output(1,GPIO.HIGH)
        GPIO.output(2,GPIO.HIGH)
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)

    elif(number==5):

        GPIO.output(1,GPIO.HIGH)
        GPIO.output(2,GPIO.HIGH)
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.LOW)
        GPIO.output(7,GPIO.HIGH)


    elif(number==6):

        
        GPIO.output(1,GPIO.HIGH)
        GPIO.output(2,GPIO.HIGH)
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.LOW)
        GPIO.output(7,GPIO.HIGH)
        

    elif(number==7):

        GPIO.output(1,GPIO.HIGH)
        GPIO.output(2,GPIO.HIGH)
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(7,GPIO.LOW)

    elif(number==8):

        GPIO.output(8,GPIO.LOW);
