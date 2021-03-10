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


def innerRange(node, n):
    return 0 <= node[0] < n and 0 <= node[1] < n


def innerRange1(node, n, m):
    return 0 <= node[0] < n and 0 <= node[1] < m


def returnValue(graph, node):
    return graph[node[0]][node[1]]


def transpose(graph):
    return list(map(list, zip(*graph)))


if __name__ == '__main__':
    V = iinput()
    matrix = collections.defaultdict(list)
    for _ in range(V):
        path = lisinput()
        path_len = len(path)
        for i in range(1, path_len // 2):
            matrix[path[0]].append([path[2 * i - 1], path[2 * i]])
    result1 = [0 for k in range(V + 1)]


    def DFS(start, matrix, result):
        for e, d in matrix[start]:
            if result[e] == 0:
                result[e] = result[start] + d
                DFS(e, matrix, result)


    DFS(1, matrix, result1)
    result1[1] = 0  # 루트 노드가 정해있지 않아 양방향으로 입력을 박기 때문
    tmpmax = 0  # 최댓값 구하기
    index = 0  # 최장 경로 노드
    for i in range(len(result1)):
        if tmpmax < result1[i]:
            tmpmax = result1[i]
            index = i
    # 최장 경로 노드에서 다시 DFS 를 통해 트리 지름 구하기
    result2 = [0 for k in range(V + 1)]
    DFS(index, matrix, result2)
    result2[index] = 0
    print(max(result2))
