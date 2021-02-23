import collections
import copy
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
    r, c, k = minput()
    A = []
    r -= 1
    c -= 1


    def command(curA):
        if len(curA) >= len(curA[0]):
            return commandR(curA)
        else:
            return commandC(curA)


    def commandR(curA):
        newA = copy.deepcopy(curA)
        maxRow = 0
        for i in range(len(newA)):
            r = dict(collections.Counter(newA[i]))
            r.pop(0, None)
            arrR = list(sorted(r.items(), key=(lambda x: (x[1], x[0]))))
            newA[i] = []
            for k in arrR:
                if len(newA[i]) >= 100:
                    break
                else:
                    newA[i] += k
            maxRow = max(len(newA[i]), maxRow)
        for i in range(len(newA)):
            diff = maxRow - len(newA[i])
            newA[i] += [0 for ll in range(diff)]
        return newA


    def commandC(curA):
        newA = copy.deepcopy(curA)
        newA = transpose(newA)
        newA = commandR(newA)
        newA = transpose(newA)
        return newA


    for i in range(3):
        A.append(lisinput())

    will_visit = [{"sec": 1, "result": command(copy.deepcopy(A))}]
    visited = [copy.deepcopy(A)]
    answer = -1
    if len(A) > r and len(A[r]) > c and A[r][c] == k:
        answer = 0
    else:
        while will_visit:
            travel = will_visit.pop()
            if travel["sec"] > 100:
                answer = -1
                break
            if len(travel["result"]) > r and len(travel["result"][r]) > c and travel["result"][r][c] == k:
                answer = travel["sec"]
                break
            else:
                cR = command(travel["result"])
                if cR not in visited:
                    visited.append(cR)
                    will_visit.append({"sec": travel["sec"] + 1, "result": cR})
    print(answer)
