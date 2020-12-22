T = int(input())
Ns =[0,1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for _ in range(T):
    N = int(input())
    if N < len(Ns):
        print(Ns[N])
    else:
        for i in range(len(Ns), N+1):
            Ns.append(Ns[i-1]+Ns[i-5])
        print(Ns[N])
