#!/usr/bin/env python
# coding: utf-8

# In[110]:


from collections import deque
answer=0
anslist=[]
def solution(sticker):
  

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    bfs(deque(sticker),  0,[]) 

    return answer

def bfs(sticker,  ans,listlist):
    global answer 
    if len(sticker)==0:
        return
    elif  len(sticker)==1:
        ans+=sticker[0]
        listlist.append(sticker[0])
        if answer <ans:
            answer=ans
            anslist.append(listlist)
            return
    elif len(sticker)==3 or len(sticker)==2:
        sticker = list(sticker)
        sticker.sort(reverse=True)
        sticker = deque(sticker)
        ans+=sticker[0]
        listlist.append(sticker[0])
        if answer <ans:
            answer=ans
            anslist.append(listlist)
            return
    elif len(sticker)==4:
        a= sticker[0]+ sticker[2]
        b= sticker[1]+ sticker[3]
        if a<b:
            ans= b
            listlist.append( sticker[1], sticker[3])
        else:
            ans=a
            listlist.append( sticker[0], sticker[2])
        if answer <ans:
            answer=ans
            anslist.append(listlist)
            return
    else:
        len_sticker = len(sticker)
        for k in range(len_sticker):
            sticker2=sticker.copy()
            ans2=ans+sticker[k]
            #listlist2 = listlist.append(sticker[k])

            if k!=0:
               
                sticker2.rotate(-k)
            sticker2.popleft()
            sticker2.popleft()
            sticker2.pop()
            bfs(sticker2,  ans2,listlist[:]) 
            
        

