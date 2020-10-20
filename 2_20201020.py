def solve(S, type,barrier_letters):
    answer=0
    if type=='a':
        hidden='b'
    elif type=='b':
        hidden='a'
    test = S.split(hidden)
    while len(max(test))>=barrier_letters:
        max_string = max(test)
        S=S.replace(max_string,type*(len(max_string)//2)+hidden+type*(len(max_string)-1-(len(max_string)//2)))
        answer+=1
        test = S.split(hidden)
    return S,answer

def solution(S):
    barrier_letters=3
    S,answerA=solve(S, 'a',barrier_letters)
    S,answerB=solve(S, 'b',barrier_letters)
    return answerA+answerB

solution("baabab")#0
solution("baaabbaabbba")#2
solution("baaaaa")#1
