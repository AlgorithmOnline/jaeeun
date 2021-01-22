# 백준 8958번 
N = int(input())
for i in range(N):
    ans=list( input())
    aa=[0 for a in range(len(ans))]
    for k in range(len(ans)):
        if ans[k]=='O':
            if k==0:
                aa[k]=1
                continue
            aa[k]=aa[k-1]+1
        else:
            aa[k]=0
    print(sum(aa))
            
