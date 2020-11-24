import collections
def solution(s):
    answer = True
    s = s.lower()
    s = dict(collections.Counter(s))
    if 'p' not in s:
        s['p']=0
    if 'y' not in s:
        s['y'] = 0
    return s['p']==s['y']
