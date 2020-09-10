def solution(m, n, board):
    # 4 개씩 출력할 생각

    # 톰소여 모험
    board2=[]
    for k in range(n):
        sss=''
        for b in range(m):
            sss+=board[b][k]
        board2.append(sss)
    board = board2
    temp = m
    m = n
    n = temp

    
    answer=0
    breakpoint=9999
    while(breakpoint!=0):
        ans_list =set()
        for a in range(0,m-1):
            for b in range(0,n-1):
                if board[a][b]==board[a][b+1] and board[a][b]!='@@':
                    if board[a-1][b]== board[a][b] and board[a][b+1] ==  board[a-1][b+1] and board[a][b+1]!='@':
                        ans_list.add(str([a-1,b]))
                        ans_list.add(str([a,b]))
                        ans_list.add(str([a-1,b+1]))
                        ans_list.add(str([a,b+1]))
                    if board[a+1][b]== board[a][b] and board[a][b+1] ==  board[a+1][b+1] and board[a][b]!='@':
                        #ans_list.append([[a+1,a],[b,b+1]])
                        ans_list.add(str([a+1,b]))
                        ans_list.add(str([a,b]))
                        ans_list.add(str([a+1,b+1]))
                        ans_list.add(str([a,b+1]))
                if board[a][b]==board[a][b-1] and board[a][b]!='@@':
                    if board[a-1][b]== board[a][b] and board[a][b-1] ==  board[a-1][b-1] and board[a][b-1]!='@':
                      #  ans_list.append([[a-1,a],[b,b-1]])
                        ans_list.add(str([a-1,b]))
                        ans_list.add(str([a,b]))
                        ans_list.add(str([a-1,b-1]))
                        ans_list.add(str([a,b-1]))
                    if board[a+1][b]== board[a][b] and board[a][b-1] ==  board[a+1][b-1] and board[a][b-1]!='@':
                       # ans_list.append([[a+1,a],[b,b-1]])
                        ans_list.add(str([a+1,b]))
                        ans_list.add(str([a,b]))
                        ans_list.add(str([a+1,b-1]))
                        ans_list.add(str([a,b-1]))
        
        breakpoint=len(ans_list)
      #  print(breakpoint)
        answer+=len(ans_list)
        if breakpoint ==0:
            break
        # 지도에 터진건 x 표시
        for param in ans_list:
            param=param[1:-1]
            q,w= map(int, param.split(","))
            board[w]='@'+board[w][:q]+board[w][q+1:]
     #   print(board)

                
                
    #print(answer)
    return answer
