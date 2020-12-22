N = int(input())
homes  =[]
answer=[]
for i in range(N):
    R,G,B = map(int, input().split())
    homes.append({'R':R, 'G':G, 'B':B})
dp=[homes[0]]
for i in range(1,N):
    dp.append({'R':homes[i]['R']+min(dp[-1]['G'],dp[-1]['B']),'G':homes[i]['G']+min(dp[-1]['B'],dp[-1]['R']), 'B':homes[i]['B']+min(dp[-1]['G'],dp[-1]['R']) })
print(min(dp[-1]['R'],dp[-1]['G'],dp[-1]['B'] ))
