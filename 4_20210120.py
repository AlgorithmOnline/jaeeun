N = int(input())
for i in range(1, N+1):
    a,b = map(int, input().split())
    print("Case #"+str(i)+": "+str(a)+" + "+str(b)+" = "+str(a+b))
