import math


def distance(x1,y1,x2,y2):
    result= math.sqrt(  ( (x1-x2)**2)+((y1-y2)**2) )
    return result

print(distance(2,2,4,4))