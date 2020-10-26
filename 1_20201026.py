import collections
def bigger(word):
    return word.upper() # 알파벳 대문자로 바꾸는 방법
A= list(input().upper())
A=  collections.Counter(A)
#print(A)
if len(A)>1:
    B=A.most_common(n=2) # collections Counter 가장 흔한 케이스 찾기
    if  B[0][1] == B[1][1]:
        print("?")
    else:
        print(B[0][0])
elif len(A)==0:
    print()
else:
    
    #print(A[0][0]) # 딕셔너리 개수가 1일때 이게 먹지 않는다.
    print(list(A.keys())[0])
