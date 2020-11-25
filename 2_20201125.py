T=int(input())
semo=[]
for i in range(T):
    semo.append(list(map(int,input().split())))
semo=collections.deque(semo)
def fire(semo):
    if len(semo)==1:
        print(max(semo[0]))
        return
    else:
        travel=semo.popleft()
        
        for i in range(len(semo[0])):
            if i==0:
                semo[0][i]+=travel[0]
            elif i ==len(semo[0])-1:
                semo[0][i]+=travel[i-1]
            else:
                semo[0][i]+=max(travel[i-1], travel[i])
        return fire(semo)
fire(semo)    
