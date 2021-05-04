import re

def solution(files):
    answer = []
    
    head_num_tail = [re.split(r"([0-9]+)", file) for file in files]
    
    sorted_head_num_tail = sorted(head_num_tail, key=lambda x: (x[0].lower(), int(x[1])))
    
    answer = ["".join(h_n_t) for h_n_t in sorted_head_num_tail]
    
    return answer
