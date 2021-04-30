def solution(gems):
    n = len(set(gems))
    answer = [0, len(gems) - 1]
    start = 0
    end = 0
    dic1 = {gems[0]: 1}
    while start < len(gems) and end < len(gems):
        if len(dic1) == n:
            if answer[1] - answer[0] > end - start:
                answer[0] = start
                answer[1] = end
            if dic1[gems[start]] == 1:
                del dic1[gems[start]]
            else:
                dic1[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            else:
                if dic1.get(gems[end]) is None:
                    dic1[gems[end]] = 1
                else:
                    dic1[gems[end]] += 1
    answer[0] += 1
    answer[1] += 1
    return answer
