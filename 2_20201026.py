N, M = map(int, input().split()) # row , dolumn 
maps=[]
for _ in range(N):
    maps.append(list(input()))

empty_row=[]
empty_column=[]
for m in range(N):
    if ''.join(maps[m]) =='.'*M:
       # print('.'*M)
        empty_row.append(m)
    #for n in range(N):


for n in range(M): # column
        dragon4=True
        for m in range(N): # row
          #  print(m,n)
            if maps[m][n]!='.':
                dragon4=False
            else:
                continue
        if dragon4:
            empty_column.append(n)

#print(empty_row)
#print(empty_column)
print(max(len(empty_column), len(empty_row)))               
