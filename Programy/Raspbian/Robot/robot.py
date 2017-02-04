#obsuga robota
import time 
import socket 


class Robot:
    def __init__(self):
        print('initialize')
        return

    def goForward(self):
        print('going forward')       
        return

    def goBack(self):
        print('going back')       
        return

    def turnRight(self):
        print('turn right')
        return

    def turnLeft(self):
        print('turn left')

        return
    
    def stop(self):
        print('stop')
        return

    def move(self, speed, direction):
        speed = speed * 4
        speed = 100 if speed > 100.0 else speed
        speed = -100 if speed < -100.0 else speed
        direction = direction * 4
        direction = 100 if direction > 100.0 else direction
        direction = -100 if direction < -100.0 else direction
        print('going with', speed, 'speed and direction: ', direction)
        return 
    def makePhoto(self):
        return
