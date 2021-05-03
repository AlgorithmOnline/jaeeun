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
    return


if __name__ == '__main__':
    v, e = minput()
    arr = [f for f in range(v)]
    vvvv = []
    parent = []
    answer = 0
    for _ in range(e):
        a, b, c = minput()
        a -= 1
        b -= 1
        vvvv.append([c, a, b])
        # arr[b] = a
    vvvv = sorted(vvvv, key=lambda x: x[0])
    for i in vvvv:
        if findParent(arr, i[1]) != findParent(arr, i[2]):
            unionParent(arr, i[1], i[2])
            answer += i[0]
    # print(arr)
    print(answer)
