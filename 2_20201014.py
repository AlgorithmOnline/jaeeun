N = int(input())
index =1
second=0
while N !=0:
    
    if index>N:
        index=1
        continue
    else:
        N-=index
        index+=1
        second+=1
        continue
print(second)
