import collections
def solution(A):
    # write your code in Python 3.6
    max_a = max(A)
    min_a = min(A)
    len_a = len(A)
    if min_a !=1  or max_a!=len_a:
        return 0
        
    A = collections.Counter(A)
    #print(A)
    for i in range(1, max_a+1):
        if i not in A:
            return 0
    return 1
