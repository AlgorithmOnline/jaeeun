def findPrime(n):
    if n==1:
        return 0
    for i in range(2, n):
        if n%i ==0:
            return 0
    return 1
N  = int(input())
nums = list(map(int,input().split()))
nums = list(map(findPrime, nums))
print(sum(nums))
