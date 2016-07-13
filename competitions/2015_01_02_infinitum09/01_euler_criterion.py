# https://www.hackerrank.com/contests/infinitum9/challenges/eulers-criterion
# https://www.hackerrank.com/challenges/eulers-criterion
# reading a simple explanation about the solution here http://en.wikipedia.org/wiki/Euler%27s_criterion
# do not forget about some corner cases with m == 2 and a == 0
def is_e(a, m):
    if m == 2 and a == 2:
        return False
    if m == 2 or a == 0:
        return True
    return pow(a, (m - 1) / 2, m) == 1

for i in xrange(input()):
    print 'YES' if is_e(*map(int, raw_input().split())) else 'NO'