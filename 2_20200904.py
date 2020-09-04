import heapq
import sys

heap=[]
N = int(sys.stdin.readline())
for _ in range(N):
    a = int(sys.stdin.readline())
    
    if a ==0:
        if len(heap) ==0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
       # abs_a = abs(a)
        if a> 0:
            heapq.heappush(heap,(a,a))
        else:
             heapq.heappush(heap,(a*(-1),a))
