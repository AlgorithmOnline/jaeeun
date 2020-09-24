#제발 list.pop(0)를 쓰지 마세요! 
# 파이썬의 최대 재귀 깊이는 1,000 근처입니다. 그래서 재귀로 DFS를 구현하면 방법에 따라 런타임 에러가 날 수 있습니다. 
#sys.setrecursionlimit으로 이 깊이를 조절할 수 있습니다.
import collections 

def bfs(graph,start_node):
    visited=[]
    will_visit=[]
    # 두개의 큐로 된다.
    if start_node in graph:
        will_visit=collections.deque(sorted(graph[start_node][:]))
    visited.append(start_node)
    while will_visit:
        travel = will_visit.popleft()
        if travel not in visited:
            visited.append(travel)
            if travel in graph: # 런타임 해소 돼라. graph에 node라는 key가 없을 수도 있습니다.
                aaaa=sorted(graph[travel])
                for kl in aaaa:
                    will_visit.append(kl)
    print(*visited)
    return

def dfs(graph,start_node):
    visited=[]
    will_visit=[]
    # 큐, 스택으로 된다.
    if start_node in graph:
        will_visit=collections.deque(sorted(graph[start_node][:], reverse=True))
    visited.append(start_node)
    
    while will_visit:
        
        travel = will_visit.pop()
        if travel not in visited:
            visited.append(travel)
            if travel in graph: # 런타임 해소 돼라. graph에 node라는 key가 없을 수도 있습니다.
                aaaa=sorted(graph[travel], reverse=True)
                for kl in aaaa:
                    will_visit.append(kl)
        

    print(*visited)
    return

N, M , V =map(int, input().split(" "))
maps = []
for _ in range(M):
    maps.append(list(map(int, input().split(" "))))
graph={}
while maps:
    gg=maps.pop()
    if gg[0] in graph:
        graph[gg[0]].append(gg[1])
    else:
        graph[gg[0]]=[gg[1]]
    if gg[1] in graph:
        graph[gg[1]].append(gg[0])
    else:
        graph[gg[1]]=[gg[0]]

# for j in graph:
#     graph[j]=sorted(graph[j],reverse=True)
#print(graph)
# graph={
#     1:[4,3,2],
#     2:[4,1],
#     3:[4,1],
#     4:[3,2,1]
# }
dfs(graph,V)
bfs(graph,V)


