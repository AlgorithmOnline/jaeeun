N = int(input())
NN = N
ans=0
while NN//5!=0:
    ans+=NN//5
    NN//=5
print(ans)
