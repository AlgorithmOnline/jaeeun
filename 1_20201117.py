import math
def divide(matrix):
    N = len(matrix)
    mid   = math.ceil((N-1)/2)
    matrixs = [[],[],[],[]]
    for row in range(N):
        if mid<=row:
            tmp_row_0 =[]
            tmp_row_1 =[]
            for col in range(N):
                if  mid>col:
                    tmp_row_0.append(matrix[row][col])
                else:
                    tmp_row_1.append(matrix[row][col])
            matrixs[2].append(tmp_row_0)
            matrixs[3].append(tmp_row_1)
        elif mid>row:
            tmp_row_0 =[]
            tmp_row_1 =[]
            for col in range(N):
                if  mid>col:
                    tmp_row_0.append(matrix[row][col])
                else:
                    tmp_row_1.append(matrix[row][col])
            matrixs[0].append(tmp_row_0)
            matrixs[1].append(tmp_row_1)
    return matrixs

import collections
answer={0:0,
       1:0}
def fire(matrix):
    tmp=[]
    for i in matrix:
        tmp+=i
    counter  = dict(collections.Counter(tmp))
    if len(counter)==1:
        global answer
        answer[matrix[0][0]]+=1
    else:
        matrixs =  divide(matrix)
        for m in matrixs:
            fire(m)
    
def solution(arr):
    global answer
    fire(arr)
    answer = [answer[0], answer[1]]
    return answer

