import sys
import math

A,B,C = map(int, input().split(" "))
# first_start =A//(C-B)
# while  A +(B*first_start)>=C*first_start:
#     first_start+=1
# print( first_start)
if B <C: # 중요
    print(1+(A//(C-B)))#  엡실론
else:
    print(-1) # 문제를 잘 읽고, 분모 0을 주의
