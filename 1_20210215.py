import collections
import copy
import heapq
import math
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def hpop(ALIST):
    heapq.heapppop(ALIST)


def log2(i):
    return math.log(i, 2)


def iinput(): return int(input())


def lisinput(): return list(map(int, input().split()))


def minput(): return map(int, input().split())


def liinput(): return list(map(int, list(input())))


def dq(): return collections.deque([])


def popl(a): return a.popleft()


def appendl(a, b):
    a.appendleft(b)
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


def addNode(A, B):
    return [A[0] + B[0], A[1] + B[1]]


def add(A, value, maps):
    maps[A[0]][A[1]] += value
    return maps


def value(A, maps):
    return maps[A[0]][A[1]]


def dpcopy(m):
    return copy.deepcopy(m)


def sec_to_time(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    ans = []
    if h < 10:
        ans.append(0)
    ans.append(h)
    ans.append(':')
    if m < 10:
        ans.append(0)
    ans.append(m)
    ans.append(':')
    if s < 10:
        ans.append(0)
    ans.append(s)
    string = ''.join(list(map(str, ans)))
    return string


def time_to_sec(play_time):
    h, m, s = map(int, play_time.split(":"))
    sec = 3600 * h + 60 * m + s
    return sec


def split2times(log):
    s, e = log.split("-")
    return (time_to_sec(s), time_to_sec(e))

    # 항상 시간은   min(끝난 시간들) - max(시작 시간들 )


if __name__ == '__main__':
    n, m = minput()
    nums = []
    for i in range(n):
        nums.append(iinput())
    if log2(n) % 1 != 0:
        ideal = 2 ** ((log2(n) // 1) + 1)
        remain = int(ideal - n)
        nums = nums + [nums[-1] for i in range(remain)]
        n = int(ideal)
    tornements = [list(zip(nums, nums))]
    trees = [0]
    while len(tornements[-1]) != 1:
        cur_torn = tornements[-1]
        wins = []
        for i in range(0, len(cur_torn), 2):
            if len(cur_torn) > i + 1:
                wins.append((min(cur_torn[i][0], cur_torn[i + 1][0]), max(cur_torn[i][1], cur_torn[i + 1][1])))
        if len(cur_torn) % 2 == 1:
            wins.append(cur_torn[-1])
        tornements.append(wins)
    for k in range(len(tornements) - 1, -1, -1):
        trees += tornements[k]


    # print(trees)

    def findNodeAndAnswer(s, e, cs, ce, node):
        global answer
        if cs == s and e == ce:
            answer[0] = min(answer[0], trees[node][0])
            answer[1] = max(answer[1], trees[node][1])
            return
        elif cs > e or ce < s:
            return
        else:
            mid = (cs + ce) // 2
            if s <= mid:
                if mid <= e:
                    findNodeAndAnswer(s, mid, cs, mid, 2 * node)
                else:
                    findNodeAndAnswer(s, e, cs, mid, 2 * node)
            if mid + 1 <= e:
                if mid + 1 >= s:
                    findNodeAndAnswer(mid + 1, e, mid + 1, ce, 2 * node + 1)
                else:
                    findNodeAndAnswer(s, e, mid + 1, ce, 2 * node + 1)


    for k in range(m):
        answer = [float('inf'), -float('inf')]
        gg, ggg = minput()
        findNodeAndAnswer(gg, ggg, 1, n, 1)
        print(*answer)
