aA, B, C = map(int, input().split())
# 아아아아아아아ㅏ악

def solve(A, B):
    if(B % 2 > 0):
        return solve(A, B - 1) * A
    elif(B == 0): # 이런 작은 것들을 생각해야함.
        return 1
    elif(B == 1): # 이런 작은 것들을 생각해야함.
        return A
    else:
        # 10^11에서 11을 %2 해줄때의 경우는 홀수와 짝수로 나뉘게 된다.
        # 첫 시작부터 % 12를 붙이고 끝까지 계산을 해보면,
        # 왜 result ** 2 % C가 필요한지 알 수 있다.
        result = solve(A, B//2)
        return result ** 2 % C

# 식을 보는 도중, 여기서 왜 또 %C를 해주는지 헷갈릴 수 있는데,
# solve(A, B)는 (10, 11)의 결괏값이고,
# (10, 11) % C는 문제가 원하는 정답이다.
print(solve(A, B) % C)
