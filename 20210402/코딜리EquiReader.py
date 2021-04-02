import collections
def solution(A):
    answer=0
    # write your code in Python 3.6
    ans=collections.Counter(A).most_common(1)[0]
    if ans[1]<=len(A)//2:
        return 0
    comons=[0]*len(A)
    for i in range(len(A)):
        if i==0 and  A[i] == ans[0]:
            comons[0]=1
        elif A[i] == ans[0]:
            comons[i]=comons[i-1]+1
        else:
            comons[i]=comons[i-1]
    for i in range(len(A)-1):
        before=comons[i]
        after=comons[len(A)-1]-before
        afterLen= len(A)-i-1
        beforeLen=i+1
        if before<= beforeLen//2 or after<=afterLen//2:
            continue
        else:
            answer+=1
    
    return answer
