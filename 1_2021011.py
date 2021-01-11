import sys

INF = sys.maxsize
input = sys.stdin.readline

n = int(input())
m = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                a[i][j] = 1
            if a[i][k] and a[k][j]:
                a[i][j] = 1

d = list(map(int, input().split()))
for i in range(len(d)-1):
    if a[d[i]-1][d[i+1]-1] != 1:
        print("NO")
        sys.exit()
print("YES")
