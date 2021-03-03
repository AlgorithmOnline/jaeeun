def lisinput(): return list(map(int, input().split()))
import collections
import sys

sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline


#
# def print(a):
#     sys.stdout.write(str(a))


# print = sys.stdout.write


def iinput(): return int(input())


def lisinput(): return list(map(int, input().split()))


def dq(a):
    return collections.deque(a)


def minput(): return map(int, input().split())


def liinput(): return list(map(int, list(input().replace("\n", ""))))


def addNode(a, b):
    return [a[0] + b[0], a[1] + b[1]]


def innerRange(node, n):
    return 0 <= node[0] < n and 0 <= node[1] < n


def innerRange1(node, n, m):
    return 0 <= node[0] < n and 0 <= node[1] < m


def returnValue(graph, node):
    return graph[node[0]][node[1]]


def transpose(graph):
    return list(map(list, zip(*graph)))


def findParent(arr, n):
    if arr[n] == n:
        return n
    else:
        arr[n] = findParent(arr, arr[n])
        return arr[n]


def unionParent(arr, a, b):
    pa = findParent(arr, a)
    pb = findParent(arr, b)
    if pa < pb:
        arr[pb] = pa
    else:
        arr[pa] = pb
    return min(pa, pb)


if __name__ == '__main__':
    n = iinput()
    s = [list(map(int, input().split())) for i in range(n)]
    dp = [[0] * n for i in range(n)]
    for i in range(1, n):
        for j in range(n - i):
            x = j + i
            dp[j][x] = 2 ** 32
            for k in range(j, x):
                dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + s[j][0] * s[k][1] * s[x][1])
    print(dp[0][n - 1])

