
import math
def calcCircleArea(r):
    result = float((math.pi)*(math.pow(r,2)))
    result="{:.2f}".format(result)
    return result
def calcLog(a, b):
    result = float(math.log(a,b))
    result="{:.2f}".format(result)
    return result
def calcSin(x):
    result = float(math.sin(x))
    result="{:.2f}".format(result)
    return result
def calcFactorial(x):
    result = int(math.factorial(x))
    return result
def calcCombination(n, r):
    result = int(math.comb(n,r))
    return result

def calculator(order):
    answer=0
    a = 0
    b = 0
    answer= order.split()
    if answer[0]=="원넓이:":
        a=int(answer[-1])
        answer=calcCircleArea(a)
        return answer
    elif answer[0]=="로그:":
        b=int(answer[-1])
        if answer[1]== "e":
            a =math.e
        answer=calcLog(b,a)     
        return answer 
    elif answer[0]=="사인:":
        a=int(answer[-1])
        answer=calcSin(a)
        return answer  
    elif answer[0]=="팩토리얼:":
        a=int(answer[-1])
        answer=calcFactorial(a)   
        return answer
    elif  answer[0]=="초합:":
        a=int(answer[1])
        b=int(answer[-1])
        answer= calcCombination(a,b)  
        return answer     
      