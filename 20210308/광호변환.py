import copy
import collections


def findPpQq(st):
    status = 0
    orange = collections.Counter(st)
    if len(orange) == 0:
        return 0
    elif len(orange) == 1:
        return 0
    elif orange[")"] != orange["("]:
        return 0
    else:
        status = 1
        stack = []
        for k in st:
            if k == "(":
                stack.append(-1)
            elif k == ")":
                if len(stack) == 0:
                    return 1
                else:
                    stack.pop()
    return 2


def dividedToUV(v):
    if len(v) == 0:
        return v
    else:
        u = collections.deque([])
        u.append(v.popleft())
    while findPpQq(u) == 0:
        u.append(v.popleft())
    if findPpQq(u) == 2:
        u += dividedToUV(copy.deepcopy(v))
        return u
    elif findPpQq(u) == 1:
        newSt = ["("]
        newSt += dividedToUV(copy.deepcopy(v))
        newSt.append(")")
        for kkkk in range(1, len(u) - 1):
            if u[kkkk] == "(":
                newSt.append(")")
            elif u[kkkk] == ")":
                newSt.append("(")
        return newSt


def solution(p):
    status = findPpQq(list(p))
    if len(list(p)) == 0 or status == 2:
        return p
    answer=dividedToUV(collections.deque(list(p)))
    anss= ''.join(list(answer))
    return anss
