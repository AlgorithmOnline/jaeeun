N  = int(input())
ass = [[]]*N
for i in range(N):
    ass[i] = list(map(int, input().split()))
    
ass.append(ass[0])
left=0
right =0
import math
for i in range(N):
    left+=ass[i][0]*ass[i+1][1]
    right +=ass[i][1]*ass[i+1][0]

print(((round(abs(left-right)/2*100)//10)/10))
