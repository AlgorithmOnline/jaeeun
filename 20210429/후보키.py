import itertools


def solution(relation):
    answers = 0
    rss = len(relation[0])
    success = []
    count = 1
    while count <= rss:
        s = list(itertools.combinations(list(range(rss)), count))
        for i in s:  # i 가 list 문치
            i = set(i)
            flag = True  # 답일수 있는 확률률
            for ee in success:
                if ee.issubset(i):
                    flag = False  # 답일 수 없음
                    break
            if not flag:
                continue
            setti = set([])
            for k in relation:
                a = ""
                for m in i:
                    a += "👩" + str(k[m])
                setti.add(a)
            if len(setti) == len(relation):
                answers += 1
                success.append(i)

        count += 1

    return answers

