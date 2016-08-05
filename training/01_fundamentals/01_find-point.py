# https://www.hackerrank.com/challenges/find-point
# if the point of symmetry is in the center (0, 0)
# then the symmetry of A (x, y) is (-x, -y)
# So to move the S (x, y) in the center you need to subtract numbers
# so for one coordinate it will be:
# -(a - s) + s = -a +2s
def symmetricalPoint(aX, aY, sX, sY):
    return -aX + 2 * sX, -aY + 2 * sY 

for i in xrange(input()):
    print ' '.join(map(str, symmetricalPoint(*map(int, raw_input()))))