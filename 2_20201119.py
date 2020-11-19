def solution(clothes):
    
    answer = 1
    spy={}
    for i in clothes:
        if i[1] in spy:
            spy[i[1]]+=1
        else:
             spy[i[1]]=1
    for i in spy:
        answer*=(spy[i]+1)
    answer-=1
    return answer
