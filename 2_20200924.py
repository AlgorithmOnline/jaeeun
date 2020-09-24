import collections
def bfs(graph, start_node):
    will_visit=collections.deque(graph[start_node])
    visit=[start_node]
    while will_visit:
        travel  = will_visit.popleft()
        if travel not in visit:
            if len(graph[travel])>0:
                for k in graph[travel]:
                    will_visit.append(k)
            visit.append(travel)
    return set(visit)






computer = int(input())
edges  = int(input())
networks={}
for i in range(computer):
    networks[i+1] =[]
for  _ in range(edges):
    tmp=list(map(int, input().split(" ")))
    if tmp[1] not in networks[tmp[0]]:
        networks[tmp[0]].append(tmp[1])
    if tmp[0] not in networks[tmp[1]]:
        networks[tmp[1]].append(tmp[0])
print(len(bfs(networks, 1))-1)

