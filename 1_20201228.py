import math
import sys
from collections import deque, Counter
import heapq   # 우선순위 큐용  # heapq.heappop(heap) # heapq.heappush(heap,(a,a))
import collections
import itertools


def bfs(maps, start_node, ans):
    moves =[[1,0],[0,1],[0,-1],[-1,0]]
    visited = collections.deque([])
    need_visit= collections.deque([])
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.popleft()
        if node not in visited :
            visited.append(node)
            maps[node[0]][node[1]]=ans
            for t in moves:
                travel = [ node[0]+t[0], node[1]+t[1]]
                if 0<=travel[0]<len(maps) and   0<=travel[1]<len(maps[0]) and  maps[travel[0]][travel[1]]==0:
                    maps[travel[0]][travel[1]]=ans
                    need_visit.append(travel)
            
    return maps



T = int(input())
for _ in range(T):
    M,N,K= map(int, input().split())
    maps =[ [-1 for  _ in range(N)] for _ in range(M)]
    vegets=[]
    ans=0
    for i in range(K):
        x,y= map(int, input().split())
        vegets.append([x,y])
        maps[x][y]=0

    for x in range(M):
        for y in range(N):
            if maps[x][y]==0:
                ans+=1
                maps=bfs(maps, [x,y],ans )
    print(ans)
