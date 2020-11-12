def solution(arr):
    before = arr[0]
    answer = [before]
    for a in range(1,len(arr)):
        if arr[a]==before:
            continue
        else:
            before= arr[a]
            answer.append(before)
            
    
    
    return answer
