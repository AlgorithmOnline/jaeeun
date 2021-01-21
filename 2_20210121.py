# 백준 10871번 
N,X = map(int, input().split())
ass= list(map(int, input().split()))
for i in range(N):
    if ass[i]<X:
        print(ass[i], end= ' ')`
