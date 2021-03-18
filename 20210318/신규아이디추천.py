
def solution(new_id):
    answer = step2(step1(new_id))
    return answer


def step1(new_id):
    return new_id.lower()


def step2(new_id):
    new_id = list(new_id)
    ans = []
    spot_point = 0
    count = 0
    for i in new_id:
        if "a" <= i <= "z" or "0" <= i <= "9" or i == "-" or i == "_" or i == ".":
            count += 1
            if i == "." and spot_point == 0:
                if count == 1:
                    pass
                else:
                    ans.append(i)
                spot_point += 1

            elif i == "." and spot_point > 0:
                spot_point += 1
                continue
            else:
                spot_point = 0
                ans.append(i)
    if ans and ans[-1] == ".":
        ans.pop()
    if not ans:
        ans = ["a"]
    if len(ans) >= 16:
        ans = ans[:15]
        if ans and ans[-1] == ".":
            ans.pop()
    if len(ans) <= 2:
        last = ans[-1]
        while len(ans) < 3:
            ans.append(last)
    return ''.join(ans)

