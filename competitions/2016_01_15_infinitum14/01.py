from decimal import *

getcontext().prec = 20


def hypot(a, b):
    return (Decimal(a) ** 2 + Decimal(b) ** 2).sqrt()


arr_x, arr_y = [], []
for i in xrange(input()):
    x, y = map(int, raw_input().split())
    if x == 0:
        arr_y.append(y)
    else:
        arr_x.append(x)

min_x, max_x, min_y, max_y = min(arr_x), max(arr_x), min(arr_y), max(arr_y)

a1, a2 = max_x - min_x, max_y - min_y
b1, b2, b3, b4 = hypot(max_x, max_y), hypot(max_x, min_y), hypot(min_y, min_x), hypot(min_x, max_y)
el = max(a1, a2, b1, b2, b3, b4)
print el
