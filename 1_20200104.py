import heapq
from collections import defaultdict 

V,E = map(int, input().split())
K=1

graph={}

for _ in range(E):
    u,v,w =map(int, input().split())
    if u in graph:
        if v in graph[u]:
            graph[u][v]=min(w,graph[u][v])
        else:
            graph[u][v]=w
    else:
        graph[u]={}
        graph[u][v]=w 

    u,v=v,u   
    if u in graph:
        if v in graph[u]:
            graph[u][v]=min(w,graph[u][v])
        else:
            graph[u][v]=w
    else:
        graph[u]={}
        graph[u][v]=w         


v1,v2 =  map(int, input().split())
will_visit=[]
import heapq
def bfs(node,end): # visited 로 node 간데 체크
    global graph
    global V
    distances=defaultdict(lambda : float('inf'))
    will_visit=[]
    heapq.heappush(will_visit, [0,node])
    while will_visit: 
        cur_value,cur_travel = heapq.heappop(will_visit) # K - curvalue
        if cur_travel in graph:
            for  key,value in graph[cur_travel].items():
                total_value = value + cur_value # K - curvalue, curvalue -key == K- key
                if total_value < distances[key]:
                    distances[key]=total_value
                    heapq.heappush(will_visit, [total_value,key ])

    if node == end:
        return 0
    else:
        return distances[end]



answer=min( bfs(1,v1)+bfs(v1,v2)+bfs(v2,V), bfs(1,v2)+bfs(v2,v1)+bfs(v1,V))   
if answer==float('inf'):
    print(-1)
else:
    print(answer)
