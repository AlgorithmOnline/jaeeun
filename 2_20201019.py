from heapq import heappush, heappop
import sys
#input = sys.stdin.readline
inf = 100000000
def dijkstra(start):
    heap = []
    heappush(heap, [0, start])
    dp = [inf for i in range(n + 1)]
    dp[start] = 0
    while heap:
        we, nu = heappop(heap)
        for ne, nw in s[nu]:
            wei = we + nw
            if dp[ne] > wei:
                dp[ne] = wei
                heappush(heap, [wei, ne])
    return dp
t = int(input())
for _ in range(t):
    n, d, start = map(int, input().split())
    s = [[] for i in range(n + 1)]
    for i in range(d):
        a, b, c = map(int, input().split())
        s[b].append([a, c])
    dp = dijkstra(start)
    max_dp = 0
    cnt = 0
    for i in dp:
        if i != inf:
            if max_dp < i:
                max_dp = i
            cnt += 1
    print(cnt, max_dp)
