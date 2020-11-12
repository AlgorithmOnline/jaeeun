def solution(n):
    fire=[0,1]
    m=2
    if n<2:
        return fire[n]
    while n>=m:
        fire.append((fire[m-1]+fire[m-2])%1234567)
        m+=1
    answer = fire[-1]
    return answer
