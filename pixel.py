import math as m
# 
class Pixel:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.colour = None
        #print(x,y)
        self.distance = m.sqrt((x*x)+(y*y))
        if x == 0 and y==0:
            angle = 0
        elif x==0 and y>0:
            angle = m.pi/2
        elif x==0 and y<0:
            angle = 1.5*m.pi
        else: 
            angle = m.atan(y/x*2)
        
        if x<0:
            angle += m.pi
        if x>0 and y<0:
            angle+= 2*m.pi 
        self.angle = angle
# x, the value to run the equation on
# a, the mean value 
# s, the standard deviation
def std_dev(x,a,s):
    return (1/(m.sqrt(2*m.pi)))*m.e**(-(x-a)**2/(2*s*s))

