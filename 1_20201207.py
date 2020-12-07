from collections import deque 
n, _ = map(int, input().split()) 
numbers = list(map(int, input().split())) 
queue = deque(range(1, n+1)) 
total_compute = 0 
for idx in range(len(numbers)): 
    if numbers[idx] == queue[0]: 
        queue.popleft() 
        continue 
    queue_idx = queue.index(numbers[idx]) # 뒤 -> 앞으로 옮기는 게 이득인 경우 
    if queue_idx > len(queue) // 2: 
        queue.rotate(len(queue) - queue_idx) 
        total_compute += (len(queue) - queue_idx) # 앞 -> 뒤로 옮기는 게 이득인 경우 
    elif queue_idx <= len(queue) // 2: 
        queue.rotate(-queue_idx) 
        total_compute += queue_idx 
    queue.popleft() 
print(total_compute)

