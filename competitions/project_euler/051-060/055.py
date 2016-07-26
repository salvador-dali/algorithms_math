# straight forward implementation.
# too bored to write this thing for go
from collections import Counter

def reverse(n):
	return int(str(n)[::-1])

def lychrel(n):
	numbers, result = [], -1
	for i in xrange(60):
		numbers.append(n)
		r = reverse(n)
		if n == r:
			result = n
			break
		n += r

	return result

def main():
	c = Counter(lychrel(i) for i in xrange(1, 10000))
	c.pop(-1, None)
	key = max(c, key=c.get)
	print key, c[key]
main()
