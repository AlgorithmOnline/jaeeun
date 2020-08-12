# 프로그래머스 이중 우선순위 큐
def solution(operations):
    # 항상 소팅이 돼어 있어야한다.
    answer = []
    queue=[]
    for op in operations:
        if op[:1] =='I':
            queue.append(int(op[2:]))
            queue.sort()
        elif op =="D 1": # 최대 제거
            if len(queue) ==0:
                continue
            else:
                queue=queue[:-1]
        elif op =="D -1": # 최소 제거
            if len(queue) ==0:
                continue
            else:
                queue=queue[1:]
    if len(queue) ==0:
                return [0,0]
    else:

        answer.append(queue[-1])
        answer.append(queue[0])
    return answer
