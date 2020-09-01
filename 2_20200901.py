N = int(input())
home_works =[]
ans=0
days =0

for index in range(N):
    work  = list(map(int, input().split(" ")))
    if work[0]> days:
        days = work[0]
    work.append(index)
    home_works.append(work)
home_works=sorted(home_works, key = lambda i:( -i[1],i[0]))

planner =[]
for _ in range(days+1):
    planner.append(-1)
for work in home_works:
    for i in range(work[0],0, -1):
        #print(i)
        if planner[i] ==-1:
            planner[i] = work[2]
            ans+=work[1]
            break
        
print(ans)
