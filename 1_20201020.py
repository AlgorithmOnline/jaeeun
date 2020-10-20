def solution(N,A):
	li = {i:0 for i in range(1, N+1)}
    max_sum = 0
    max_num = 0
    for key in A:
    	if key ==N+1:
        	max_sum +=max_num
            li.clear() 
            max_num = 0
        else:
        	if li.get(key)  is None:
            	li[key]=1
            else:
            	li[key]+=1
            max_num = max(max_num, li[key])
     answer = [max_sum]*N
     for key, val in li.items():
     	answer[key-1] +=val
     return answer
