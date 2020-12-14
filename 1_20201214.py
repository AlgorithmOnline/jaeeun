k = int(input())
s = []
cnt_zero = 0
cnt_one = 0
for _ in range(k):
    s.append(list(map(int,input().split())))

def check(i, j, n):
    global cnt_zero, cnt_one
    t = s[i][j]
    for x in range(i, i + n):
        for y in range(j, j + n):
            if t != s[x][y]:
                check(i,j,n//2)
                check(i,j+n//2,n//2)
                check(i+n//2,j,n//2)
                check(i+n//2,j+n//2,n//2)
                return
                
    if t == 0:
        cnt_zero += 1
    else:
        cnt_one += 1

check(0, 0, k)
print(cnt_zero)
print(cnt_one)
