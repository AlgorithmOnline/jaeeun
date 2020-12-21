import collections
a=input()
while a!='.':
    b= collections.deque()
    ans=True
    for i in a:
        if i=='(':
            b.append('(')
        elif i=='[':
            b.append('[')
        elif  i==')':
            if len(b)>0 and b[-1] =='(':
                b.pop()
            else:
                ans = False
                break
        
        elif  i==']':
            if len(b)>0 and b[-1] =='[':
                b.pop()
            else:
                ans = False
                break   
    if ans and len(b)==0:
        print("yes")
    else:
        print("no")
    a=input()
