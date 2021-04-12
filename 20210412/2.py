def solution(s):
    ans = len(s)

    if len(s) == 1:
        return 1
    for cut in range(1, len(s) // 2 + 1):
        result = ""
        count = 1
        before = s[:cut]
        for i in range(cut, len(s), cut):
            if s[i:i + cut] == before:
                count += 1
            else:
                if count == 1:
                    result += before
                else:
                    result += str(count) + before
                before = s[i:i + cut]
                count = 1
        if count == 1:
            result += before
        else:
            result += str(count) + before
        ans = min(ans, len(result))
    return ans
