
def solution(dirs):
    answer = 0
    visited=[]
    start=[0,0]

    for d in dirs:
        if d=='U':
            d=[0,1]
        elif d=='D':
            d=[0,-1]
        elif d=='R':
            d=[1,0]
        elif d=='L':
            d=[-1,0]
        end=[start[0]+d[0],start[1]+d[1]]    
        if -5<=end[0]<=5 and  -5<=end[1]<=5:
            if [start, end] not in visited and  [end, start] not in visited:
                visited.append([start,end])
            start=end
    return len(visited)


