import copy
from collections import deque


M, N, H = map(int, input().split())
box = [[[]for _ in range(N)] for _ in range(H)]
for h in range(H):
    for n in range(N):
        box[h][n]=list(map(int, input().split()))
ripen_box = copy.deepcopy(box) #인풋을 수정하기 싫어서 복사해준다


#3차원 queue에 넣어준다. 순서는 인풋 순서대로
queue = deque()
for m in range(M):
    for n in range(N):
        for h in range(H):
            if box[h][n][m] == 1:
                queue.append([h, n, m])


#BFS를 3차원으로 바꿔준다
while queue:
    [h, n, m] = queue.popleft()
    
    #앞
    if m > 0 and ripen_box[h][n][m-1] == 0:
        queue.append([h, n, m-1])
        ripen_box[h][n][m-1] = ripen_box[h][n][m] + 1
        
    #뒤
    if m < M-1 and ripen_box[h][n][m+1] == 0:
        queue.append([h, n, m+1])
        ripen_box[h][n][m+1] = ripen_box[h][n][m] + 1
    
    #왼쪽
    if n > 0 and ripen_box[h][n-1][m] == 0:
        queue.append([h, n-1, m])
        ripen_box[h][n-1][m] = ripen_box[h][n][m] + 1
    
    #오른쪽
    if n < N-1 and ripen_box[h][n+1][m] == 0:
        queue.append([h, n+1, m])
        ripen_box[h][n+1][m] = ripen_box[h][n][m] + 1

    #위
    if h > 0 and ripen_box[h-1][n][m] == 0:
        queue.append([h-1, n, m])
        ripen_box[h-1][n][m] = ripen_box[h][n][m] + 1
        
    #아래
    if h < H-1 and ripen_box[h+1][n][m] == 0:
        queue.append([h+1, n, m])
        ripen_box[h+1][n][m] = ripen_box[h][n][m] + 1


#0이 있을 경우, -1만 있을 경우 제거
answer = True
minus_count = N*M*H
for height in ripen_box:
    for row in height:
        if 0 in row:
            answer = False
        minus_count -= row.count(-1)

        
if answer and minus_count:
    min_day = 1
    for height in ripen_box:
        for row in height:
            min_day = max(min_day, max(row))
    print(min_day-1)

else:
    print(-1)
