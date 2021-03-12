def solution(S, P, Q):
    coder = {
        "A": 1,
        "C": 2,
        "G": 3,
        "T": 4
    }

    # write your code in Python 3.6

    dp = [[coder[S[c]] if c == r else float('inf') for c in range(len(S))] for r in range(len(S))]
    for row in range(len(S)):
        for col in range(row + 1, len(S)):
            dp[row][col] = min(dp[row][col - 1], dp[col][col])
    answer = []
    for i in range(len(P)):
        a, b = min(P[i], Q[i]), max(P[i], Q[i])
        answer.append(dp[a][b])
    return answer


if __name__ == '__main__':
    solution('CAGCCTA', [2, 5, 0], [4, 5, 6])
