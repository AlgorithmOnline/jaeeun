N ,K = map(int, input().split())
lines =list(map(int, input().split()))



def binary_search(low, high ):
    mid = (high+low)//2
    if low==high or mid ==low or high==mid:
        print(mid)
        return 
    else:
        maxPass=0
        midPass=0
        minPass=0
        for i in  range(len(lines)):
            if lines[i]>=high:
                
                maxPass+=lines[i]-high
            if lines[i]>=mid:
                midPass+=lines[i]-mid
            if lines[i]>=low:    
                minPass+=lines[i]-low
    if maxPass>=K:
        print(high)
        return
    elif midPass>=K and maxPass<K:
        return binary_search(mid, high  )
    elif minPass>=K and midPass<K:
        return binary_search(low,mid  )
    else:
        return 
        


binary_search(0, max(lines))   
    
