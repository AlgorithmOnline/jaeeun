# 백준 1546번
N=int(input())
ans=list(map(int, input().split()))
maxi=max(ans)
ans=list(map(lambda a:round(a*100/maxi), ans))
print(sum(ans)/N)
