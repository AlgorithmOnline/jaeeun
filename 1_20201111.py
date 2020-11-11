def findPrime(n):
    if n==1:
        return 0
    for i in range(2, n):
        if n%i ==0:
            return False
    return n
M  = int(input())
N = int(input())
nums = list(range(M,N+1))
nums = list(filter(findPrime, nums))
if sum(nums)!=0:
    print(sum(nums))
    print(min(nums))
else:
    print(-1)
