import collections
def solution(n, path, order):
    mom={}
    will_visit=collections.deque([0])
    orderDict=collections.defaultdict(int)
    roads=collections.defaultdict(list)
    for k in path:
        roads[k[0]].append(k[1])
        roads[k[1]].append(k[0])

    for i in order:
        orderDict[i[1]]=1
        mom[i[0]]=i[1]
    visit=[False for i in range(n)]
    failNum=0
    while will_visit:
        while orderDict[will_visit[0]]!=0 and failNum < len(will_visit) :
            failNum+=1
            will_visit.rotate(1)
        if failNum== len(will_visit) :
            break
        failNum=0    
        t= will_visit.popleft()
        failNum=0
        visit[t]=True
        if t in mom:
            orderDict[mom[t]]=0
        for r in roads[t]:
            if not visit[r]:
                will_visit.append(r)

    return all(visit)
