import itertools
def solution(nums):
    isPrime=findPrime()
    num = itertools.combinations(nums,3)
    answer=0
    # 3000 이하의 소수 찾기
    for i in num:
        if isPrime[i[0]+i[1]+i[2]]:
            answer+=1
    return answer

def findPrime():
    isPrime =[1 for  i in range(3011)]
    isPrime[0],isPrime[1]=0,0
    index=2
    while index<3001:
        while isPrime[index]==0 and  index<3001: 
            index+=1
            
        if isPrime[index]==1:
            for i in range(index*2, 3001, index):
                isPrime[i]=0
        index+=1
    return isPrime
