N,S = map(int, input().split())
ab = list(map(int, input().split()))


start,end=0,0
answer=float('inf') # 길이
tmp=ab[0]

while start >= 0 and end <N and start<=end:
    
    if S<=tmp:
        answer=min(answer, end-start+1)
        if  start<N and S<tmp:
            tmp-=ab[start]
            start+=1
        else:
            
            end+=1
            if end ==N:
                break
            
            tmp+=ab[end]
        continue
    elif tmp<S:
        end+=1
        if end ==N:
                break
        tmp+=ab[end]
        continue
    else:
        tmp-=ab[start]
        start+=1
        continue
        
    
if answer==float('inf'):
    print(0)
else:
    print(answer)
