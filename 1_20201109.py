import collections
def solution(n):
    str_2_n = str(bin(n))[2:]
    origin= dict(collections.Counter(list(str_2_n)))
    one = origin['1']
    n2= n
    while 1:
        n2+=1
        n2_st = str(bin(n2))[2:]
        origin2= dict(collections.Counter(list(n2_st)))
        one2 = origin2['1']
        if one2==one:
            return n2
  #   1최고, second 차항 위로  나머진 다 뒤로 싹싹

    answer = 0
    return answer
