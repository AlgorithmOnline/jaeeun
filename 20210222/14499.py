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


if __name__ == '__main__':
    dice = [dq([2, 1, 5, 6]), dq([4, 3])]
    diceNums = [-1, 0, 0, 0, 0, 0, 0]
    maps = []
    n, m, x, y, k = minput()
    for kd in range(n):
        maps.append(lisinput())
    commands = lisinput()
    curNode = [x, y]


    def returnTop():
        return diceNums[dice[0][1]]


    def returnDown():
        return diceNums[dice[0][-1]]


    def execute(node, n, m):
        if node[0] >= n or node[0] < 0 or node[1] >= m or node[1] < 0:
            answer = None
            return False
        else:
            value = maps[node[0]][node[1]]
            if value == 0:
                maps[node[0]][node[1]] = diceNums[dice[0][-1]]
            else:
                diceNums[dice[0][-1]] = maps[node[0]][node[1]]
                maps[node[0]][node[1]] = 0
            answer = returnTop()
            print(answer)


    def curNodeMove(node, num):
        if num == 1:
            return addNode(node, [0, 1])
        elif num == 2:
            return addNode(node, [0, -1])
        elif num == 3:
            return addNode(node, [-1, 0])
        elif num == 4:
            return addNode(node, [1, 0])


    def turn(num):
        if num == 1:  # 동
            dice[0][-1], dice[0][1], dice[1][0], dice[1][1] = dice[1][1], dice[1][0], dice[0][-1], dice[0][1]
        elif num == 2:  # 서
            dice[1][1], dice[1][0], dice[0][-1], dice[0][1] = dice[0][-1], dice[0][1], dice[1][0], dice[1][1]
        elif num == 3:  # 북
            dice[0].rotate(-1)
        elif num == 4:  # 남
            dice[0].rotate(1)
        return


    for c in range(k):
        newNode = curNodeMove(curNode, commands[c])
        if newNode[0] >= n or newNode[0] < 0 or newNode[1] >= m or newNode[1] < 0:
            pass
        else:
            curNode = newNode
            turn(commands[c])
            execute(curNode, n, m)

