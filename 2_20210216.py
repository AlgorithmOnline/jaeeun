def solution(routes):
    routes.sort()
    answer = 1
    travel = routes[0]
    for i in range(1,len(routes)):
        travel2=routes[i]
        travel =[max(travel[0], travel2[0]), min(travel[1], travel2[1])]
        if travel[0]<=travel[1]:
            continue
        else:
            answer+=1
            travel =travel2
    
    return answer
