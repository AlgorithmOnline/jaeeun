import sys

N = int(input())
times = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

seminars= sorted(times, key=lambda t: (t[1], t[0]))

answer = 0             
end_time = 0        
for seminar in seminars :
    if end_time <= seminar[0] :
        end_time =seminar[1]
        answer += 1
print(answer)
