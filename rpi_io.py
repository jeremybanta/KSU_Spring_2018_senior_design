import RPi.GPIO as GPIO
import time



def define_inputs_and_out_puts():  #initalize inputs and outputs on raspberry pi

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

    if(number==0):  #if should be moved 15 degrees

        GPIO.output(1,GPIO.LOW)
        GPIO.output(2,GPIO.HIGH)
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)

    elif(number==1): #if should be moved 30 degrees

        GPIO.output(1,GPIO.HIGH)
        GPIO.output(2,GPIO.LOW)
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)


    elif(number==2):  #if should be moved 45 degrees

        GPIO.output(1,GPIO.HIGH)
        GPIO.output(2,GPIO.HIGH)
        GPIO.output(3,GPIO.LOW)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)


    elif(number==3):   #if should be moved 60 degrees

        GPIO.output(1,GPIO.HIGH)
        GPIO.output(2,GPIO.HIGH)
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.LOW)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)


    elif(number==4):   #if should be moved 75 degrees

        GPIO.output(1,GPIO.HIGH)
        GPIO.output(2,GPIO.HIGH)
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)

    elif(number==5):   #if should be moved 90 degrees

        GPIO.output(1,GPIO.HIGH)
        GPIO.output(2,GPIO.HIGH)
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.LOW)
        GPIO.output(7,GPIO.HIGH)


    elif(number==6):  #if should be moved 105 degrees

        
        GPIO.output(1,GPIO.HIGH)
        GPIO.output(2,GPIO.HIGH)
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.LOW)
        GPIO.output(7,GPIO.HIGH)
        

    elif(number==7):  #if blue disk should not be moved at all

        GPIO.output(1,GPIO.HIGH)
        GPIO.output(2,GPIO.HIGH)
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(7,GPIO.LOW)

    elif(number==8):  #if blue disk should not be moved at all

        GPIO.output(1,GPIO.HIGH)
        GPIO.output(2,GPIO.HIGH)
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(7,GPIO.LOW)
        
def turn_off_all_ouput_io_pins();  #turn all output pins off

    GPIO.output(1,GPIO.HIGH)
    GPIO.output(2,GPIO.HIGH)
    GPIO.output(3,GPIO.HIGH)
    GPIO.output(4,GPIO.HIGH)
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(6,GPIO.HIGH)
    GPIO.output(7,GPIO.HIGH)
        
 
def digitize_output(angle):  #get int value between 1 and 7 for a angle value between 0 and 120 degrees
    
    if(angle/15==8):
        
        return 7;
    
    return int(angle/15)
