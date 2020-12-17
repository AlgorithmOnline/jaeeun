N = int(input())
maps = []
for i  in range(N):
    a=list(input())
    maps.append(a)
# N =8
# maps = [['1', '1', '1', '1', '0', '0', '0', '0'],
#  ['1', '1', '1', '1', '0', '0', '0', '0'],
#  ['0', '0', '0', '1', '1', '1', '0', '0'],
#  ['0', '0', '0', '1', '1', '1', '0', '0'],
#  ['1', '1', '1', '1', '0', '0', '0', '0'],
#  ['1', '1', '1', '1', '0', '0', '0', '0'],
#  ['1', '1', '1', '1', '0', '0', '1', '1'],
#  ['1', '1', '1', '1', '0', '0', '1', '1']]
def divide_conquer(xs,ys,xe,ye):
    
    control= maps[xs][ys] 
    case = control
    for x in range(xs,xe):
        for y in range(ys,ye):
            if maps[x][y] != control:
                case = 2
                break
    if case ==2:
        #print(xs, ys,(xs+xe)//2,(ys+ye)//2 )
        elem1= divide_conquer(xs,ys,(xs+xe)//2,(ys+ye)//2) 
        elem2= divide_conquer(xs,(ys+ye)//2,(xs+xe)//2,ye) 
        elem3= divide_conquer((xs+xe)//2,ys,xe,(ys+ye)//2) 
        elem4= divide_conquer((xs+xe)//2,(ys+ye)//2,xe,ye) 
        return "("+elem1+elem2+elem3+elem4+")"
    else:
        return str(control)
print(divide_conquer(0,0,N,N))
