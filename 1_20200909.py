import collections
# https://excelsior-cjh.tistory.com/94
# https://pydole.tistory.com/entry/Python-collections-Counter%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%95%A9%EC%A7%91%ED%95%A9-%EA%B5%90%EC%A7%91%ED%95%A9-%EC%B0%A8%EC%A7%91%ED%95%A9-%EA%B5%AC%ED%95%98%EA%B8%B0

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    A=[]
    B=[]
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha() and str1[i+1]!=" " and  str1[i]!=" ":
            A.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha() and str2[i+1]!=" " and  str2[i]!=" ":
            B.append(str2[i:i+2])
    len_A= len(A)
    len_B= len(B)
    A = collections.Counter(A)
    B= collections.Counter(B)
    if len_A+len_B ==0:
        return 65536
    else:
        return int( len(list((A&B).elements()))/len(list((A|B).elements()))*65536)
