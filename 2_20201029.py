N, K =map(int, input().split())
coins=[]
for i in range(N):
    coin =int(input())
    if coin <K:
        coins.append(coin)
    elif coin == K:
        
        print(1)
        break
    else:
        pass
answer=0
while K!=0:
    target = coins.pop()
    while target>K:
        target = coins.pop()
    share = K//target
    answer+=share
    K-=share*target
print(answer)    
