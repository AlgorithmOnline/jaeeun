ass=[[]]*3
figure=0
def findgrad(dx,dy):
    if dx!=0:
        figure = dy/dx
    else:
        figure = float('inf')
    return figure
for i in range(3):
    ass[i] = list(map(int, input().split()))
S2=(ass[1][0]-ass[0][0])*(ass[2][1]-ass[0][1])-(ass[1][1]-ass[0][1])*(ass[2][0]-ass[0][0])

if S2>0:
    print(1)
elif S2 ==0:
    print(0)
else:
    print(-1)
    
