import collections
import sys
input = sys.stdin.readline
N = int(input())
a=[0]*N
for i in range(N):
    a[i]=int(input())

print(round(sum(a)/N)) # 산술 평균, 반올림에는 round 를 사용한다.
b= sorted(a)
print(b[N//2])
c= dict(collections.Counter(a))
c= sorted(c.items(), key=lambda d:(-d[1],d[0]))

#print(c)
if len(c)>1:
    if c[0][1]==c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
else:
    print(c[0][0])
print(b[-1]-b[0])
