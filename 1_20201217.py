N = int(input())
maps = []
for i  in range(N):
    a=list(map(int, input().split()))
    maps.append(a)
# N = 9
# maps =[[0, 0, 0, 1, 1, 1, -1, -1, -1],
#  [0, 0, 0, 1, 1, 1, -1, -1, -1],
#  [0, 0, 0, 1, 1, 1, -1, -1, -1],
#  [1, 1, 1, 0, 0, 0, 0, 0, 0],
#  [1, 1, 1, 0, 0, 0, 0, 0, 0],
#  [1, 1, 1, 0, 0, 0, 0, 0, 0],
#  [0, 1, -1, 0, 1, -1, 0, 1, -1],
#  [0, -1, 1, 0, 1, -1, 0, 1, -1],
#  [0, 1, -1, 1, 0, -1, 0, 1, -1]]
cases ={1:0,0:0,-1:0, -99:0}

def divide_conquer(xs,ys,xe,ye):
    global cases
    control= maps[xs][ys] 
    case = control
    for x in range(xs,xe):
        for y in range(ys,ye):
            if maps[x][y] != control:
                case = -99
                break
    if case ==-99:
        Xparam = [xs, (xs*2+xe)//3,(xs+xe*2)//3,xe]
        Yparam = [ys,(ys*2+ye)//3,(ys+ye*2)//3,ye]
        for x in range(len(Xparam)-1):
            for y in range(len(Yparam)-1):
                divide_conquer(Xparam[x],Yparam[y],Xparam[x+1],Yparam[y+1]) 
    else:
      #  print(cases)
        cases[control]+=1
divide_conquer(0,0,N,N)
print(cases[-1])
print(cases[0])
print(cases[1])
