import collections
def solution(str1, str2):
    dict={}
    str1=list(str1.upper())
    str2=list(str2.upper())
    print(str1,str2)
    index=1
    A=collections.defaultdict(int)
    B=collections.defaultdict(int)
    for i in range(len(str1)-1):
        if str1[i]+str1[i+1] in dict:
            A[dict[str1[i]+str1[i+1]]]+=1
        else:
            if not str1[i].isalpha() or not str1[i+1].isalpha():
                continue
            dict[str1[i]+str1[i+1]]=index
            A[index]+=1
            index+=1
    for i in range(len(str2)-1):
        if str2[i]+str2[i+1] in dict:
            B[dict[str2[i]+str2[i+1]]]+=1
        else:
            if not str2[i].isalpha() or not str2[i+1].isalpha():
                continue
            dict[str2[i]+str2[i+1]]=index
            B[index]+=1
            index+=1
    bunmo=0
    bunja=0
    for i in range(1,index+1):
        bunmo+=max(A[i],B[i])
        bunja+=min(A[i],B[i])

    if bunmo==0:
        return 65536
    answer=int((bunja*65536)/bunmo)
    return answer
