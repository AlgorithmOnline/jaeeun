import itertools
import collections
n = int(input())
a=list(map(int, input().split()))
operator = ['+','-','*','%']
operatorNum = list(map(int, input().split()))
operatorReal = []
for i in range(len(operatorNum)):
    operatorReal+=[operator[i]]*operatorNum[i]
opCombi = collections.deque(list(set(itertools.permutations(operatorReal,sum(operatorNum)))))
history=[]
while opCombi:
    travel = opCombi.popleft()
    aa=a[0]
   # print(a,aa, travel)
    for i in range(len(travel)):
            if travel[i]=='+':
                aa+=a[i+1]
            elif travel[i]=='-':
                aa-=a[i+1]
            elif travel[i]=='*':
                aa*=a[i+1]
            else:
                if aa<0:
                    aa=abs(aa)//a[i+1]
                    aa*=(-1)
                else:
                    aa//=a[i+1]
    if aa not in history:
        history.append(aa)
history.sort()
print(history[-1])
print(history[0])
