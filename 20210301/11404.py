import collections
import sys

sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline



# print = sys.stdout.write


def iinput(): return int(input())


def lisinput(): return list(map(int, input().split()))


def dq(a):
    return collections.deque(a)


def minput(): return map(int, input().split())


def liinput(): return list(map(int, list(input().replace("\n", ""))))


def addNode(a, b):
    return [a[0] + b[0], a[1] + b[1]]


def returnValue(graph, node):
    return graph[node[0]][node[1]]


def transpose(graph):
    return list(map(list, zip(*graph)))


if __name__ == '__main__':
    n = iinput()
    m = iinput()
    maps = [[0 for k in range(n)] for l in range(n)]
    trees = collections.defaultdict(list)
    for k in range(m):
        a, b, c = minput()
        a -= 1
        b -= 1
        # maps[a][b] = min(maps[a][b], c)
        if maps[a][b] == 0:
            maps[a][b] = c
        else:
            maps[a][b] = min(maps[a][b], c)
        trees[a].append(b)
    visit = [True for k in range(n)]
    for travel in range(n):
        for s in range(n):
            if s == travel:
                continue
            for j in range(n):
                if s == j or j == travel or  s== travel:
                    continue
                if maps[s][travel] == 0 or maps[travel][j] == 0:
                    continue
                elif maps[s][j] == 0:
                    maps[s][j] = maps[s][travel] + maps[travel][j]
                elif maps[s][travel] + maps[travel][j] < maps[s][j]:
                    maps[s][j] = maps[s][travel] + maps[travel][j]

    for i in range(n):
        print(*maps[i])

