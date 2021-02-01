import sys
import collections
import heapq
N, M = map(int, input().split())
graph=collections.defaultdict(list)
adj_list=[0 for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    adj_list[b]+=1
visited=[]
stack=[]
for i in range(1, len(adj_list)):
    if adj_list[i]==0:
        stack.append(i)
while stack:
    travel= stack.pop()
    visited.append(travel)
    for i in graph[travel]:
        adj_list[i]-=1
        if adj_list[i]==0:
            stack.append(i)
print(*visited)    
