#obsuga robota
import time 
import socket 
#import pygame
import RPi.GPIO as GPIO
AIN1 = 17 #lewy przod
AIN2 = 27 #lewy tyl
BIN1 = 22 #prawy tyl
BIN2 = 23 #prawy przod
Frequency = 50

class Robot:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(AIN1, GPIO.OUT)
        GPIO.setup(AIN2, GPIO.OUT) 
        GPIO.setup(BIN1, GPIO.OUT)
        GPIO.setup(BIN2, GPIO.OUT)
        self.motorLeftForward = GPIO.PWM(AIN1, Frequency)
        self.motorLeftBack = GPIO.PWM(AIN2, Frequency)
        self.motorRightForward = GPIO.PWM(BIN2, Frequency)
        self.motorRightBack = GPIO.PWM(BIN1, Frequency)


    def goForward(self):
        print('going forward')
        (GPIO.output(AIN1, GPIO.HIGH))
        (GPIO.output(AIN2, GPIO.LOW))
        (GPIO.output(BIN1, GPIO.LOW))
        (GPIO.output(BIN2, GPIO.HIGH))
        return

    def goBack(self):
        print('going back')
        (GPIO.output(AIN1, GPIO.LOW))
        (GPIO.output(AIN2, GPIO.HIGH))
        (GPIO.output(BIN1, GPIO.HIGH))
        (GPIO.output(BIN2, GPIO.LOW))
        return

    def turnRight(self):
        print('turn right')
        (GPIO.output(AIN1, GPIO.HIGH))
        (GPIO.output(AIN2, GPIO.LOW))
        (GPIO.output(BIN1, GPIO.HIGH))
        (GPIO.output(BIN2, GPIO.LOW))
        return

    def turnLeft(self):
        print('turn left')
        (GPIO.output(AIN1, GPIO.LOW))
        (GPIO.output(AIN2, GPIO.HIGH))
        (GPIO.output(BIN1, GPIO.LOW))
        (GPIO.output(BIN2, GPIO.HIGH))
        return
    
    def stop(self):
        (GPIO.output(AIN1, GPIO.LOW))
        (GPIO.output(AIN2, GPIO.LOW))
        (GPIO.output(BIN1, GPIO.LOW))
        (GPIO.output(BIN2, GPIO.LOW))
        return
    def move(self, speed, direction):
        speed = round(speed) * 4
        speed = 100 if speed > 100 else speed
        speed = -100 if speed < -100 else speed
        direction = round(direction) * 4
        direction = 100 if direction > 100 else direction
        direction = -100 if direction < -100 else direction
        print('going with', speed, 'speed and direction: ', direction)

        leftEngineSpeed = (speed + direction) /2
        rightEngineSpeed = (speed - direction) /2

        if leftEngineSpeed > 0 :
            self.motorLeftBack.stop()
            self.motorLeftForward.start(leftEngineSpeed)
        else if leftEngineSpeed < 0:
            self.motorLeftForward.stop()
            self.motorLeftBack.start(leftEngineSpeed)
        else:
            self.motorLeftForward.stop()
            self.motorLeftBack.stop()

        if rightEngineSpeed > 0 :
            self.motorRightBack.stop()
            self.motorRightForward.start(rightEngineSpeed)
        else if rightEngineSpeed <0:
            self.motorRightForward.stop()
            self.motorRightBack.start(rightEngineSpeed)
        else:
            self.motorRightForward.stop()
            self.motorRightBack.stop()

        
        return "ok"

    def makePhoto(self):
        return
