import collections
def solution(participant, completion):
    before = collections.Counter(participant)
    after = collections.Counter(completion)
    answer = list((before - after).elements())
    return answer[0]
