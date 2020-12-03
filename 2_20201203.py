def hansu(n) :
    cnt=0
    for i in range (1,n+1):
        if i<100 :
            cnt+=1
        else :     
            nums = list(map(int, str(i)))  
            if nums[0] - nums[1] == nums[1] - nums[2] : 
                cnt+=1
        
            
    return cnt       
    
n=int(input())
print(hansu(n))
