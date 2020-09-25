A = int(input())
#answer= (A//15)*3  # 15 나머지는 제외
asnwer=0
tmp5=A//5
tmp3=A//3
flag =False
for t5 in range(tmp5,-1,-1):
    for t3 in range(tmp3,-1,-1):
        if 5* t5 + 3* t3 == A and not flag:
            flag=True
            print( t5+t3)
            break
            break
if not flag:
    print(-1)

