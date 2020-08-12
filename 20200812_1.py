# 프로그래머스
# 가장 긴 팰린드롬
# 
def solution(s):
    # 회문은 스택을 쓰면 된다.
    real=""
    for i in s:
        real+=i
        real+="_"
    s=real[:-1]
        
    answer = 1
    for flag2 in range(1,len(s)-1):
        flag = flag2
        before = flag
        after= len(s) -before -1
        if before<after:
            before_stack = list(s[:before][:])
            hhhh = len(before_stack)
            after_stack=list(s[flag+1:flag+1+hhhh ][:][::-1])
            if s[flag]=='_':
                target =0
            else:
                target = 1
            while(len(before_stack)!=0 and len(after_stack)!=0 ):
                first = before_stack.pop()
                second = after_stack.pop()
                if first == second:
                    if first =="_":
                        pass
                    else:
                        target +=2
                else:
                  
                    break
            if answer < target:
                       answer = target
                        
        else:
            after_stack=list(s[flag+1: ][:][::-1])
            hhhh = len(after_stack)
            before_stack = list(s[flag-hhhh:flag][:])
            if s[flag]=='_':
                target =0
            else:
                target = 1
            while(len(before_stack)!=0 and len(after_stack)!=0 ):
                first = before_stack.pop()
                second = after_stack.pop()
                if first == second:
                    if first =="_":
                        pass
                    else:
                        target +=2
                else:
                    break
                        
            if answer <target:
                    answer = target
                        
    return answer
