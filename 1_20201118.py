def solution(s):
    answer = True
    before =list(s)
    after  = []
    while before:
        travel = before.pop()
        if travel ==')':
            after.append(travel)
        else:
            if len(after) ==0:
                return False
            else:
                after.pop()
            
    if len(after) ==0:
        return True
    else:
        return False

