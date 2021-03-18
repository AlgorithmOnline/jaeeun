import collections
def transpose(graph):
    return list(map(list, zip(*graph)))
def solution(board, moves):
    stack=[]
    board=transpose(board)
    answer = 0
    for m in range(len(board)):
        board[m]=collections.deque(board[m])
    for m in moves:
        m-=1
        while board[m] and board[m][0]==0:
            board[m].popleft()
        if  board[m] and board[m][0]!=0:
            picked=board[m].popleft()
            if stack and stack[-1]!=picked:
                stack.append(picked)
                continue
            elif stack and stack[-1]==picked:
                stack.pop()
                answer += 2
                continue
            else:
                stack.append(picked)
                continue
                
    return answer
