import collections
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = collections.deque(truck_weights)
    visit=[]
    on_bridge={
    }
    sum_bridge = 0
    while len(on_bridge) !=0 or len(truck_weights) !=0:
        
        answer+=1
        if len(on_bridge) ==0:
            travel = truck_weights.popleft()
            on_bridge[0] = travel
            sum_bridge+=travel
        else:
            on_bridge_new = dict((key+1,value) for (key, value) in on_bridge.items())
            
            if  bridge_length in on_bridge_new:
                sum_bridge -=on_bridge_new[bridge_length]
                visit.append(on_bridge_new[bridge_length])
                del on_bridge_new[bridge_length]
            on_bridge=on_bridge_new
            if len(truck_weights)!=0 and (truck_weights[0] + sum_bridge) <=weight :
                travel = truck_weights.popleft()
                sum_bridge+=travel
                on_bridge[0] = travel
    return answer
