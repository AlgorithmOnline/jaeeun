# 내 풀이
import collections
import math
def bfs(start,endm):
    visit=[start]
    will_visit=collections.deque(graph[start])
    while will_visit:
        travel = will_visit.popleft()
        if travel == end:
            return True
        if travel not in visit:
            visit.append(travel)
          
            for i in graph[travel]:
                will_visit.append(i)
            #will_visit.extend(graph[travel])
    return False

N, M = map(int, input().split())
#graph={}
graph_cost=[]
#for i in range(1, N+1):
#   graph[i]=set()
    
for _ in range(M):
    lis=list(map(int, input().split()))
    #graph[lis[0]].append(lis[1])
    #graph[lis[1]].append(lis[0])
    graph_cost.append([lis[2], [lis[1], lis[0]]])
graph_cost.sort()
start, end = map(int, input().split())

maxi= graph_cost[-1][0]
mini = graph_cost[0][0]
mid_list=[]
answer=0
#print(graph_cost)
while maxi>=mini:
   # print(answer)
    mid = math.ceil((maxi+mini)/2)
    #print(maxi, mini, mid)
    if mid not in mid_list:
        mid_list.append(mid)
        filtered = list(filter(lambda a:a[0]>=mid, graph_cost))
        graph={}
        for i in range(1, N+1):
            graph[i]=[]
        for f in filtered:
            graph[f[1][0]].append(int(f[1][1]))
            graph[f[1][1]].append(int(f[1][0]))
        #print('graph', graph)
        if bfs(start, end):
            answer=max(answer, mid)
            mini = mid-1
        else:
            maxi=mid+1
    else:
        mini+=1
    
print(answer)  
