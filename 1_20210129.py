from sys import stdin


if __name__ == "__main__":
    s, t = [list(stdin.readline().strip()) for _ in range(2)]

    while len(s) != len(t):
        if t[-1] == 'A':
            t.pop()
        else:
            t.pop()
            t = t[::-1]

    print(1 if s == t else 0)
