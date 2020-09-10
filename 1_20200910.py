import math
def solution(lines):
    answer = 0
    if len(lines) ==1:
        return 1
    
    lines_tmp=[]
    for line in lines:
        tmp1=line.split(" ")
        tmp1=tmp1[1:]
        tmp2=tmp1[0].split(":")
        times=0
        for indx,t in enumerate(tmp2):
            times+= float(t)*math.pow(60,(2-indx))
        real_start_end=[times-float(tmp1[1][:-1]), round(times-0.001,3)]
        lines_tmp.append(real_start_end)
    ans=0
    for line in lines_tmp:
        if_zero_start=line[0]
        if_zero_end = round(line[0]+0.999,3)

        if_one_start=line[1]
        if_one_end = round(line[1]+0.999,3)
        power=0
        power1=0
        for i in lines_tmp:
            if i[0]<= if_zero_start and  if_zero_start <=i[1]:
    #             print(if_zero_start)
                power+=1
            elif i[0]<= if_zero_end and  if_zero_end <=i[1]:
    #             print(if_zero_end)
                power+=1
            if i[0]<= if_one_end and  if_one_end <=i[1]:
                #print(if_one_end)
                power1+=1
            elif i[0]<= if_one_start and  if_one_start <=i[1]:
                #print(if_one_start)
                power1+=1
        power=max(power1,power)   
        ans=max(power, ans)
        
    return ans

###
