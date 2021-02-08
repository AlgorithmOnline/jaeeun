# input = sys.stdin.readline
import collections
import copy


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
    [-1, 0],  # 왼
    [0, -1],  # 아래
    [1, 0],  # 오른쪽
    [0, 1],  # 위
]


def in_r(x, N):
    return (0 <= x[0] and x[0] < N and 0 <= x[1] and x[1] < N)


def in_rc(x, r, c):
    return (0 <= x[0] and x[0] < r and 0 <= x[1] and x[1] < c)


def in_upRs(x, r, maps):
    return (0 <= x[0] and x[0] <= r and x[1] >= 0 and x[1] < len(maps[0]))


def in_downRs(x, r, maps):
    return (r <= x[0] and x[0] < len(maps) and x[1] >= 0 and x[1] < len(maps[0]))


def addNode(A, B):
    return [A[0] + B[0], A[1] + B[1]]


def existAir(A, airs):
    if A in airs:
        return True
    return False


def addDirt(A, n, maps):
    maps[A[0]][A[1]] += n
    return maps


def remainDirt(A, dUse, maps):
    maps[A[0]][A[1]] -= dUse
    return maps


def valueDirt(A, maps):
    return maps[A[0]][A[1]]


def dpcopy(m):
    return copy.deepcopy(m)


def dirtSpread(airs, dirts, maps):
    copyMaps = dpcopy(maps)
    for d in dirts:
        dSpread = valueDirt(d, maps) // 5  # 확산되는양# 확산되는 양은 Ar,c/5이고 소수점은 버린다.
        dUse = 0
        for m in move:  # 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.# (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
            newNode = addNode(m, d)
            if in_rc(newNode, len(maps), len(maps[0])):
                if not existAir(newNode, airs):  # 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
                    dUse += 1
                    copyMaps = addDirt(newNode, dSpread, copyMaps)
        copyMaps = remainDirt(d, dUse * dSpread, copyMaps)  # (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
    return copyMaps


def sortAirs(airs):
    if airs[0][0] > airs[1][0]:
        airs[0], airs[1] = airs[1], airs[0]
    return airs


def in_1sec(dirts, airs, maps):
    #  print("먼지 확산중...")
    maps = dirtSpread(airs, dirts, maps)
    # print("먼지 확산끝...")
    # print(*maps, sep='\n')
    # print('-' * 10)
    timeMove = [[  # 시계

        [0, 1],  # 오른쪽
        [-1, 0],  # 위
        [0, -1],  # 왼
        [1, 0],  # 아래

    ],
        [  # 반시계
            [0, 1],
            # 오른쪽
            [1, 0],
            # 아래
            [0, -1],
            # 왼
            [-1, 0],  # 위

        ]]

    airMaps = copy.deepcopy(maps)
    airs = sortAirs(airs)  # 공기청정기 위아래
    # print("공기청정기중...")
    for i in range(2):
        partAir = airs[i]
        tMoveIndex = 0
        curNode = partAir
        while tMoveIndex < 4:
            if (i == 0 and in_upRs(addNode(curNode, timeMove[i][tMoveIndex]), partAir[i], maps)) or (
                    i == 1 and in_downRs(addNode(curNode, timeMove[i][tMoveIndex]), partAir[i], maps)):
                nextNode = addNode(curNode, timeMove[i][tMoveIndex])
                if nextNode in airs:
                    break
                if curNode in airs:
                    airMaps[nextNode[0]][nextNode[1]] = 0
                else:
                    airMaps[nextNode[0]][nextNode[1]] = valueDirt(curNode, maps)
                curNode = nextNode
            else:
                tMoveIndex += 1
                continue
    return airMaps


# 공기청정기가 작동한다.
# 공기청정기에서는 바람이 나온다.
# 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
# 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
# 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.


if __name__ == '__main__':
    R, C, T = minput()
    maps = []
    dirts = []
    airs = []
    for r in range(R):
        col = lisinput()
        for c in range(C):
            if col[c] > 0:
                dirts.append([r, c])
            elif col[c] < 0:
                airs.append([r, c])
        maps.append(col)
    for t in range(T):
        maps = in_1sec(dirts, airs, maps)
        dirts = []
        for r in range(R):
            for c in range(C):
                if maps[r][c] > 0:
                    dirts.append([r, c])

    #    print(t, "초 작업 결과")
    #   print(*maps, sep='\n')
    #  print('-' * 10)
    answer = 0
    for r in range(R):
        for c in range(C):
            if maps[r][c] > 0:
                answer += maps[r][c]

    print(answer)
