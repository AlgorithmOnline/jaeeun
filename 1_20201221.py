import collections
n = int(input())
b= collections.deque()
for _ in range(n):
    i = input()
    if i=='0':
        b.pop()
    else:
        b.append(i)
        
print(sum(list(map(int, list(b)))))
