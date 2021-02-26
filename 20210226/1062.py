import collections
import sys

sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline
print = sys.stdout.write


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
    """
    알파벳 문제는 반드시 ord
    """


    def dfs(idx, cnt):
        global answer
        if cnt == k - 5:
            read_cnt = 0
            for word in words:
                for w in word:
                    if not learn[ord(w) - ord('a')]:
                        break
                    else:
                        read_cnt += 1
            answer = max(answer, read_cnt) if answer else read_cnt
            return

        for i in range(idx, 26):
            if not learn[i]:
                learn[i] = True
                dfs(i, cnt + 1)
                learn[i] = False


    answer = None
    n, k = minput()
    if k < 5 or k == 6:
        print(0 if k < 5 else n)

    else:
        words = [set(input().rstrop()) for _ in range(n)]
        learn = [False for k in range(26)]
        for c in ('a', 'c', 'i', 'n', 't'):
            learn[ord(c) - ord('a')] = True
    dfs(0, 0)
    print(answer)
