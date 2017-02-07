#obsuga robota
import time 
import socket 


class Robot:
    def init(self):
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
        s = int(speed) * 4
        s = 100 if s > 100 else s
        s = -100 if s < -100 else s
        d = int(direction) * 4
        d = 100 if d > 100 else d
        d= -100 if d < -100 else d
        print('going with', s, 'speed and direction: ', d)
        print('2')
        leftEngineSpeed = (s +  d* s/100  ) 
        rightEngineSpeed = (s - d* s/100 )
        
        print ('left engine: ', leftEngineSpeed)
        print('right engine: ', rightEngineSpeed)
        
        return "ok"

    def makePhoto(self):
        return

    
