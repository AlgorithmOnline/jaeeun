xH=[]
yH=[]
for _ in range(3):
    x,y = map(int, input().split())
    if x in xH:
        xH.remove(x)
    else:
        xH.append(x)
    if y in yH:
        yH.remove(y)
    else:
        yH.append(y)
print(xH[0], yH[0])
