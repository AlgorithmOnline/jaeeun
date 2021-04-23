def solution(numbers, hand):
    cellPhone = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
def solution(numbers, hand):
    cellPhone = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    person = {'left': [3, 0], 'right': [3, 2]}
    answer = ''

    def countDist(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            person["left"] = cellPhone[n]
        elif n == 3 or n == 6 or n == 9:
            answer += "R"
            person["right"] = cellPhone[n]
        else:
            dist = cellPhone[n]
            leftCost = countDist(dist, person["left"])
            rightCost = countDist(dist, person["right"])
            if leftCost < rightCost:
                answer += 'L'
                person["left"] = cellPhone[n]
            elif rightCost < leftCost:
                answer += "R"
                person["right"] = cellPhone[n]
            else:
                if hand == "right":
                    answer += "R"
                    person["right"] = cellPhone[n]
                else:
                    answer += 'L'
                    person["left"] = cellPhone[n]

    return answer
