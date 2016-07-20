# Prisoners' Names in Boxes
# https://en.wikipedia.org/wiki/100_prisoners_problem
# http://puzzling.stackexchange.com/questions/16/100-prisoners-names-in-boxes
# http://people.math.sfu.ca/~jtmulhol/math302/notes/25-Prisoners-in-Boxes.pdf
def H(n):
    s = 0
    for i in xrange(1, n + 1):
        s += 1. / i
    return s

def easy(n):
    return 1 - H(n) + H(n / 2)

for i in xrange(input()):
    n, k = map(int, raw_input().split())
    print easy(n)