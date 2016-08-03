# https://www.hackerrank.com/challenges/stars
# for every possible 2 points check the sum of the weights above and below the the line
# (not taking into the account these two points). Then also try different combinations with these
# points it can be 2 points above the line, 2 points below the line, 1 point above, one below
import itertools
def betterWeight(m_weight, a, b):
    return max(m_weight, min(a, b))

def crossProduct(p1, p2, px):
    return (p2[0] - p1[0]) * (px[1] - p1[1]) - (p2[1] - p1[1]) * (px[0] - p1[0])

def bestWeight(points):
    w = 0
    for p1, p2 in itertools.combinations(points, 2):
        above, below = 0, 0
        for px in points:
            if px != p1 and px != p2:
                if crossProduct(p1, p2, px) > 0:
                    above += px[2]
                else:
                    below += px[2]

        w = betterWeight(w, above + p1[2] + p2[2], below)
        w = betterWeight(w, above + p1[2], below + p2[2])
        w = betterWeight(w, above + p2[2], below + p1[2])
        w = betterWeight(w, above, below + p1[2] + p2[2])
    return w

points = [map(int, raw_input().split(' ')) for i in xrange(input())]
print bestWeight(points)