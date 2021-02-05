import math

x0, y0, r0, x1, y1, r1 = map(float, input().split())


def area(x0, y0, r0, x1, y1, r1):
    d = math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
    rr0 = r0 * r0
    rr1 = r1 * r1
    # Circles do not overlap
    if (d > r1 + r0):
        return 0
    # Circle1 is completely inside circle0
    elif (d <= abs(r0 - r1) and r0 >= r1):
        return math.pi * rr1
    # Circle0 is completely inside circle1
    elif (d <= abs(r0 - r1) and r0 < r1):
        # Return area of circle0
        return math.pi * rr0
    # Circles partially overlap
    else:
        phi = (math.acos((rr0 + (d * d) - rr1) / (2 * r0 * d))) * 2
        theta = (math.acos((rr1 + (d * d) - rr0) / (2 * r1 * d))) * 2
        area1 = 0.5 * theta * rr1 - 0.5 * rr1 * math.sin(theta)
        area2 = 0.5 * phi * rr0 - 0.5 * rr0 * math.sin(phi)

        # Return area of intersection
        return area1 + area2


answer = float(round(1000 * area(x0, y0, r0, x1, y1, r1)) / 1000)
print('%.3f' % answer)
