# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math
def solution(N):
    # write your code in Python 3.6
    answer=0
    for i in range(1,int(math.sqrt(N)+1)):
        if i**2==N:
            answer+=1
            break
        elif i**2>N:
            break
        elif N%i==0:
            answer+=2
    return answer
