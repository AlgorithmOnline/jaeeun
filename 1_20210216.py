import copy
def solution(n):
    dp=[None,[[1,3]],[ [1,2], [1,3], [2,3] ]]
    if n==1:
        return dp[1]
    elif n==2:
        return dp[2]
    while len(dp)<n+1:
        row =[]
        first_step=copy.deepcopy(dp[-1])
        for i in range(len(first_step)):
            for k in range(len(first_step[i])):
                if first_step[i][k]==2:
                    first_step[i][k]=3
                elif first_step[i][k]==3:
                    first_step[i][k]=2
        second_step=[[1,3]]
        third_step=copy.deepcopy(first_step)
        
        for i in range(len(third_step)):
            for k in range(len(third_step[i])):
                if third_step[i][k]==2:
                    third_step[i][k]=3
                elif third_step[i][k]==3:
                    third_step[i][k]=1
                elif third_step[i][k]==1:
                    third_step[i][k]=2

        row=first_step+second_step+third_step
        dp.append(row)
    return dp[n]
