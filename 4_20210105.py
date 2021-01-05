import collections
import sys
input = sys.stdin.readline
N = int(input())
a=collections.deque([])
for _ in range(N):
    
    command =list(input().split())
    if len(command)==2:
        num = int(command[1])
    command = command[0]
    if command =="push":
        a.append(num)
    elif command =="pop":
        if len(a)>0:
                print(a.popleft())
        else:
            print(-1)
    elif command =="size":
        print(len(a))
    elif command =="empty":
        print(int(len(a)==0))
    elif command =="front":
        if len(a)>0:
                print(a[0])
        else:
            print(-1)
    elif command =="back":
        if len(a)>0:
                print(a[-1])
        else:
            print(-1)
