import collections
def solution(clothes):
    new=[]
    answer = 1
    for i in clothes:
        new.append(i[1])
    an=collections.Counter()
    an.update(new)

    for i in an.values():
        answer*=(i+1)
    answer-=1
    
    return answer
