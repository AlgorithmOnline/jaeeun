# K=2
# names=[3, 1]
# turns=[-1, 1]
# wheels={1: collections.deque([1, 0, 1, 0, 1, 1, 1, 1]),
#  2: collections.deque([0, 1, 1, 1, 1, 1, 0, 1]),
#  3: collections.deque([1, 1, 0, 0, 1, 1, 1, 0]),
#  4: collections.deque([0, 0, 0, 0, 0, 0, 1, 0])}


import collections

wheels = {}
for i in range(1, 5):
    wheels[i] = collections.deque(list(map(int, input())))
names = []
turns = []
commands = ["both", "left", "right"]
K = int(input())
for i in range(K):
    name, turn = map(int, list(input().split()))
    names.append(name)
    turns.append(turn)


def left(n, t):
    #print(n, "번째 수레", t, "방향 회전")
    if wheels[n - 1][2] + wheels[n][6] == 1:
        nearTurn(n - 1, -t, "left")


def right(n, t):
    #print(n, "번째 수레", t, "방향 회전")
    if wheels[n][2] + wheels[n + 1][6] == 1:
        nearTurn(n + 1, -t, "right")


def nearTurn(n, t, command):
    if 1 < n < 4:
        if command == "both" or command == "left":
            left(n, t)
        if command == "both" or command == "right":
            right(n, t)
    elif n == 1:
        if command == "both" or command == "right":
            right(n, t)
    elif n == 4:
        if command == "both" or command == "left":
            left(n, t)
    else:
        pass
    wheels[n].rotate(t)  # turn

    #print(wheels)


for i in range(K):
    n, t = names[i], turns[i]
    #print(i, "번째 명령")
    nearTurn(n, t, "both")
    #print("--" * 8)
answer = 0
for i in range(1, 5):
    answer += wheels[i][0] * (2 ** (i - 1))
print(answer)
