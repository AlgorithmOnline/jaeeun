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


if __name__ == '__main__':
    n = iinput()
    ass = lisinput()
    # 자기 포함하게 해놓고 나중에 1빼기
    starts = [1 for k in range(n)]  # 해당 인덱스로 끝나는 증가수열 최대개수
    ends = [1 for k in range(n)]  # 해당 인덱스로 시작하는 감소수열 최대개수
    for k in range(1, n):
        for j in range(k):
            # 증가
            if ass[j] < ass[k] and starts[j] + 1 > starts[k]:
                starts[k] = starts[j] + 1
    for k in range(n - 2, 0, -1):
        for j in range(n - 1, k, -1):
            # 증가
            if ass[j] < ass[k] and ends[j] + 1 > ends[k]:
                ends[k] = ends[j] + 1
    answers = [starts[k] + ends[k] for k in range(n)]
    # print(starts)
    # print(ends)
    print(max(answers) - 1)

