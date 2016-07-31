# https://www.hackerrank.com/challenges/eulers-criterion
def is_e(a, m):
    if m == 2 and a == 2:
        return False
    if m == 2 or a == 0:
        return True
    return pow(a, (m - 1) / 2, m) == 1

for i in xrange(input()):
    if is_e(*map(int, raw_input().split())):
        print 'YES'
    else:
        print 'NO'