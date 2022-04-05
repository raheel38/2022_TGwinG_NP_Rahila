
# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 입력을 요구하는 문제가 없습니다.
# answer 변수를 사용하여 문제를 풀이하세요. 반환값은 answer 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 5일 23시 59분.
# 지각 제출 기한: 2022년 4월 6일 23시 59분. 주차 점수에서 20% 감점

# 문제 1번

from multiprocessing.pool import ApplyResult


def intervention(queue):
    for i in range(len(queue)):
        if i>=5:
            if queue[i] =="성은":
                queue.insert(i+1,"승호")
            elif "성은" not in queue:
                queue.append("승호")    
    answer= queue            
    return answer

print(intervention(["쯔위","지효","사나","나연","채영","다현","성은","모모","정연"])) 
print(intervention(["쯔위","지효","사나","나연","채영","다현","성은","모모","정연"])) 
print(intervention(["쯔위","지효","사나","성은","나연","채영","다현","모모","정연"])) 
print(intervention(["쯔위","지효","사나","나연","성은","채영","다현","모모","정연"])) 

# 문제 2번
def pascal(n):
    n=n-1
    line=[1]
    for i in range(max(n,0)):
        line.append(line[i]*(n-i)//(i+1))
    return line
print(pascal(3))
print(pascal(10))    

# 문제 3번
def auto_complete(entry, searchWords):
    a=list()
    for i in searchWords:
        if entry in i:
           a.append(i) 
    answer= a    
    return answer
print(auto_complete("강아지",["커피","강아지","강아지 무료분양","강아지그림","레드벨벳","강아지입양","트와이스"]))    



# 문제 4번
def stock_price(stockChart):
    for i in range(len(stockChart)):
        if stockChart[i] > stockChart[i+1]:
            return"아니야 조금만 더 기다려"
        elif stockChart[i] == stockChart[i]:
            return"아니야 조금만 더 기다려"
        elif stockChart[i] < stockChart[i+1]:   
            answer= stockChart[i]+"일 전에 샀어야지 으이구"
            return answer
    
print(stock_price([+0, +0, +0, +0, +0, +0, +0, +0, +0, +0]))  
print(stock_price([-1, -2, -3, -1, -2, -3, -4, -5, -7, +0])) 
print(stock_price([-1, -2, +3, -7, +2, +4, -5, +6, 0, +1])) 
print(stock_price([-1, -2, +0, +0, +1, +2, +3, +4, -10, +2])) 
print(stock_price([-2005, -100, +3000, +2500, +700, +450, -50, +670, 0, +8010, -900, -200, +3550, -11500, +2000, +40, -50, +600, -2000, -1820, +200, +500, +800, +1000]))    

# 문제 5번
def decryption(letter):
    dec = 'abcdefghijklmnopqrstuvwxyz'
    enc = 'xyzabcdefghijklmnopqrstuvw'
    for i in range(len(letter)): 
       if letter[i] in enc:
           if letter[i] in dec:
             answer= letter[i]
           return answer

print(decryption("""Ylr xob rkabo qeb molqbzqflk lc x oxzzllk.
Nriifcfbp qeb Lrzhv Lbqqbo bccbzq xka vlr tfii exsb qeb oxzzllk 'p irzh.
S1 qorpq qeb oxzzllk xka exsb x kfzb axv exex"""))    



