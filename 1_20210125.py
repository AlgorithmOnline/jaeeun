import heapq
import collections
N, M = map(int, input().split())
ps = [[] for i in range(N + 1)]
ls=[0 for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    ps[a].append(b)
    ls[b]+=1
    
stack=[]
visited=[]
for i in range(1, N+1):
    if ls[i]==0:
        heapq.heappush(stack, i)
while stack:
    
    travel = heapq.heappop(stack)
    if travel in visited:
        continue
    visited.append(travel)
    for k in ps[travel]:
        ls[k]-=1
        if ls[k]==0 and k not in visited:
            heapq.heappush(stack, k)
print(*visited)
