# 백준 4344
import math
T=int(input())
for i in range(T):
    ss=list(map(int, input().split()))
    
    ss=ss[1:]
    ls=len(ss)
    
    ag= list(filter(lambda a:a>sum(ss)/len(ss), ss))
    answer=round((len(ag)/ls)*100000)/1000
    print("%.3f"%answer,"%", sep='',end='\n')
