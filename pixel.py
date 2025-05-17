import math as m
# 
class Pixel:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.colour = None
        self.distance = m.sqrt(x^2+y^2)
        
# x, the value to run the equation on
# a, the mean value 
# s, the standard deviation
def std_dev(x,a,s):
    return (1/(s*m.sqrt(2*m.pi)))*m.e^(-(x-a)^2/(2*s^2))