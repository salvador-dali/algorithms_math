"""
https://www.hackerrank.com/challenges/lexicographic-steps
generate all possible paths (in order) for all possible x, y. Store them in hash
and extract the one needed

Possible improvement is not to calculate symmetrical values
"""

def all_ways(x, y):
    def generate(x, y, s):
        if x + y == 0:
            l.append(s)
            return

        if x > 0:
            generate(x - 1, y, s + 'H')
        if y > 0:
            generate(x, y - 1, s + 'V')

    l = []
    generate(x, y, '')
    return l

def createHash():
    d = {}
    for x in xrange(1, 11):
        for y in xrange(1, 11):
            d[(x, y)] = all_ways(x, y)

    return d

d = createHash()
for i in xrange(input()):
    x, y, k = map(int, raw_input().split())
    print d[(x, y)][k]