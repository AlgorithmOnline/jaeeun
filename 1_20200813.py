# 프로그래머스 카펫 문제

import math
def solution(brown, red):
    total = brown + red
    total_root =int(math.sqrt(total))
    gazi =[]
    for i in range(1,total_root+1):
        if total %i ==0:
            gazi.append([i,total//i]) # 세로,< 가로 ㅇㅣ 순
    for kk in gazi :
        garo =kk[1]
        sero=kk[0]
        if red == (garo -2) * (sero -2):
            return [garo, sero]
