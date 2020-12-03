n = int(input())
maps = [[0] *n for i in range(n) ]

answer = 0
def fire(maps, history_column, mother,diff,plus):
    moves=[[1,0],[1,1],[1,-1]]
    if mother[0] == len(maps)-1:
        global answer
        answer+=1
        return
    for i in range(len(maps)): # column 만 볼거야
        if i in history_column:
            continue         
        else:
            new_mom = [mother[0]+1, i]
            # 1차원 diff 로 생각.
            if  new_mom[0]-new_mom[1] in diff:
                continue
            elif new_mom[0]+new_mom[1] in plus:
                continue
            
            # 조건에 부합함
            new_history_column = history_column[:]
            new_history_column.append(i)
            new_diff = diff[:]
            new_diff.append( new_mom[0]-new_mom[1])
            new_plus=plus[:]
            new_plus.append(new_mom[0]+new_mom[1])
            fire(maps, new_history_column, new_mom, new_diff, new_plus)
for i in range(n):
    fire(maps, [i],[0,i],[-i],[i])
print(answer)
