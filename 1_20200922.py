A = int(input())
minus1=1
ans=minus1*(minus1+1)//2
while A>ans:
    minus1+=1
    ans=minus1*(minus1+1)//2
#print(ans,minus1)
ans+=1

ans2=ans-A
total =minus1+1-ans2

# 지그재그를 신경써야한다.
if( ans2+total) % 2 ==1:
    print(str(total)+"/"+str(ans2))
else:

    print(str(ans2)+"/"+str(total))


