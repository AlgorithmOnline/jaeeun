import collections
A=collections.deque(list(map(int, list(input()))))
if len(A)==1:
    A.appendleft(0)
originA=A
count=0
while True:
    
    sumA= sum(A)%10
    
    A=collections.deque([A[1],sumA])
    count+=1
    if A[0]==originA[0] and A[1] == originA[1]:
        print(count)
        break
        
    
    
    
