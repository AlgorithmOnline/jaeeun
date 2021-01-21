# 백준 3052번
import collections
ans=[]
for i in range(10):
    a= int(input())% 42
    if a in ans:
        continue
    else:
        ans.append(a)
print(len(ans))
