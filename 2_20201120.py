def solution(N, number):
    answer = -1
    S = [set() for x in range(8)]
    for i,x in enumerate(S, start=1):
        x.add(int(str(N)*i))
    for i in range(1, len(S)):
        for j in range(i):
            for op1 in S[j]:
                for op2 in S[i-j-1]:
                    S[i].add(op1 + op2)
                    S[i].add(op1 - op2)
                    S[i].add(op1 * op2)
                    if op2 != 0:
                        S[i].add(op1 // op2)
        if number in S[i]:
            answer = i + 1
            break
    return answer
