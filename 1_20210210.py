import collections
def solution(n, edge):
    answer = 0
    dp=[float('inf') for _ in range(n+1)]
    dp[1]=0
    dp[0]=-1
    trees=collections.defaultdict(list)
    for e in edge:
        trees[e[0]].append(e[1])
        trees[e[1]].append(e[0])
    will_visit=collections.deque([1])
    while will_visit:
        travel = will_visit.popleft()
        for node in trees[travel]:
            if dp[node]> dp[travel]+1:
                dp[node]= dp[travel]+1
                will_visit.append(node)
    max_dp=max(dp)

    return collections.Counter(dp)[max_dp]
