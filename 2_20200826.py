import sys
from collections import deque

test_case = int(sys.stdin.readline())
for case in range(test_case):
    node , find = map(int, input().split(" "))
    scores = list(map(int, input().split(" ")))
    scores_map= deque([])
    for n in range(node):
        scores_map.append((n, scores[n]))
    scores =deque(sorted(scores, reverse=True))
    i=1
    while(len(scores)!=0):
        if scores[0] == scores_map[0][1]:
            if scores_map[0][0]==find:
                   print(i) 
            scores_map.popleft()
            scores.popleft()
            i+=1
        else:
            toss =scores_map.popleft()
            scores_map.append(toss)
