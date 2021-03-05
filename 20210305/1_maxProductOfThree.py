# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import heapq
def solution(A):
    # write your code in Python 3.6
    minusGroup=[]
    minusReverse=[]
    plusGroup=[]
    zero=False
    for i in A:
        if i<0:
            heapq.heappush(minusGroup,i)
            heapq.heappush(minusReverse,-i)
            #minusGroup.append(i)
        elif i>0:
            heapq.heappush(plusGroup,-i)
        elif i==0:
            zero=True
    # 마이너스 2개 이상+ max 양수
    answer=0
    if len(minusGroup)>=2 and len(plusGroup)>0:
        a1=heapq.heappop(minusGroup)
        a2=heapq.heappop(minusGroup)
        a3=min(plusGroup)
        a3*=-1
        answer=max(a1*a2*a3,answer)
    elif len(plusGroup)==0: # 마이너스 꽃밭
        if zero:
            return 0
        else:
            a1=heapq.heappop(minusReverse)
            a2=heapq.heappop(minusReverse)
            a3=heapq.heappop(minusReverse)
            return -1*a1*a2*a3

    # 양수 3개
    if len(plusGroup)>2:
        a1=heapq.heappop(plusGroup)
        a2=heapq.heappop(plusGroup)        
        a3=heapq.heappop(plusGroup)
        a1*=-1
        answer=max(a1*a2*a3,answer)
    
    return answer
