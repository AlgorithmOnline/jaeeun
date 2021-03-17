NOTATION = '0123456789ABCDEF' 
def numeral_system(number, base): 
    q, r = divmod(number, base) 
    n = NOTATION[r] 
    return numeral_system(q, base) + n if q else n


def solution(n):
    answer=0
    three_num = str(int(str(numeral_system(n, 3))[::-1]))
    for i in range(len(three_num)):
        answer+=int(three_num[i])*3**(len(three_num)-i-1)
    
    
    return answer
