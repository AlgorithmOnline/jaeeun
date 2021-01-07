N = int(input())
ab = list(map(int, input().split()))

min_ans=float('inf') # 0 에 근접할 수록 좋음 
ans_list=[0,0]
ab.sort()

start,end=0,N-1
answer=0

while start >= 0 and end <N and start<end:
    
    tmp = ab[start]+ab[end]
    if abs(tmp)<abs(min_ans):
        min_ans=tmp
        ans_list[0] = ab[start]
        ans_list[1] = ab[end]
        if  tmp<0:
            start+=1
        else:
            end-=1
        continue
    elif tmp<0:
        start+=1
        continue
    else:
        end-=1
        continue
        
    
    
print(*ans_list)
