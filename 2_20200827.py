Sum = 0
a = input()
b = a.split(',')
b = list(map(int,b))
for i in range (len(b)) :
    Sum = Sum + b[i]
print(Sum)
