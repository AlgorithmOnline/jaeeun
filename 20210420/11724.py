import sys
# 이게 젤중요 진짜 별표 억만게
sys.setrecursionlimit(10000)


def dfs(node):
    visited[node] = True
    for i in adj[node]:
        if visited[i]:
            pass
        else:
    
            dfs(i)


n, m = map(int, sys.stdin.readline().split(" "))

adj = [ [] for _ in range(n+1)]
visited = [False] * (n+1)
ans = 0

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split(" "))
    adj[a].append(b)
    adj[b].append(a)


for i in range(1, n+1):         
    if not visited[i]:
        ans += 1
        dfs(i)
print(ans)
