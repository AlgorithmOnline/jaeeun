import sys

arr = [int(sys.stdin.readline()) for _ in range(int(input()))]

def solve(arr):
    stack = []
    answer = []
    idx = 0
    curnum = 1

    while idx < len(arr):
        if stack:    #안비어있을때.
            if stack[-1] != arr[idx]:    #마지막요소랑 지금 뽑아야할 수랑 다르면
                if curnum > arr[idx]:    #다른데, 이미 스택안에 들어있으면 못뽑으니까 No
                    return ['NO']
                else:                    
                    stack.append(curnum)
                    answer.append('+')
                    curnum += 1
            else:                        #마지막요소랑 지금 뽑아야할 수가 같으면.
                answer.append('-')
                idx += 1
                stack.pop()
        else:
            stack.append(curnum)
            answer.append('+')
            curnum += 1

    return answer

print(*solve(arr), sep='\n')            #리턴받은 배열에서 한줄씩 요소 출력
