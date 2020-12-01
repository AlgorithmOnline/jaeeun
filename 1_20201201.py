N, threeBack, limit =map(int, input().split())
answer=[]
num=0
for i in range(N):
    a= list(map(int, input().split()))
  
    flag = True
    for i in a:
        if i<limit:
            flag = False
            break
    if flag:
        ans=sum(a)
        if ans >=threeBack:
            answer+=a
            num+=1
print(num)
print(*answer)
            
