n= int(input())
a={}
for _ in range(n):
    f,name=input().split()
    f= int(f)
    if f in a:
        a[f].append(name)
    else:
        a[f]=[name]
a= sorted(a.items(), key= lambda g:g[0])
for i in a:
    for j in i[1]:
        print(i[0],j )
    
