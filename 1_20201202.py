N, M = map(int, input().split())
maps=list(range(1, N+1))
def dfs(maps,visit ):
    if len(visit)==M:
        print(*visit)
        return
    elif len(maps)==0:
        return 
    else:
        for i in range(0, len(maps)):
            visit2= visit[:]
            visit2.append(maps[i])
            dfs(maps[i+1:], visit2)

for i in range(0, len(maps)):
    dfs(maps[i+1:], [maps[i]])
