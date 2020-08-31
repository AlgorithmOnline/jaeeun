global total 
def solve(A,last,not_param):
    global total 
    if len(last)==1:
        b= last[0]
        if total < b**2:
            total = b**2
            solve(A,A[0:2],2)
    elif len(last) ==2:
        a= sum(last) * last[-1]
        if total < a:
            total =a
            solve(A,A[0:3],3)
    else:
        a= sum(last) * last[-1]
        if total < a:
            total =a
            not_param+=1
            if not_param <=len(A):
            
                solve(A,A[0:not_param],not_param)
            else:
                return




N = int(input())
A =  list(map(int, input().split(" ")))
A.sort(reverse=True)
total =0
solve(A,A[0:1],1)
# 이건 ㅜ조건 우측에서 시작한 정복 정렬임에 틀림없다.


print(total)
