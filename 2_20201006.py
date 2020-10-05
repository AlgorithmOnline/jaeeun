N, X = map(int, input().split()) # N 이 문자열 개수, X 가 비용
if X< N or X>26*N:
    print('!') # 1차 걸름
else:
    answer=['A'  for _ in range(N)]
    X-=N
    may_z = X//25 # z 의 개수
    namu_z = X%25
    zz=N-1
    while may_z>0:
        answer[zz]='Z'
        zz-=1
        may_z-=1
    if namu_z>0:
        answer[zz]=chr(namu_z+65)
    print(''.join(answer))
