N = int(input())
ab = list(map(int, input().split()))
x= int(input())

ab.sort()
start,end=0,N-1
answer=0

while start >= 0 and end <N and start<=end:
    
    tmp = ab[start]+ab[end]
    if tmp>x:
        end-=1
        continue
    elif tmp<x:
        start+=1
        continue
    else:
        if start != end:
            answer+=1
        if start<N-1:
            start+=1
            continue  
        else:
            end-=1
            continue
print(answer)
