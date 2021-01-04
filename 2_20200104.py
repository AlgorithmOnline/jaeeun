import heapq

V,E = map(int, input().split())
K=int(input())

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

will_visit=[]
import heapq
def bfs(node): # visited 로 node 간데 체크
    global graph
    global V
    distances= {node : float('inf') for node in range(1,V+1)}
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

    for i in distances:
        if node ==i :
            print(0)
        elif distances[i]==float('inf'):
            print("INF")
        else:
            print(distances[i])


bfs(K)
