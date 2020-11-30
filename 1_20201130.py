N = int(input())
ans=[1]*(N+1)
def fac(N):
    for i in range(1,N+1):
       # print(ans)
        ans[i] = ans[i-1]*i
    return ans[N]
print(fac(N))
