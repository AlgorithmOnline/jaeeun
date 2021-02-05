import collections
import sys
input = sys.stdin.readline
import math


def iinput(): return int(input())


def lisinput(): return list(map(int, input().split()))


def minput(): return map(int, input().split())


def liinput(): return list(map(int, list(input())))


def dq(): return collections.deque([])


def pl(a): return a.popleft()


def p(a): return a.pop()


def al(a, b):
    a.appendleft(b)
    return a


def a(a, b):
    a.append(b)
    return a


move = [
    [-1, 0],  # 위
    [0, -1],  # 왼
    [1, 0],  # 아래
    [0, 1],  # 오른쪽
]


def in_r(x, N):
    return (0 <= x[0] and x[0] < N and 0 <= x[1] and x[1] < N)


def snowy(maps, x, y, N):
    move = [
        [-1, 0],  # 위
        [0, -1],  # 왼
        [1, 0],  # 아래
        [0, 1],  # 오른쪽
    ]

    yFull = maps[y[0]][y[1]]
    if yFull == 0:
        return maps, 0
    maps[y[0]][y[1]] = 0
    fallen = 0
    mmove = [y[0] - x[0], y[1] - x[1]]
    mindex = move.index(mmove)
    a = [2 * y[0] - x[0], 2 * y[1] - x[1]]
    part4Percent5 = [3 * y[0] - 2 * x[0], 3 * y[1] - 2 * x[1]]
    # 1
    p1 = int(yFull / 100)
    p7 = int((7 * yFull) / 100)
    p2 = int((2 * yFull) / 100)
    p10 = int((10 * yFull) / 100)
    p5 = int((5 * yFull) / 100)
    use = 2 * (p1 + p7 + p2 + p10) + p5
    yFull -= use
    if in_r(part4Percent5, N):
        maps[part4Percent5[0]][part4Percent5[1]] += p5
    else:
        fallen += p5
    if in_r(a, N):
        maps[a[0]][a[1]] += yFull
    else:
        fallen += yFull
    for i in [1, -1]:
        moveIndex = (mindex + i) % 4
        part1Percent1 = [x[0] + move[moveIndex][0], x[1] + move[moveIndex][1]]
        part3Percent10 = [a[0] + move[moveIndex][0], a[1] + move[moveIndex][1]]
        part2Percent7 = [y[0] + move[moveIndex][0], y[1] + move[moveIndex][1]]
        part2Percent2 = [y[0] + 2 * move[moveIndex][0], y[1] + 2 * move[moveIndex][1]]
        if in_r(part1Percent1, N):
            maps[part1Percent1[0]][part1Percent1[1]] += p1
        else:
            fallen += p1
        if in_r(part3Percent10, N):
            maps[part3Percent10[0]][part3Percent10[1]] += p10
        else:
            fallen += p10
        if in_r(part2Percent7, N):
            maps[part2Percent7[0]][part2Percent7[1]] += p7
        else:
            fallen += p7

        if in_r(part2Percent2, N):
            maps[part2Percent2[0]][part2Percent2[1]] += p2
        else:
            fallen += p2

    return maps, fallen


if __name__ == '__main__':
    N = iinput()
    maps = []
    for _ in range(N):
        maps.append(lisinput())
    answer = 0
    middle = N // 2
    turn = 0
    flag = 0
    x = [middle, middle]
    while x != [0, 0]:
        flag += 1
        turn += 1
        turn %= 4
        step = math.ceil(flag / 2)
        for i in range(step):
            y = [x[0] + move[turn][0], x[1] + move[turn][1]]
            maps, fallen = snowy(maps, x, y, N)
            x = y
            answer += fallen
            if x == [0, 0]:
                break

    print(answer)

