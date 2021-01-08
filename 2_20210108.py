import sys
input = sys.stdin.readline
N,M = map(int, input().split())
maps=[[0]*M]*N
for i in range(N):
    maps[i] = list(input())
import collections



def bfs(graph, start,N,M):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    answer=float('inf')

    will_visit=collections.deque([start])
  
    while will_visit:
        travel= will_visit.popleft()
        if answer<=travel[2]:
            continue
        
        if travel[0]==N-1 and travel[1]==M-1:
            answer = min(answer, travel[2])
        for  i in range(4):
            travel2=travel[:]
            travel2[0]+=dx[i]
            travel2[1]+=dy[i]
            if 0<=travel2[0]<N and  0<=travel2[1]<M and graph[travel2[0]][travel2[1]]=='1' and [travel2[0],travel2[1]] not in travel[-1]:
                travel2[2]+=1
                travel2[-1].append([travel2[0],travel2[1]])
                
                will_visit.append(travel2)

    return answer

    
print(bfs(maps, [0,0,1,[0,0]],N,M)   )
