iimport collections


def solution(n):
    answer = [[0]*i for i in range(1, n+1)]
    
    
    def fire(step, start,n):

      
        if step==1:
            step+=1
            move=[1,0]
        elif step==2:
            step+=1
            move = [0,1]
        elif step==3:
            step=1
            move=[-1,-1]
            
        will_visit=collections.deque([start])
        break_flag= True
        while will_visit:
               
               travel_origin = will_visit.popleft()
               travel = [travel_origin[0]+move[0], travel_origin[1]+move[1]]
             #  print(travel,step)
               if 0<=travel[0]<n and 0<=travel[1]<n and answer[travel[0]][travel[1]] ==0:
                    break_flag=False
              #      print(travel)
                    will_visit.append(travel)
                    answer[travel[0]][travel[1]] =answer[travel_origin[0]][travel_origin[1]] +1

        if break_flag:
            return 
        else:
          #  print(travel)
           # print(answer, step)
            return fire(step, travel_origin,n)


    start =[-1,0]
    fire(1, start,n)
    #print(answer)
    real=[]
    for i in answer:
        real+=i
    return real
#solution(4)
