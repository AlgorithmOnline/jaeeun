def solution(A):
    # write your code in Python 3.6
    return len(set(list(map(lambda a:abs(a), A))))
