def solution(answers):
    person =[[1,0],[2,0],[3,0]]
    p1 = [1, 2, 3, 4, 5]
    p2= [2, 1, 2, 3, 2, 4, 2, 5]
    p3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
    length=len(answers)
    for i in range(length):
        if  p1[i%5] == answers[i]:
            person[0][1]+=1
        if  p2[i%8] == answers[i]:
            person[1][1]+=1 
        if  p3[i%10] == answers[i]:
            person[2][1]+=1

    person =sorted(person, key= lambda a:a[1], reverse=True)
    answer = [person[0][0]]
    if person[0][1] ==person[1][1]:
        answer.append(person[1][0])
        if person[1][1] ==person[2][1]:
            answer.append(person[2][0])
 
    return answer
