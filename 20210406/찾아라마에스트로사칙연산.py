import math

def solution(arr):
    number_arr = [int(arr[i]) for i in range(0, len(arr), 2)]
    operator = [arr[i] for i in range(1, len(arr), 2)]
    dp = [[[math.inf, -math.inf] for _ in range(len(arr) // 2 + 1)] for _ in range(len(arr) // 2 + 1)]
    
    for i, v in enumerate(number_arr):
        dp[i][i] = [v, v]
        
    for i in range(0, len(number_arr) - 1):
        j = i + 1
        if operator[i] == "+":
            dp[i][j][0] = dp[i][j][1] = dp[i][j-1][1] + dp[i+1][j][1]
        else:
            dp[i][j][0] = dp[i][j][1] = dp[i][j-1][1] - dp[i+1][j][1]
        
    for k in range(2, len(number_arr)):
        for i in range(0, len(number_arr) - k):
            j = i + k
            
            for m in range(1,k+1):
                y, x = i, j - m
                b, a = j + 1 - m, j
                if operator[x] == "+":
                    dp[i][j][1] = max(dp[y][x][1] + dp[b][a][1], dp[i][j][1])
                    dp[i][j][0] = min(dp[y][x][0] + dp[b][a][0], dp[i][j][0])
                else:
                    dp[i][j][1] = max(dp[y][x][1] - dp[b][a][0], dp[i][j][1])
                    dp[i][j][0] = min(dp[y][x][0] - dp[b][a][1], dp[i][j][0])
    
    return dp[0][-1][1]




