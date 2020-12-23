import collections
import copy
N ,C = map(int, input().split())
#N,C = 5,3
ans=C
C-=1
lines =[0]*N
for i in range(len(lines)):
    lines[i] = int(input())
lines.sort()
origin_lines = collections.deque(lines )   

def binary_search(low, high ):
   # print(low, high)
    mid = (high+low)//2
    if low==high or mid ==low or high==mid:
        print(mid)
        return 
    else:
        # high, mid, low
        lines = copy.deepcopy(origin_lines)
        travel = lines.popleft()
        maxPass=[travel]
        midPass=[travel]
        minPass=[travel]       
        # high version
        while lines:
           # print(lines)
            travel =  lines.popleft()
            if  -maxPass[-1]+ travel>=high:
                maxPass.append(travel)
            if  -midPass[-1]+ travel>=mid:
                midPass.append(travel)
            
            if  -minPass[-1]+ travel>=low:
                minPass.append(travel)        
    #print(maxPass, midPass, minPass)      
    if len(maxPass)>=ans:
        print(high)
        return
    elif  len(midPass)>=ans and len(maxPass)<ans :
        return binary_search(mid, high  )
    elif len(minPass)>=ans  and len(midPass)<ans :
        return binary_search(low,mid  )
    else:
        return 
        


binary_search(1, max(lines))   
    
