N,S,M=map(int,input().split())
play_list = list(map(int, input().split()))
possible_volumns=[]

def fire(start_volumns, possible, M):
    next_volumns=set()
    if start_volumns[0]==-1 or len(start_volumns)==0:
        return [-1]
    for volumn in start_volumns:
        if volumn+ possible<=M:
            next_volumns.add(volumn+ possible)
        if volumn- possible>=0:
            next_volumns.add(volumn- possible)
    if len(next_volumns)==0:
        return [-1]
    return list(next_volumns)

start_volumns = [S]
flag = True
for possible in play_list:
    if start_volumns[0]==-1 or len(start_volumns)==0:
        flag = False
        print(-1)
        break
    else:
        start_volumns=fire(start_volumns, possible, M)
        #print(start_volumns)
if flag:
    print(max(start_volumns))
