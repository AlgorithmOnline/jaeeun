def solution(a, b):
    mons = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    days = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    ans=0
    if a!=1:
        while a!=1:
            a-=1
            ans+=mons[a]
            
    else:
        b%=7
        return days[b]
    
    ans+=b
    ans %=7
    return days[ans]
    
