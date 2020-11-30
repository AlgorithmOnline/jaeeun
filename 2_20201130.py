N = int(input())

ficc=[0] *(N+10)
ficc[1] = 1
def makeFic(N):
    if N ==1:
        return 1
    elif N == 0:
        return 0
    else:
        for i in range(2,N+1):
            ficc[i]=ficc[i-1]+ficc[i-2]
        return ficc[N]
                
print(makeFic(N))
