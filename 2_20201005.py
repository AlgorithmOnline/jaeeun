N = int(input())
origin = list(map(int, input().split()))
M = int(input())
test = list(map(int, input().split()))
for t in test:
    if t in origin :
        print(1)
    else:
        print(0)
