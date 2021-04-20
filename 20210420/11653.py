import math
N = int(input())
ans_list=[]
while N !=1:
    if len(ans_list)==0:
        start=2
    else:
        start=ans_list[-1]
    for i in range(start,N+1):
        if N % i==0:
            #print(i)
            ans_list.append(i)
            N=N//i
            break
        else:
            continue
print(*ans_list, sep='\n')
        
