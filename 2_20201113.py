import collections
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_tree = collections.deque(list(skill_tree))
        skill_copy=  collections.deque(list(skill))
        ans_flag = True
        while skill_tree:
            travel = skill_tree.popleft()
            if travel in skill:
                if travel == skill_copy[0]:
                    skill_copy.popleft()
                else:
                    ans_flag = False
                    break
            else:
                continue
        if ans_flag:
             answer+=1
                    
    return answer
