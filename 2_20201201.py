T = int(input())
for i in range(T):
    start, end = map(int, input().split())
    between = end-start
    flag = 0
    num =1
    while between>0:
    
        if flag%2==1:
            between-=num
            num+=1
            flag+=1
        else:
            between-=num
            flag+=1
    print(flag)      


