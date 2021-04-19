import collections
def solution(s):
    s=list(s[2:-2].split("},{"))
    s=sorted(s, key=lambda a:len(a))
    answer =[]
    for i in s:
        i=list(map(int,i.split(",")))
        for k in i:
            if k not in answer:
                answer.append(k)
    return answer
