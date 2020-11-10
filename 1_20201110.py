def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            summer = numbers[i]+ numbers[j]
            if summer not in answer:
                answer.append(summer)
    answer.sort()
    
    return answer

