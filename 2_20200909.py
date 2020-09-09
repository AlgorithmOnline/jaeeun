def solution(record):
    answer = []
    person={"uid":"", "nickname":""} # 인간 한명
    characters={} # 인간 여러명  key: 아이디,value: list(nickname s)
    for r in record:
        aaa=list(r.split(" "))
        if aaa[1] not in   characters:
            characters[aaa[1]] = [aaa[2]]
        else:
            #print(characters[aaa[1]][-1])
            if len(aaa) ==3:
                if  characters[aaa[1]][-1] == aaa[2]:
                     pass
                else:
                    characters[aaa[1]].append(aaa[2])
    a2=[]
    for r in range(len(record)):
        aaa=list(record[r].split(" "))
        nick=characters[aaa[1]][-1]
       
       # print(aaa[0])
        if aaa[0]=="Enter":
          #  print(3)
            #print(nick)
            #print(nick+"님이 들어왔습니다.")
            aaaa=nick+"님이 들어왔습니다."
            a2.append(aaaa)
         #   print(a2)
        elif aaa[0]=="Leave":
          #  pass
            a2.append(nick+"님이 나갔습니다."   ) 
        else:
            pass
                    
    return a2
            
    
    
    
    return answer
