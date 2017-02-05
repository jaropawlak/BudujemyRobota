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
        self.motorLeftForward.start(0)
        self.motorLeftBack.start(0)
        self.motorRightForward.start(0)
        self.motorRightBack.start(0)

    def __del__(self):
        GPIO.cleanup()


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
        print('move started1')
        print('1')
        s = int(speed) * 4
        s = 100 if s > 100 else s
        s = -100 if s < -100 else s
        d = int(direction) * 4
        d = 100 if d > 100 else d
        d= -100 if d < -100 else d
#        print('going with', s, 'speed and direction: ', d)
        print('2')
        leftEngineSpeed = (s + d) 
        rightEngineSpeed = (s - d)

        leftEngineSpeed = 100 if leftEngineSpeed > 100 else leftEngineSpeed
        leftEngineSpeed = -100 if leftEngineSpeed < -100 else leftEngineSpeed

        rightEngineSpeed = 100 if rightEngineSpeed > 100 else rightEngineSpeed
        rightEngineSpeed = -100 if rightEngineSpeed < -100 else rightEngineSpeed

        if leftEngineSpeed > 0 :
            self.motorLeftBack.ChangeDutyCycle(0)
            self.motorLeftForward.ChangeDutyCycle(leftEngineSpeed)
        elif leftEngineSpeed < 0:
            self.motorLeftForward.ChangeDutyCycle(0)
            self.motorLeftBack.ChangeDutyCycle(-leftEngineSpeed)
        else:
            self.motorLeftForward.ChangeDutyCycle(0)
            self.motorLeftBack.ChangeDutyCycle(0)

        if rightEngineSpeed > 0 :
            self.motorRightBack.ChangeDutyCycle(0)
            self.motorRightForward.ChangeDutyCycle(rightEngineSpeed)
        elif rightEngineSpeed <0:
            self.motorRightForward.ChangeDutyCycle(0)
            self.motorRightBack.ChangeDutyCycle(-rightEngineSpeed)
        else:
            self.motorRightForward.ChangeDutyCycle(0)
            self.motorRightBack.ChangeDutyCycle(0)

        
        return "ok"

    def makePhoto(self):
        return
