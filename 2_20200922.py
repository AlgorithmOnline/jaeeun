




# 벌집은 그냥 변두리까지 길이가 그 변에선 모두 같다. 원과 유사한 느낌
A= int(input())
ans=1
tmp=0

if ans == A:
    print(1)
else:
    while ans< A:
        tmp+=1
        ans+=(tmp-1)*6
        if ans==A:
          #  print(tmp)
            break
       # print(ans,tmp)



    print(tmp)
