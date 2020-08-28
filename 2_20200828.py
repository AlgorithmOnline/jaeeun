# 668ms
# 백준 1018 체스판 다시 칠하기
import itertools


N, S = map(int, input().split(" "))
ns = list(map(int, input().split(" ")))
ans = 0

for g in range(1,N+1):
    nCr = list(itertools.combinations(ns,g))
    for param  in nCr:
        if sum(param) == int(S):
            ans+=1
    
print(ans)
