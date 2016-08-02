# https://www.hackerrank.com/challenges/triangle-numbers
# this is called Trinomial triangle
# http://en.wikipedia.org/wiki/Trinomial_triangle
# which did not helped me at all during this challenge
# I just reviewed a few rows (which is really hard to do manually)
# and so the following sequence
# 1     -1
# 2     -1
# 3     2
# 4     3
# 5     2
# 6     4
# 7     2
# 8     3
# 9     2
#10     4
# and the pattern emerges
def trinomial(n):
    if n < 2:
        return -1

    h = {
        0: 2,
        1: 3,
        2: 2,
        3: 4
    }
    return h[(n - 3) % 4]

for i in xrange(input()):
    print trinomial(input())