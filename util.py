import RPi.GPIO as GPIO
from time import sleep
import os
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

edgetpu = 0

class Motor():
    def __init__(self,Ena,In1,In2):
        self.Ena=Ena
        self.In1=In1
        self.In2=In2
        GPIO.setup(self.Ena,GPIO.OUT)
        GPIO.setup(self.In1,GPIO.OUT)
        GPIO.setup(self.In2,GPIO.OUT)
        self.pwm=GPIO.PWM(self.Ena,100)
        self.pwm.start(0)
    
    def moveF(self,x=100,t=0):
        GPIO.output(self.In1, GPIO.HIGH)
        GPIO.output(self.In2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(x)
        sleep(t)
    
    def moveB(self,x=100,t=0):
        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(self.In2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(x)
        sleep(t)
    
    def stopbot(self,t=0):
        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(self.In2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(0)
        sleep(t)


motor1 = Motor(2,3,4)
motor2 = Motor(14,15,18)

def forward():
    motor1.moveF()
    motor2.moveF()

def right():
    motor1.moveF()
    motor2.moveB()

def left():
    motor1.moveB()
    motor2.moveF()

def back():
    motor1.moveB()
    motor2.moveB()

def stop():
    motor1.stopbot()
    motor2.stopbot()

