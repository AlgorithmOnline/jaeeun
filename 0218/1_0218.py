import copy
import sys

sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline


def iinput(): return int(input())


def lisinput(): return list(map(int, input().split()))


def minput(): return map(int, input().split())


def liinput(): return list(map(int, list(input())))


if __name__ == '__main__':
    n, k = map(int, input().split())
    consent = [False for b in range(k + 1)]
    ass = list(map(int, input().split()))
    history = [[0 for kj in range(k + 1)]]  # row 가 횟수 , col 이 물품
    for kindex in range(k):
        if kindex == 0:
            history[kindex][ass[kindex]] = 1
        else:
            row = copy.deepcopy(history[kindex - 1])
            row[ass[kindex]] += 1
            history.append(row)
    answer = 0
    for i in range(k):
        if i < n:
            consent[ass[i]] = True
        elif consent[ass[i]]:
            continue
        else:
            answer += 1
            next_window = n + ass[i] - 1
            if n + ass[i] - 1 >= k:
                next_window = k
            import heapq

            dd = []
            for kd in range(k):
                if consent[kd]:
                    heapq.heappush(dd, (history[next_window][kd] - history[i][kd], kd))
            if len(dd) == 0:
                break
            lotto = heapq.heappop(dd)
            consent[lotto[1]] = False
            consent[ass[i]] = True
    print(answer)

