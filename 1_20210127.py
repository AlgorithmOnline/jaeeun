import itertools
N, M = map(int, input().split())
ass=list(filter(lambda k: k<=M, list(map(int, input().split()))))
q=list(itertools.combinations(ass,3))
w=list(map(lambda a:sum(a), q))
d=list(filter(lambda a :a<=M,w))
print(max(d))

