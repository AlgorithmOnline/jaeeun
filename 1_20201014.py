N,K = map(int, input().split())
weight = [0]
gold =[0]
for _ in range(N):
    w, g= map(int, input().split())
    weight.append(w)
    gold.append(g)
    


dp=[[0  for i in range(K+1)] for k in range(N+1)]
for w in range(1, N+1):

    for i in range(1, K+1):
        if i>= weight[w]:
          #  print(weight[w],gold[w],dp[w]  )
                
                dp[w][i]=max(dp[w-1][i], dp[w-1][i-weight[w]]+gold[w])
                # 요게 w-1 인 이유 : 중복 제거
        else:
            
                dp[w][i]=dp[w-1][i]
print(dp[N][K])
