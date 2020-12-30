def findLen(xs,ys,xe,ye):
    return min(abs(xs-xe), abs(ys-ye))
x, y, w, h =map(int, input().split())
print(min(findLen(x,y,0,0),findLen(x,y,w,0),findLen(x,y,0,h),findLen(x,y,w,h) )   )
