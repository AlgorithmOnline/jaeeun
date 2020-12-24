N = int(input())
K =  int(input())
low =0
high = K # k 번째 수는 K 를 넘을 수 없다.
answer =0
while low<=high:
    mid = (low +high)//2
    count =0
    for i in range(1,N+1):
        count +=min(mid//i, N) # mid // i 가 N보다 클 수 있기 때문에 각 줄이 N 보다  
    if count<K:
        low = mid +1
    else: # 최솟값을 찾아야하기 때문에, 같을 때는 줄여준다.
        answer = mid
        high =mid -1
print(answer)
