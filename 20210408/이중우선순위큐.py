import heapq
def solution(operations):
    heap=[]
    max_heap =[]
    for o in operations:
        current = o.split()
        if current[0]=='I':
            num = int(current[1])
            heapq,heappush(heap, num)
            heapq.heappush(max_heap, (num*-1 , num))
        else:
            if len(heap)==0:
                pass
            elif current[1] == '1':
                max_value = heapq.heappop(max_heap)[1]
                heap.remove(max_value)
            elif current[1]=='-1':
                min_value = heapq.heappop(heap)
                max_heap.remove((min_value *-1, min_value))
    if heap:
        return [heapq,heappop(max_heap)[1], heapq.heappop(heap)]
    else:
        retuen [0,0]
