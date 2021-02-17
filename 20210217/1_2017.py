import collections
import copy
import copy
import sys
sys.setrecursionlimit(10**9)


def iinput(): return int(input())


def lisinput(): return list(map(int, input().split()))


def minput(): return map(int, input().split())


def liinput(): return list(map(int, list(input())))


def dq(): return collections.deque([])


def popl(a): return a.popleft()


def appendl(a, b):
    a.appendleft(b)
    return a


move = [
    [-1, 0],  # 왼
    [0, -1],  # 아래
    [1, 0],  # 오른쪽
    [0, 1],  # 위
]


def in_r(x, N):
    return (0 <= x[0] and x[0] < N and 0 <= x[1] and x[1] < N)


def in_rc(x, r, c):
    return (0 <= x[0] and x[0] < r and 0 <= x[1] and x[1] < c)


def addNode(A, B):
    return [A[0] + B[0], A[1] + B[1]]


def add(A, value, maps):
    maps[A[0]][A[1]] += value
    return maps


def value(A, maps):
    return maps[A[0]][A[1]]


def dpcopy(m):
    return copy.deepcopy(m)


def sec_to_time(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    ans = []
    if h < 10:
        ans.append(0)
    ans.append(h)
    ans.append(':')
    if m < 10:
        ans.append(0)
    ans.append(m)
    ans.append(':')
    if s < 10:
        ans.append(0)
    ans.append(s)
    string = ''.join(list(map(str, ans)))
    return string


def time_to_sec(play_time):
    h, m, s = map(int, play_time.split(":"))
    sec = 3600 * h + 60 * m + s
    return sec


def split2times(log):
    s, e = log.split("-")
    return (time_to_sec(s), time_to_sec(e))


# 항상 시간은   min(끝난 시간들) - max(시작 시간들 )


if __name__ == '__main__':
    id = 0  # 정점의 아이디


    def minput():
        return map(int, input().split())


    d = {}
    finished = []
    v, e = minput()
    maps = collections.defaultdict(list)

    for i in range(e):
        ns, ne = minput()
        maps[ns].append(ne)
    finished = [False for i in range(v + 2)]
    answers = []
    rAnswer = {}
    stack = []

    d = [0 for _ in range(v + 2)]

    id = 00


    def dfs(x):
        global id
        id += 1
        d[x] = id
        parent = d[x]
        stack.append(x)
        for y in maps[x]:
            if d[y] == 0:
                parent = min(parent, dfs(y))
            elif not finished[y]:
                parent = min(d[y], parent)

        if d[x] == parent:
            scc = []
            while stack:
                t = stack.pop()
                scc.append(t)

                finished[t] = True
                if t == x:
                    break
            if len(scc) > 0:
                rAnswer[min(scc)] = scc
                answers.append(scc)
        return parent


    for ii in range(1, v + 1):
        if d[ii] == 0:
            dfs(ii)
    print(len(answers))
    rKey = list(rAnswer.keys())

    rKey.sort()
    for w in rKey:
        rAnswer[w].sort()
        print(*rAnswer[w], -1)
    # for w in answers:
    #     w.sort()
    #     print(*w, -1)

