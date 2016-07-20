import math

def dot_product(v1, v2):
    return sum(a*b for a, b in zip(v1, v2))

def length(v):
    return math.sqrt(dot_product(v, v))

def angle(p1, p2, p3):
    v1 = (p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2])
    v2 = (p3[0] - p2[0], p3[1] - p2[1], p3[2] - p2[2])
    return math.acos(dot_product(v1, v2) / (length(v1) * length(v2)))

def expected(points):
    s, c = 0., 0.
    for i in xrange(len(points)):
        for j in xrange(i + 1, len(points)):
            for k in xrange(j + 1, len(points)):
                s += angle(points[i], points[j], points[k])
                c += 1

    return s / c

points = []
for _ in xrange(input()):
    points.append(map(int, raw_input().split()))
print expected(points)