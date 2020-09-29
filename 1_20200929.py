N, M = map(int, input().split(" "))
L = N-M
# N 에서의 5 개수 찾기
N5 = N //5
M5  = M //5
L5 = L// 5

NN5=N//5
MM5  = M //5
LL5  = L //5

while NN5 //5 !=0:
    N5+= NN5//5
    NN5 //=5
while LL5 //5 !=0:
    L5+= LL5//5
    LL5 //=5    
    
while MM5 //5 !=0:
    M5+= MM5//5
    MM5 //=5
#print(N5, M5)   
N2 = N //2
M2  = M //2
L2 = L//2
NN2=N//2
MM2  = M //2
LL2 = L//2
while NN2 //2 !=0:
    N2+= NN2//2
    NN2 //=2
while MM2 //2 !=0:
    M2+= MM2//2
    MM2 //=2
while LL2 //2 !=0:
    L2+= LL2//2
    LL2 //=2
ans5=N5-M5-L5
ans2=N2-M2-L2
print(min(ans5, ans2))
ansTmp =list(str((5**ans5)*(2**ans2)))
ans=0
#print(ansTmp)

