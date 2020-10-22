# 풀이 1 : 재귀
def fire( start_node, people, visitied,n, friend_ship):
    if   len(visitied) == n//2:
        print(visitied)
        global answer
        answer+=1
        return 
    else:
        while start_node<len(friend_ship)-1:
            start_node +=1
            if (friend_ship[start_node][0]  in people) and ( friend_ship[start_node][1]  in people): 
                people2 = people[:]
                people2.remove(friend_ship[start_node][0])
                people2.remove(friend_ship[start_node][1])
                visitied2 = visitied[:]

                visitied2.append(friend_ship[start_node])
                fire( start_node, people2, visitied2,n, friend_ship)
        return 





answer=0
c   = 1
for _ in range(1):
    n, m  = map(int, "6 10".split(" "))
    friend_ship_input=list(map(int,"0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5".split(" ")))
    friend_ship_input
    friend_ship=[]
    for i in range(len(friend_ship_input)//2):
        friend_ship.append([friend_ship_input[2*i+1],friend_ship_input[2*i]])
    people = list(range(n))
    global answer
    answer=0
    for i in range(len(friend_ship)):
        people3 = people[:]
        people3.remove(friend_ship [i][0])
        people3.remove(friend_ship[i][1])
        # 반복문으로 friend_ship 에서  이미 줄선 애들 뺴는 것도 좋은 생각

        fire(i, people3, [friend_ship[i]],n, friend_ship)
    print(answer)
