# https://www.hackerrank.com/challenges/sherlock-and-planes/
# 4 points are on the same plane if the volume of the thing is 0
# x1 y1 z1 1
# x2 y2 z2 1
# x3 y3 z3 1
# x4 y4 z4 1
# actually this can be translated to a higher dimensions
def fourPointsOnPlane(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
    def determinant(a1, a2, a3, a4, a5, a6, a7, a8, a9):
        return a1 * (a5 * a9 - a6 * a8) - a2 * (a4 * a9 - a6 * a7) + a3 * (a4 * a8 - a5 * a7)

    return x1 * determinant(y2, z2, 1, y3, z3, 1, y4, z4, 1) - y1 * determinant(x2, z2, 1, x3, z3, 1, x4, z4, 1) + z1 * determinant(x2, y2, 1, x3, y3, 1, x4, y4, 1) - determinant(x2, y2, z2, x3, y3, z3, x4, y4, z4)

for i in xrange(input()):
    arr = map(int, raw_input().split()) + map(int, raw_input().split()) + map(int, raw_input().split()) + map(int, raw_input().split())
    print 'NO' if fourPointsOnPlane(*arr) else 'YES'