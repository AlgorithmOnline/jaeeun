import collections
import copy

import sys

input = sys.stdin.readline


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
    test = []
    answers = [0 for i in range(m)]
    finish = [False for i in range(m)]
    nums = lisinput()
    dp = [0 for i2 in range(n + 1)]
    a = nums[0]
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + nums[i - 1]


    def fire(s, e):
        if s == e:
            return nums[s - 1]
        else:
            return dp[e] - dp[s - 1]


    for i in range(m):
        a1, b1 = minput()
        print(fire(a1, b1))

