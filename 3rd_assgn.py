
# 1 Question
def answer():
    return "next"
print(answer())

# 2 Question 

def leapYear(year):
    if year % 4 ==0:
        return("It's a leap year")
    elif year % 400==0:
        return("It's a leap year")    
    elif year % 100==0:
        return("not a leap year")
    else:
        return("Not a leap year")  
     
print(leapYear(2008))


# 3 Question

def alram(time):
    mm=time%100
    early_min=45                            
    if time >=1000:
        if mm>45:   
           time-=early_min    
        else:
           time-=early_min
           time-=40       
    elif time <1000:
         if mm>45:   
           time-=early_min
         else:
           time-=early_min
           time-=40      
    if time>1200:
        return("오후 "+str(time//100)+"시 "+str(time%100)+"분")
    else:
        return("오전 "+str(time//100)+"시 "+str(time%100)+"분")    
        
print(alram(1610))
print(alram(1000))
print(alram(930))

# 4 Question
def findDaesun(x1,y1,r1,x2,y2,r2):
    disSq=(x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
    
    if(disSq==0 and r1==r2):
        return "어딘지 모르겠다 오바"
    elif((r1-r2)**2 <disSq and disSq<(r1+r2)**2):
        return 2
    elif(disSq==(r1+r2)**2 or disSq==(r1-r2)**2 ):
        return 1    
    elif(disSq>(r1+r2)**2 or disSq< (r1-r2)**2):
        return 0        
print(findDaesun(0,0,1,0,0,1))
print(findDaesun(0,0,4,0,0,1))
print(findDaesun(0,0,1,2,0,1))
print(findDaesun(1,23,23,6,5,5))
print(findDaesun(0,0,4,3,0,1))

         



        

