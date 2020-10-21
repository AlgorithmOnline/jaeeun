import collections
def solution(A):
    # write your code in Python 3.6
    max_a = max(A)
    min_a =  min(A)
    if max_a<=0:
        return 1
    elif min_a>1:
        return 1
    else:
       counter_a = dict(collections.Counter(A))
   #    print(counter_a)
       for i in range(1, max_a+1):
           if i not in counter_a:
               return i
    return max_a+1


