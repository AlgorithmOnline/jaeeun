import collections
def solution(A):
    if len(A)==0:
        return -1
    # write your code in Python 3.6
    answer=collections.Counter(A).most_common(1)[0]
    if answer[1]>(len(A)//2):
        return A.index(answer[0])
    else:
        return -1
