import collections
import sys
import collections
import heapq
def topo(graph,n):
    visited=[]
    stack=collections.deque([])
    
    for g in range(1, n+1):
        if len(graph[g])==0:
            
            stack.append(g)
    while stack:
        travel = stack.popleft()
        if travel in visited:
            return []
        visited.append(travel)
        double = 0
        for k in range(1, n+1):
            
            if k in graph  and travel in graph[k]:
                graph[k].remove(travel)
                if len(graph[k])==0:
                    double +=1
                    stack.append(k)

    if len(visited)==n:
        visited.reverse()
        print(*visited)
    else:
        print("IMPOSSIBLE")

T= int(input())
for jj in range(T):
    n= int(input())
    graph=collections.defaultdict(list)
    last_year = list( map(int, input().split()))
    for k in range(len(last_year)):
        for j in range(k):
            graph[last_year[j]].append(last_year[k])
    m=int(input())
    if m ==0:
        print(*last_year)
        continue
    for _ in range(m): 
        a,b=map(int, input().split())
        if a not in graph[b]:
            graph[a].remove(b)
            graph[b].append(a)               
        else:
            graph[b].remove(a)
            graph[a].append(b)

    reverse =topo(graph,n)

