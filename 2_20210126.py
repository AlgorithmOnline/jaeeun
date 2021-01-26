# 제일 높은 자리 -> 최빈 ( 높은 곳부터 )
import collections
N = int(input())
ggs=[]
ss=collections.defaultdict(int)
for _ in range(N):
    a=input()
    for i in range(len(a)):
        ss[a[i]]+=(10**(len(a)-i-1))
    ggs.append(a)
ss=list(sorted(ss.items(), key=lambda f:-f[1]))
answer=0
for i in range(9,9-len(ss),-1):
    answer+=ss[9-i][1]*i
print(answer)
