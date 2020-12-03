import sys
input = sys.stdin.readline
n = int(input())
a=[0]*10001
for i in range(n):
    test = int(input())
    a[test]+=1
for i in range(1,10001):
    if a[i]>0:
        for _ in range(a[i]):
            print(i)
