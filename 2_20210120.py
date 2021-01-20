# 백준 11725번 트리 부모 찾기
import collections
N = int(input())
tree=collections.defaultdict(list)
for _ in range(N-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def bfs(tree, start):
    will_visit=collections.deque([start])
    visited=[]
    mom=collections.defaultdict(int)
    while will_visit:
        travel = will_visit.popleft()# 1
        if travel in visited:
            continue
        else:
            visited.append(travel)
        getter= tree[travel]
        while getter:
            son = getter.pop()
            if mom[son]==0:
                mom[son]=travel
                will_visit.append(son)
            else:
                pass
            
    return mom  


mom  = bfs(tree, 1)
for i in range(2, N+1):
    print(mom[i])
