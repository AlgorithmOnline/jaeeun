def solution(n):
    dp=[0 for i in range(n+1)]
    dp[2]=3
    dp[4]=3*dp[2]+2
    for i in range(6,n+1,2):
        dp[i]=dp[i-2]*3+2
        for dd in range(2,i-2,2):
            dp[i]+=2*dp[dd]
        dp[i]%=    1000000007
        
        
    return dp[n]%    1000000007
