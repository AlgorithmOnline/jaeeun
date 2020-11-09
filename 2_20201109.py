def solution(n):
    result = []
    i = 0
    while n > 0:
        d = 3 ** i
        while (n - d) % 3 ** (i + 1) != 0:
            d += 3 ** i
        result.append(d // 3 ** i)
        n = n - d;
        i += 1
    return "".join(map(str,[4 if i==3 else i for i in result][::-1]))

