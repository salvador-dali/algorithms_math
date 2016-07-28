from decimal import *

n = input()
precision = input()

getcontext().prec = precision + 6

numbers = set(range(2, n + 1)) - set(i*i for i in xrange(2, int(n**0.5) + 10))

s = 0
for j in numbers:
	a = str(Decimal(j).sqrt()).replace(".", "")
	s += sum(int(i) for i in a) - int(a[-1]) - int(a[-2]) - int(a[-3]) - int(a[-4]) - int(a[-5]) - int(a[-6])

print s