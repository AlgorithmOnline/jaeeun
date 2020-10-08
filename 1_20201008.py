def solution(A):
    # write your code in Python 3.6
    import sys
 
    length=len(A)
    min_dif =sys.maxsize
    left=0
    right=sum(A[:])
    
    for i in range(length-1):
        left+=A[i]
        right -=A[i]
     #   print(left,right)
        min_dif= min(min_dif, abs(left-right))
        
        #min_dif=min(abs(sum(A[:i])-sum(A[i:])), min_dif)
    return min_dif
