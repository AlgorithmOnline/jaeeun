dict_group=dict()
g_answer =0
def solution(n, results):
    results+=sorted(results, reverse=True
      )
    answer = 0
    global group
    global dict_group
    for i in range(1, n+1):
        dict_group[i]={
        'big':set(), 
        'small':set(), 
        }
    for result in results:
        dict_group[result[0]]['small'].add(result[1])
        dict_group[result[1]]['big'].add(result[0])
    """"""
    for result in results:  
        for bigger in dict_group[result[1]]['big']:
            dict_group[result[1]]['big']=dict_group[result[1]]['big']|dict_group[bigger]['big']
        for smaller in dict_group[result[0]]['small']:
            dict_group[result[0]]['small']=dict_group[result[0]]['small']|dict_group[smaller]['small']
    """"""
   
    """"""
    for i in dict_group:
        if len(dict_group[i]['big']) + len(dict_group[i]['small']) == n-1:
            answer+=1
    return answer
