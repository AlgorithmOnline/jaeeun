import collections
import sys

sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline


def print(a):
    sys.stdout.write(str(a))


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
    return


def move가로(travel):
    global answer
    newTravel = [0, 0, 0, 0]
    newTravel[3] = travel[3]
    newTravel[0] = travel[1]
    find = addNode(travel[1], [0, 1])
    newTravel[1] = find
    newTravel[2] = 0
    if returnValue(maps, find) == 0:
        if newTravel not in visited:
            if newTravel[1] == [n - 1, n - 1]:
                answer += 1
            else:
                will_visit.append(newTravel)

    return


def move세로(travel):
    global answer
    newTravel = [0, 0, 0, 0]
    newTravel[3] = travel[3]
    newTravel[0] = travel[1]
    find = addNode(travel[1], [1, 0])
    newTravel[1] = find
    newTravel[2] = 1
    if returnValue(maps, find) == 0:
        if newTravel not in visited:
            if newTravel[1] == [n - 1, n - 1]:
                answer += 1
            else:
                will_visit.append(newTravel)
    return


def move대각선(travel):
    global answer
    newTravel = [0, 0, 0, 0]
    newTravel[3] = travel[3]
    newTravel[0] = travel[1]
    find = addNode(travel[1], [1, 1])
    find1 = addNode(travel[1], [1, 0])
    find2 = addNode(travel[1], [0, 1])
    newTravel[1] = find
    newTravel[2] = 2
    if returnValue(maps, find) == 0 and returnValue(
            maps,
            find2) == 0 and returnValue(
        maps, find1) == 0:
        if newTravel not in visited:
            if newTravel[1] == [n - 1, n - 1]:
                answer += 1
            else:
                will_visit.append(newTravel)


if __name__ == '__main__':
    # BFS를
    n = iinput()
    # n-1, n-1
    maps = [[0] * n] * n
    answer = 0
    for i in range(n):
        maps[i] = lisinput()
    will_visit = [[[0, 0], [0, 1], 0, 0]]  # 파이프1, 파이프2, 방향, 횟수
    visited = []  # 파이프 끝만 모을 것
    while will_visit:
        travel = will_visit.pop()
        if travel[3] > (n - 1) * 2:
            break
        else:
            travel[3] += 1
            if travel[2] == 0:
                if innerRange1(travel[1], n, n - 1):
                    move가로(travel)
                    if innerRange(travel[0], n - 1) and innerRange(travel[1], n - 1):
                        move대각선(travel)
            elif travel[2] == 1:
                if innerRange1(travel[1], n - 1, n):
                    move세로(travel)
                    if innerRange(travel[0], n - 1) and innerRange(travel[1], n - 1):
                        move대각선(travel)
            elif travel[2] == 2:
                if innerRange1(travel[1], n, n - 1):
                    move가로(travel)
                if innerRange1(travel[1], n - 1, n):
                    move세로(travel)
                    if innerRange(travel[0], n - 1) and innerRange(travel[1], n - 1):
                        move대각선(travel)
    print(answer)
