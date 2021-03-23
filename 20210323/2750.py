N=int(input())
nums =[]

for _ in range(N):
    nums.append(int(input()))


# insert sort
for i in range(1, len(nums)):
    while (i>0)&(nums[i]<nums[i-1]):
        nums[i], nums[i-1]=nums[i-1], nums[i]
        i-=1
for n in nums:
    print(n)

