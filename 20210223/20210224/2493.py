import collections
import sys

sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline


def iinput(): return int(input())


def lisinput(): return list(map(int, input().split()))


def dq(a):
    return collections.deque(a)


def minput(): return map(int, input().split())


def liinput(): return list(map(int, list(input())))


def addNode(a, b):
    return [a[0] + b[0], a[1] + b[1]]


def returnValue(graph, node):
    return graph[node[0]][node[1]]


def transpose(graph):
    return list(map(list, zip(*graph)))


if __name__ == '__main__':
    N = iinput()
    ass = lisinput()
    answer = [0 for i in range(N)]
    remain = collections.deque([[ass[N - 1], N - 1]])
    for k in range(N - 1, -1, -1):
        while len(remain) >= 1 and ass[k] >= remain[0][0]:  # value, index
            tup = remain.popleft()
            answer[tup[1]] = k + 1
        remain.appendleft([ass[k], k])
    print(*answer, sep=' ')
