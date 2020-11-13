import math
import collections
def solution(progresses, speeds):
    progresses = list(map(lambda a:100-a , progresses))
    tasks = list(zip(progresses, speeds))
    tasks = list(map(lambda a: math.ceil(a[0]/a[1]), tasks))
    #tasks.sort()
    tasks=collections.deque(tasks)
    answer = []
    before =[]
    while tasks:
       # print(before)
        travel = tasks.popleft()
        if len(before)==0:
            before.append(travel)
        else:
            if before[0]<travel:
                answer.append(len(before))
                before=[travel]
            else:
                before.append(travel)
    if len(before)>0:
        answer.append(len(before))
                
        
    return answer
