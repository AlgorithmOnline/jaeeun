import collections
import itertools
N = int(input())
maps = [[]]*N
for i in range(N):
    maps[i]= list(map(int,input().split()))
history=[]
answer = 999999999999999999999999999999999999999999999999999999999
counts  =list(itertools.combinations(list(range(N)),N//2))
for count in counts:
    count = set(count)
    if count  in history:
        continue
    total = set(list(range(N)))
    reverse_count = total  - count
    history.append(count)
    history.append(reverse_count)
    
    count_cost = sum(list(map(lambda x:maps[x[0]][x[1]],list(itertools.permutations(count,2)))))
    reverse_cost = sum(list(map(lambda x:maps[x[0]][x[1]],list(itertools.permutations(reverse_count,2)))))
    answer=min(answer, abs(count_cost-reverse_cost))
print(answer)
    
