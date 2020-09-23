A = int(input())
for _ in range(A):
    H,W,N = map(int, input().split(" "))
    Nm =( N//H )+1
    Nn= (N%H) 
    if Nn ==0:
        Nn =H
        Nm-=1
    #print(Nm,Nn)
    print(Nn*100+Nm)
