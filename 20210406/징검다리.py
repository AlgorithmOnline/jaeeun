def solution(distance, rocks, n):
	rocks.sort()
    rocks.append(distance)
    left, right = 0, distance
    # 바위 사이 최소 거리 보다 거리가 작을 경우 돌 삭제
    # 거리가 클 경우 , 이 값 중 최솟값을 구해둔다.
    answer=0
    while left <= right:
    	# 이전 돌
        prev =0
        # 돌 거리 최솟값
        mins = float('inf')
        # 제거한 돌 개수
        removed_rocks = 0
        # 바위 사이 최소 거리
        mid = (left+right)//2
        # 각 돌을 돌면서 제거할 돌을 찾는다.
        for i in range(len(rocks)):
        	if rocks[i] - prev <mid:
            	remove_rocks+=1
            else:
            	mins = min(mins,rocks[i] - prev)
                prev = rocks[i]
       # 제거한 돌 개수가 기준보다 많다 = 바위 제거를 줄여야한다.
       # 바위 사이 최소 거리 기준을 낮춰라
       if removed_rocks> n: 
       		right = mid -1
       # 제거한 돌 개수가 기준보다 적다 = 더 많은 바위 제거가 필요
       else:
       		answer=mins
            left= mid +1
       return answer
