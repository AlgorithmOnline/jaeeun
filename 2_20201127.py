import math
import sys
from collections import deque, Counter
  
import collections

NOTATION = '0123456789ABCDEF' 

def numeral_system(number, base): # 10진수 n진수로의 변환
  q, r = divmod(number, base) 
  n = NOTATION[r] 
  return numeral_system(q, base) + n if q else n

def solution(n, t, m, p):
    maxs=""
    for i in range(t*m):
        maxs+=numeral_system(i, n)
    # n 진법 튜브의 순서 p, 게임에 참가하는 인원 m , 미리 구할 숫자의 갯수 t
 
    answer = ''
   
    for i in range(t):
        answer+=maxs[i*m+p-1]
    return answer
