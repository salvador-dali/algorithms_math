# https://www.hackerrank.com/contests/infinitum9/challenges/difference-and-product
# https://www.hackerrank.com/challenges/difference-and-product
# solving the equation and finding the roots, paying attention to some cases where roots do not exist:
# for example when you have D < 0 or when d < 0
# then knowing the roots checking whether they are integers. If they are making the last check if they are
# satisfying the equation. After it storing all of them in the set and checking the length of the set
def number(d, p):
    def check(x, y, d, p):
        return abs(x - y) == d and x * y == p

    if d < 0:
        return 0
    if d == 0 and p == 0:
        return 1
    if d == 0 and p < 0:
        return 0

    if p == 0:
        return 4

    disc = d**2 + 4.0 * p
    if disc < 0:
        return 0

    y1 = (-d + disc**0.5)/2.0
    if y1:
        x1 = p / y1
        x1, y1 = int(x1), int(y1)
    else:
        x1, y1 = 0, 0

    y2 = (-d - disc**0.5)/2.0
    if y2:
        x2 = p / y2
        x2, y2 = int(x2), int(y2)
    else:
        x1, y1 = 0, 0

    y3 = (d - disc**0.5)/2.0
    if y3:
        x3 = p / y3
        x3, y3 = int(x3), int(y3)
    else:
        x3, y3 = 0, 0

    y4 = (d + disc**0.5)/2.0
    if y4:
        x4 = p / y4
        x4, y4 = int(x4), int(y4)
    else:
        x1, y1 = 0, 0

    s = set([])
    for x, y in [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]:
        if check(x, y, d, p):
            s.add(str(x) + '_' + str(y))

    return len(s)

for i in xrange(input()):
    print number(*map(int, raw_input().split()))