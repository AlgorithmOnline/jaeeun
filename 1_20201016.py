T =int(input())
for _ in range(T):
    N,A = input().split()
    N=int(N)
    B = '0b'+'1'*N
    B = int(B, 2)
    #A='0?1?'
    A1 =int('0b'+ A.replace("?","1"),2)
    A2 =int('0b'+ A.replace("?","0"),2)

    AB1 = len(str(bin(A1*B))) -2

    AB2 = len(str(bin(A2*B))) -2

    print(AB1, AB2)
