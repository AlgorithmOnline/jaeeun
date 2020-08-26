import sys
N = int(sys.stdin.readline())
for i  in range(N):
    string =sys.stdin.readline()
    answer =0
    flag = True
    for st in string:
        if answer <0:
            print("NO")
            flag =False
            break
        elif st == "(":
            answer+=1
        elif st ==")":
            answer-=1
    if flag and answer==0:
        print("YES")
    elif flag and answer!=0:
        print("NO")
