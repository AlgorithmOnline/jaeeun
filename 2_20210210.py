def solution(a, b):
    answer = 0
    b,a=max(a,b),min(a,b)
    
    return sum(list(range(a,b+1)))
