import heapq
import collections
N= int(input())
cost=[0 ]
infra=collections.defaultdict(int)
treeMom=collections.defaultdict(list)
tree=collections.defaultdict(list)
for i in range(1, N+1):
    ass=list(map(int, input().split()))
    cost.append(ass[0])
    for k in range(1, len(ass)-1):
        treeMom[i].append(ass[k])
        tree[ass[k]].append(i)
        infra[i]+=1
def bfs(infra, tree,cost,N):
    will_visit=collections.deque([])
    answer=[0 for i in range(N+1)]
    for i in range(1, N+1):
        if infra[i]==0:
            will_visit.append(i)
            answer[i] = cost[i]
    visited=[]
    
    while will_visit:
        travel = will_visit.popleft()
      #  print(travel,will_visit,visited,tree, answer)
        if travel in visited:
            continue
        visited.append(travel)
        while tree[travel]:# 3,4
            k= tree[travel].pop()
            infra[k]-=1
            #print("k::",k,"?",answer[k],"+",cost[travel] )
            if infra[k]==0:
                if k not in will_visit and k not in visited:
                    will_visit.append(k)
                    answer[k]=max(answer[travel]+cost[k], answer[k])
            else:
                answer[k]=max(answer[travel]+cost[k], answer[k])
    for i in range(1, N+1):
        print(answer[i])

bfs(infra, tree,cost,N)            
