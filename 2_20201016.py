N = int(input())

dp=[100000000]*(N+5)
dp[0]=0
dp[1]=0
dp[2] =1
dp[3]=1
dp[4] =2
i = 4
while i<=N:
    if i % 3 ==0:
        dp[i]=min(dp[i],dp[i//3]+1,dp[i])
    elif i % 2 ==0:
        dp[i]=min(dp[i],dp[i//2]  +1 )
    
    dp[i]= min(dp[i-1]+1,dp[i])
        
    i+=1
print(dp[N])
