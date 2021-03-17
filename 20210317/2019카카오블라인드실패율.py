### 

```python
import collections
def solution(N, stages):
    answer = []
    s=collections.Counter(stages)
    ss=sorted(s.items(),key=lambda a:-a[0])
    gosu=0
    ans=[[i+1,0] for i in range(N)]
    answer
    for i in ss:
        gosu+=i[1]
        if i[0]>N:
            continue
        ans[i[0]-1]= [i[0],i[1]/gosu]
    ans= sorted(ans, key=lambda a:(-a[1],a[0] ))
    answer=[]
    for i in ans:
        answer.append(i[0])
    return answer
```


