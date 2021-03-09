def solution(distance, rocks, n):
    rocks.sort()

    rocks.append(distance)
    # 이분 탐색
    answer=0
    low, high = 1, distance
    visit=[]
    while low<=high:
        mid = round((low+high)/2)
        if mid in visit:
            break
        visit.append(mid)
        value =0
        before = 0
        
        for i in range(len(rocks)-1):
            if rocks[i]-before<mid:
                value +=1
            else:
                before = rocks[i]
                
        if value > n:
            high=mid
        else:
            answer=max(answer, mid)
            low=mid
            
        
    return answer
