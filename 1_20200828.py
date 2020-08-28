garo, sero   = map(int, input().split(" "))
boards=[]
for _ in range(garo):
    boards.append(input())


board_want=[]
for g in range(garo-7):
    #print(g)
    for s in range(sero-7):
        board = boards[g:g+8]
        board_tmp=[]
        for b in board:
            board_tmp.append(b[s:s+8])
        board_want.append(board_tmp)
ans_list=65
for b in board_want:
    #print(b)
    ans=0
    reverse=True # 줄별로 체크 무늬 바뀐다.
    for garo in range(8):
        if reverse:
            reverse=False # 줄별로 체크 무늬 바뀐다.
            rowrow="WBWBWBWB"
        else:
            reverse=True
            rowrow="BWBWBWBW"
        for sero in range(8):
            #print("board:",b[sero][garo])
            #print(rowrow[sero])
            if b[sero][garo]==rowrow[sero]:
                ans+=0
            else:

                ans+=1
    if ans > 32:
        ans = 64-ans
    if ans_list> ans:
        ans_list = ans

    ans=0

print(ans_list)
