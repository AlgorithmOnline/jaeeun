

def solution(distance, rocks, n):
    low = 1
    if len(rocks) - n == 0:
        return distance
    import math
    rocks.append(distance)
    midVisit = []
    rocks.sort()
    answer = 0
    high = math.ceil(distance / (len(rocks) - n))
    while low <= high:

        mid = (low + high) // 2
        # print("ans", answer, mid, midVisit)

        if mid in midVisit:
            break
        else:
            midVisit.append(mid)
        jumpCount = 0
        before = 0
        index = 0

        while index < len(rocks):
            if rocks[index] - before < mid:
                index += 1
                jumpCount += 1
                continue
            else:
                before = rocks[index]
                index += 1
        if jumpCount > n:
            high = mid + 1
        elif jumpCount <= n:
            if answer > mid:
                break
            else:
                answer = mid
                low = mid - 1

    return answer
