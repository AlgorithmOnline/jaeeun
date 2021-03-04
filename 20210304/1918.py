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
    a = input().replace("\n", "")
    stack = []  # 스택
    res = ''  # 출력
    for x in a:
        if x.isalpha():  # 피연산자인지 아닌지 확인
            res += x
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
        else:
            stack.append(x)
    while stack:
        res += stack.pop()
    print(res)
