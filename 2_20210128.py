import collections
def solution(n, edge):
    answer = 0
    maps=collections.defaultdict(list)
    for e in edge:
        maps[e[0]].append(e[1])
        maps[e[1]].append(e[0])
        
    def bfs(maps, start,n):
       # cost=[n-1 for i in range(n+1)]
        cost=[n-1]*(n+1)
        cost[0]=-1
        cost[1]=0
        visited=[]
        will_visit=collections.deque([start])
        while  will_visit:
            travel= will_visit.popleft()
            ww=travel[0]
            visited.append(ww)
            while maps[ww]:
                k = maps[ww].pop()
                if   cost[k]> travel[1]+1 and   k not in visited :
                    will_visit.append((k, travel[1]+1))
                    cost[k]=travel[1]+1 
        maxi = max(cost)
        print(cost)
        c=collections.Counter(cost)
        return c[maxi]
    return bfs(maps,(1,0),n )
