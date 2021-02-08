# input = sys.stdin.readline
import collections
import copy


def iinput(): return int(input())


def lisinput(): return list(map(int, input().split()))


def minput(): return map(int, input().split())


def liinput(): return list(map(int, list(input())))


def dq(): return collections.deque([])


def popl(a): return a.popleft()


def appendl(a, b):
    a.appendleft(b)
    return a


def in_r(x, N):
    return (0 <= x[0] and x[0] < N and 0 <= x[1] and x[1] < N)


def in_rc(x, r, c):
    return (0 <= x[0] and x[0] < r and 0 <= x[1] and x[1] < c)


def addNode(A, B):
    return [A[0] + B[0], A[1] + B[1]]


def add(A, value, maps):
    maps[A[0]][A[1]] += value
    return maps


def value(A, maps):
    return maps[A[0]][A[1]]


def dpcopy(m):
    return copy.deepcopy(m)


def rotate90(group, end):
    group.remove(end)
    aa = list(map(lambda a: [a[0] - end[0], a[1] - end[1]], group))
    r90 = list(map(lambda a: [-a[1], a[0]], aa))
    aa = list(map(lambda a: [a[0] + end[0], a[1] + end[1]], aa))
    r90 = list(map(lambda a: [a[0] + end[0], a[1] + end[1]], r90))
    aa.append(end)
    end = r90[0]
    r90.reverse()
    aa += r90
    return aa, end


def findBlock(group):
    answer = []
    ans = 0
    for a in group:

        if ([a[0] - 1, a[1] - 1] in group) and ([a[0], a[1] - 1] in group) and (
                [a[0] - 1, a[1]] in group):
            ans += 1
    return ans


if __name__ == '__main__':
    move = [

        [1, 0],  # 3
        [0, -1],  # 2
        [-1, 0],  # 1
        [0, 1],  # 0

    ]

    # # print(rotate90([[0, 0], [1, 0]], [1, 0]))
    N = iinput()
    groupFinal = []
    for i in range(N):
        x, y, d, g = minput()
        start = [x, y]
        end = addNode(start, move[d])
        # print(start, end)
        group = [start, end]
        for _ in range(g):
            group, end = rotate90(group, end)
        for k in group:
            if k not in groupFinal:
                groupFinal.append(k)
    # print(*groupFinal, sep='\n')
    print(findBlock(groupFinal))
