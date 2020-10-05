N = int(input())
test=[]
test_plus=[]
test_minus=[]
zero_here=0 # 제로 있다.
one_here =0 # 1 개수
for _ in range(N):
    a= int(input())
    test.append(a)
    if a>1:
        test_plus.append(a)
    elif a==1:
        one_here+=1
    elif a==0:
        zero_here+=1
    else:
        test_minus.append(a)
        
        
test_minus.sort(reverse=True)
test_plus.sort()
answer=one_here
# 1, 0, 음수를 크게 생각할 것
while len(test_plus)>=2:
    answer+=test_plus[-2]*test_plus[-1]
    test_plus.pop()
    test_plus.pop()
    
if len(test_plus)==1:
    answer+=test_plus[0]
    
while len(test_minus)>=2:
    answer+=test_minus[-2]*test_minus[-1]
    test_minus.pop()
    test_minus.pop()   
    
if len(test_minus)==1:
    if zero_here>0:
        pass
    else:
        answer+=test_minus[0]    
print(answer)
