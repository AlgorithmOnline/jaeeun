import sys
input = sys.stdin.readline
import itertools
L, C = map(int, input().split())
Os = ['a', 'e', 'i', 'o', 'u']
#Os=list(map(lambda k:ord(k), Os))
Cs = list(  input().split())
aa=[]
bb=[]
for c in Cs:
    if c in Os:
        aa.append(c)
    else:
        bb.append(c)
aas=[]
bbs=[]
for k in range(1,len(aa)+1):
    aas+=list(itertools.combinations(aa,k))
for k in range(2,len(bb)+1):
    bbs+=list(itertools.combinations(bb,k))
answer=[]
for k in aas:
    for j in bbs:
        if len(list(k+j))==L:
            answer.append(sorted(list(k+j)))
            
answer.sort()
for k in answer:
    print(''.join(k))
