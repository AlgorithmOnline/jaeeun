while 1:
    lines  = list(map(int, input().split()))
    if 0 in lines:
        break
    else:
        lines.sort()
        if lines[0] ** 2 + lines[1]**2 ==lines[2]**2:
            print("right")
        else:
            print("wrong")
