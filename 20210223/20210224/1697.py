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
    n, k = minput()

    will_visit = collections.deque([[0, n]])
    will_node = [n]

    while will_visit:
        if n == k:
            print(0)
            break
        travel = will_visit.popleft()  # 56
        travel[0] += 1
        move1 = [travel[0], travel[1] + 1]
        move2 = [travel[0], travel[1] - 1]
        move3 = [travel[0], travel[1] << 1]
        if move1[1] == k or move2[1] == k or move3[1] == k:
            print(travel[0])
            break

        if move3[1] > 0 and move3[1] <= 100000 and move3[1] not in will_node:
            will_visit.append(move3)
            will_node.append(move3[1])
        if 0 <= move1[1] <= 100000 and move1[1] not in will_node:
            will_visit.append(move1)
            will_node.append(move1[1])
        if move2[1] >= 0 and move2[1] not in will_node:
            will_visit.append(move2)
            will_node.append(move2[1])
