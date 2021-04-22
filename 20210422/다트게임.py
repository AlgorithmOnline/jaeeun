def solution(dartResult):
    stack = []
    dartResult = list(dartResult)
    lenDart = len(dartResult)
    index = 0
    answer = 0
    while index < lenDart:
        if dartResult[index] == "*":
            back = []
            if len(stack) > 0:
                back.append(2 * stack.pop())
            if len(stack) > 0:
                back.append(2 * stack.pop())
            while back:
                stack.append(back.pop())
            index += 1
            continue

        elif dartResult[index] == "#":
            if len(stack) > 0:
                stack.append(-1 * stack.pop())
            index += 1
            continue
        else:
            if dartResult[index + 1] != "S" and dartResult[index + 1] != "T" and dartResult[index + 1] != "D":
                index += 1
                dartResult[index] = 10
            if dartResult[index + 1] == "S":
                stack.append(int(dartResult[index]) ** 1)
                index += 2
            elif dartResult[index + 1] == "D":
                stack.append(int(dartResult[index]) ** 2)
                index += 2
            elif dartResult[index + 1] == "T":
                stack.append(int(dartResult[index]) ** 3)
                index += 2
    return sum(stack)
