# dp[n]  = max(dp[n-2] , dp[n-3] +a[n-1] )+a[n] n>2

N = int(input())
a=[0]
for _ in range(N):
    a.append(int(input()))
dp=[0]*(N+15)
round_num=0
if N>0:
    round_num=1
    dp[1]=a[1]
    
if N>1:
    round_num=2
    dp[2]=a[1]+a[2]
if N>2:
    round_num=3
    dp[3]=max(a[1],a[2])+ a[3]

if N>3:
    while round_num<N:
        round_num+=1
        dp[round_num]= max(dp[round_num-2],dp[round_num-3]+ a[round_num-1])+ a[round_num]
print(dp[round_num])
