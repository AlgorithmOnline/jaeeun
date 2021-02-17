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
"""
"""

if __name__ == '__main__':
    # 데이터의 개수(n),   변경 횟수(m), 구간 합계산 횟수 (k)
    n, m, k = minput()
    # 전체 데이터 개수는 최대 1000000개
    arr = [0] * (n + 1)
    tree = [0] * (n + 1)


    # i번째 수까지의 누적 합을 계산하는 함수
    def prefix_sum(i):
        result = 0
        while i > 0:
            result += tree[i]
            # 0이 아닌 마지막 비트만큼 빼가면서 이동
            i -= (i & -i)
        return result


    # i번째 수를 dif만큼 더하는 함수
    def update(i, dif):
        while i <= n:
            tree[i] += dif
            i += (i & -i)


    # start 부터 end 까지 구간 합을 계산하는 함수
    def interval_sum(start, end):
        return prefix_sum(end) - prefix_sum(start - 1)


    for i in range(1, n + 1):
        x = iinput()
        arr[i] = x
        update(i, x)

    for i in range(m + k):
        a, b, c = minput()

        # 업데이트 연산의 경우
        if a == 1:
            update(b, c - arr[b])  # 바뀐 크기(dif) 만큼 적용
            arr[b] = c
        # 구간합 연산의 경우
        else:
            print(interval_sum(b, c))

