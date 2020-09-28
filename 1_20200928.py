def solution(words):
    will_visit=words
    visit=[]
    i=0
    answer = 0
    while will_visit:
        tmp_visit={}
        for k in range(len(will_visit)):
            char_tmp=will_visit[k][:i+1]
            if char_tmp in tmp_visit:
                tmp_visit[char_tmp].append(will_visit[k])
            else:
                tmp_visit[char_tmp]=[will_visit[k]]
        #print(tmp_visit)
        for l in tmp_visit:
            if len(tmp_visit[l])==1:
                answer += len(l)
                will_visit.remove(tmp_visit[l][0])
            elif len(tmp_visit[l])==2:
                #continue 
                ll=i+1
                ff=tmp_visit[l][0][:ll][:]
                if ff ==tmp_visit[l][0] or tmp_visit[l][1]==ff:
                    answer+=len(ff)*2+1
                  #  print(ff,len(ff)*2+1 )
                    will_visit.remove(tmp_visit[l][0])
                    will_visit.remove(tmp_visit[l][1])
                    continue

                while tmp_visit[l][0][:ll]==tmp_visit[l][1][:ll]:
                   # print('hey',tmp_visit[l][0][:ll])
                    ll+=1

                if     ll-1==len(tmp_visit[l][0]) or      ll-1==len(tmp_visit[l][1]):
                    answer += 2*ll-1
                   # print('erw',2*len(ff)+1,ff,ll)
                else:  
                    answer += 2*len(tmp_visit[l][0][:ll])
                   # print('banab',len(tmp_visit[l][0][:ll])*2)
                will_visit.remove(tmp_visit[l][0])
                will_visit.remove(tmp_visit[l][1])
        i+=1






    return answer
