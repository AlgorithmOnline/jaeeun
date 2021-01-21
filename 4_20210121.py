# 백준 2577번
import collections
A = int(input())
B= int(input())
C= int(input())

ans=dict(collections.Counter(str(A*B*C)))
for i in range(10):
    if str(i) not in ans:
        print(0)
    else:
        print(ans[str(i)])



