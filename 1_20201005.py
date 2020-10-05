import collections
N = int(input())
nmaps = list(map(int, input().split()))
nmaps = dict(collections.Counter(nmaps))
M = int(input())
mmaps =  list(map(int, input().split()))
for m in mmaps:
    if m in nmaps:
        print(nmaps[m], end= ' ')
    else:
        print(0, end =' ')
