import collections
import itertools
import heapq
def solution(orders, course):
    answer = []
    rank = collections.defaultdict(int)
    countRank= collections.defaultdict(lambda : collections.defaultdict(int))
    for c in course:
        for o in orders:
            o=sorted(list(o))
            f = list(itertools.combinations(list(o), c))
            for i in f:
                rank[''.join(i)]+=1
                countRank[len(i)][''.join(i)]-=1
    
    for c in course:
        aa= []
        for i in countRank[c].items():
            heapq.heappush(aa,(i[1], i[0]))
        if len(aa)>0:
            ff= heapq.heappop(aa)
            if ff[0]<=-2:
                answer.append(ff[1])
                while len(aa)>0:
                    a=heapq.heappop(aa)
                    if ff[0]==a[0]:
                        answer.append(a[1])
                    else:
                        break
                        
    answer.sort()
    return answer
