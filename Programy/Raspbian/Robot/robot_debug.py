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
#        print('going with', s, 'speed and direction: ', d)
        print('2')
        leftEngineSpeed = (s + d) 
        rightEngineSpeed = (s - d)

        leftEngineSpeed = 100 if leftEngineSpeed > 100 else leftEngineSpeed
        leftEngineSpeed = -100 if leftEngineSpeed < -100 else leftEngineSpeed

        rightEngineSpeed = 100 if rightEngineSpeed > 100 else rightEngineSpeed
        rightEngineSpeed = -100 if rightEngineSpeed < -100 else rightEngineSpeed

        lf = lb = rf = fb = 0
        if (d > 0) # 
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

    
