import collections
import sys
N = int(sys.stdin.readline())
dec= collections.deque([])
for _ in range(N):
    commands = list(sys.stdin.readline().split())
    if commands[0]=="push_back":
        dec.append(int(commands[1]))
        continue
    elif  commands[0]=="push_front":
        dec.appendleft(int(commands[1]))
        continue
    elif commands[0]=="pop_back":
        if len(dec)>0:
            print(dec.pop())
        else:
            print(-1)
        continue
    elif  commands[0]=="pop_front":
        if len(dec)>0:
            print(dec.popleft())
        else:
            print(-1)
        continue
    elif  commands[0]=="front":
        if len(dec)>0:
            print(dec[0])
            
        else:
            
            print(-1)
        continue
    elif  commands[0]=="back":
        if len(dec)>0:
            print(dec[-1])
        else:
            print(-1)
        continue
    
    elif  commands[0]=="size":
            print(len(dec))
            continue
    elif  commands[0]=="empty":
            print(int(len(dec)==0))
            continue
