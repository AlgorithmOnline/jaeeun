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


def returnValue(graph, node):
    return graph[node[0]][node[1]]


def transpose(graph):
    return list(map(list, zip(*graph)))


def make_table():
    length = len(p)
    table = [0] * len(p)
    j = 0
    for i in range(1, length):
        while j > 0 and p[i] != p[j]:
            j = table[j - 1]
        if p[i] == p[j]:
            j += 1
            table[i] = j
    return table


def kmp():
    table = make_table()
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j - 1]
        if s[i] == p[j]:
            if j == len(p) - 1:
                return True
            else:
                j += 1
    return False


if __name__ == '__main__':
    s = input().replace('\n', '')
    p = input().replace('\n', '')
    print(1 if kmp() else 0)
