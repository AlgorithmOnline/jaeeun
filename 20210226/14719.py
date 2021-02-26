import collections
import sys

sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline


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
    h, w = minput()
    ass = lisinput()
    history = [[0 for i in range(w)]]
    maxi = {"key": 0, "value": ass[0]}
    param = 0
    answer = 0
    middle = []
    minimiddle = float('inf')
    while param < w - 1:
        param = param + 1
        if ass[param] >= maxi["value"]:
            for i in range(maxi["key"] + 1, param):
                answer += maxi["value"] - ass[i]
                ass[i] = maxi["value"]
            maxi["value"] = ass[param]
            maxi["key"] = param
            middle = []
        else:
            if len(middle) == 0:
                middle.append(param)
                minimiddle = ass[param]
                # minimiddle = min(minimiddle, middle["value"])
            else:
                if ass[param] > minimiddle:
                    minimiddle = ass[param]
                    for kl in middle:
                        if minimiddle > ass[kl]:
                            answer += (minimiddle - ass[kl])
                            ass[kl] = minimiddle
                    middle.append(param)
                else:
                    middle.append(param)
                    minimiddle = ass[param]
                    # minimiddle = min(minimiddle, middle["value"])
    print(answer)

