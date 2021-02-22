import collections
import itertools
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


if __name__ == '__main__':
    n, m = minput()
    maps = []
    homes = []
    chickens = []
    len_chicks = 0
    len_homes = 0
    logs = []
    for r in range(n):
        row = lisinput()
        for c in range(n):
            if row[c] == 1:  # 집
                homes.append([r, c])
            elif row[c] == 2:  # 치킨집
                chickens.append([r, c])
    len_chicks = len(chickens)
    len_homes = len(homes)
    # print(homes, chickens)
    for c in range(len_chicks):
        chick_homes = []
        for h in range(len_homes):
            chick_homes.append(abs(homes[h][0] - chickens[c][0]) + abs(homes[h][1] - chickens[c][1]))
        logs.append(chick_homes)
    answer = float('inf')
    chicken_managers = list(itertools.combinations(list(range(len_chicks)), m))

    for mm in chicken_managers:
        # 1,2,3
        cur_answer = 0
        for cur in range(len_homes):
            chicken_cost = float('inf')
            mm = list(mm)
            for j in mm:
                chicken_cost = min(chicken_cost, logs[j][cur])
            cur_answer += chicken_cost
        answer = min(answer, cur_answer)
    print(answer)

