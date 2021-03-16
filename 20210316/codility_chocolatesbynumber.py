def solution(N, M):
    # write your code in Python 3.6
    lcd=(N*M)//gcd(N,M)
    return lcd//M
def gcd(a,b):
    if a==b:
        return a
    a,b=min(a,b),max(a,b)
    if b%a==0:
        return a
    return gcd(a,b%a)
