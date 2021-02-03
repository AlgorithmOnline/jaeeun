import collections


def iinput(): return int(input())


def lisinput(): return list(map(int, input().split()))


def minput(): return map(int, input().split())


def liinput(): return list(map(int, list(input())))


def dq(): return collections.deque([])


def pl(a): return a.popleft()


def p(a): return a.pop()


move = [

    [-1, 0],  # 위 0(북)
    [0, 1],  # 오른쪽 1(동)
    [1, 0],  # 아래 2(남)
    [0, -1],  # 왼 3(서)

]


def msinput(N):
    maps = []
    for i in range(N):
        maps.append(liinput())
    return maps


def mssinput(N):
    maps = []
    for i in range(N):
        maps.append(lisinput())
    return maps


def al(a, b):
    a.appendleft(b)
    return a


def a(a, b):
    a.append(b)
    return a


N, M = minput()
r, c, d = minput()
maps = mssinput(N)
will_visit = dq()
will_visit.append((r, c, d))
answer = 0
while will_visit:
    travel = pl(will_visit)
    if maps[travel[0]][travel[1]] == 0:
        maps[travel[0]][travel[1]] = -1  # 현재 위치를 청소한다.
        answer += 1
    tl = travel[2]  # 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다
    i = 0
    while i < 4:
        i += 1
        tl = (tl - 1) % 4
        if 0 <= travel[0] + move[tl][0] < M and 0 <= travel[1] + move[tl][1] < N:
            if maps[travel[0] + move[tl][0]][travel[1] + move[tl][1]] == 0:
                break
        else:
            continue

