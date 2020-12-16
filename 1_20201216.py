import collections
N,k = map(int, input().split())
a= collections.deque(list(range(1, N+1)))
answer=[]
while a:
    a.rotate(-k+1)
    
    answer.append(a.popleft())
    
    #print(a)
print("<",end="")
print(*answer,sep=", ",end="")
print(">")
