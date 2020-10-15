def gcd(a,b):
    # A>b
    fs=[a,b]
    fs.sort()
    a=fs[1]
    b=fs[0]
    if a==b:
        return a
    elif b ==1:
        return 1
    elif a%b ==0:
        return b
    
    else:
        return abs(gcd(max(b,a-b), min(b,a-b)))

N = int(input())
rings=list(map(int,input().split(" ")))
# N = 4
# rings=[12,3,8,4]
first_ling = rings[0]
rings=rings[1:]
for r in range(len(rings)):
    
    aa=[ first_ling,rings[r]]
  
    aa=[ first_ling// gcd(aa[0],aa[1]),rings[r]//gcd(aa[0],aa[1])] 
    print(str(aa[0])+"/"+str(aa[1]))

        
    
