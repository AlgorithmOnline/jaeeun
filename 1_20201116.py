def solution(prices):
    # 테스트 케이스는 10000개 => n^2 까지 가능하다는 뜻
    answer=[0] * len(prices)
    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] >prices[j]:
                break
            else:
                answer[i] +=1

    return answer
