T = int(input())
for _ in range(T):
        k = int(input())
        n = int(input())
        
        
        if n ==1:
            print(1)
        else:
            floor=list(range(1,n+1))
            ans=0
            
            for i in range(k): # 층수 
                floor_new= [1]
                for h in range(2,n+1):
                    tmp=floor[: h]
                   # print("tmp",tmp)
                    a=sum(tmp)
                    floor_new.append(a)
                floor= floor_new
               # print(floor)
            print(floor_new[-1])

