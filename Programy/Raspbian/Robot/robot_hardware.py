#obsuga robota
import time 
import socket 
#import pygame
import RPi.GPIO as GPIO
AIN1 = 17
AIN2 = 27
BIN1 = 22
BIN2 = 23

class Robot:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(AIN1, GPIO.OUT)
        GPIO.setup(AIN2, GPIO.OUT) 
        GPIO.setup(BIN1, GPIO.OUT)
        GPIO.setup(BIN2, GPIO.OUT)

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

    def makePhoto(self):
        return
