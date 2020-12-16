import collections
N = int(input())
a= collections.deque(list(range(1, N+1)))
while len(a)>1:
    a.popleft()
    a.rotate(-1)
    #print(a)
print(a[0])
