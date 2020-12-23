import collections
T= int(input())

for _ in range(T):
    originD="D"
    ans=True
    ps=list(input())
    n= int(input())
    tmp = input()
    arr= collections.deque(list(tmp[1:-1].split(",")))
    #print(arr)
    for p in ps:
        if p =="R":
            if originD=="D":
                originD="RD"
            else:
                originD="D"
        elif p =="D":
            if len(arr)==0:
                ans=False
                print("error")
                break
            if originD=="D" :
                if arr.popleft()=="":
                    ans=False
                    print("error")
                    break
            else:
                 if arr.pop()=="":
                    ans=False
                    print("error")
                    break               
                
                

            
    if ans:
        print("[", end="")
        
        if originD=="RD":
            arr=list(arr)[::-1]
            print(*arr,sep=",", end="")
        
        else:
            print(*arr,sep=",", end="")
        print("]")
