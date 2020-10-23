from collections import deque
def solution(maps):
    # bfs
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    n=len(maps[0
              ]) 
    m =len(maps) 
    visited=[]
    stack=deque([[0,0,1]])
    maxi=0
    while stack: 
        travel = stack.popleft()
        maps[travel[0]][travel[1]]=0
        if travel[0] ==m-1 and travel[1] ==n-1:
            return  travel[2]
        for g in dirs:
                may_be =[travel[0]+g[0],travel[1] +g[1],travel[2]+1]
                if 0<= may_be[0]<m and 0<= may_be[1]<n and  maps[may_be[0]][may_be[1]]==1:
                    maps[may_be[0]][may_be[1]]=0
                    
                    stack.append(may_be)

    return -1
