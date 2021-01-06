import sys

n, m = map(int, sys.stdin.readline().split())
maps = list()
for _ in range(n):
    map_tmp = sys.stdin.readline().strip()
    map_tmp = list(map(lambda x: int(x), map_tmp))
    maps.append(map_tmp)

queue = [(0, 0, 1)]
visited = [[[0] * 2 for i in range(m)] for i in range(n)]
visited[0][0][1] = 1
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
count = -1

while queue:
    x, y, bump = queue.pop(0)
    if x == n - 1 and y == m - 1:
        count = visited[x][y][bump]
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if maps[nx][ny] == 0 and visited[nx][ny][bump] == 0:
                queue.append((nx, ny, bump))
                visited[nx][ny][bump] = visited[x][y][bump] + 1
            if maps[nx][ny] == 1 and bump == 1:
                queue.append((nx, ny, 0))
                visited[nx][ny][0] = visited[x][y][1] + 1

print(count)
