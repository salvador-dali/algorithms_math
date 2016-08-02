# https://www.hackerrank.com/challenges/little-gaurav-and-sequence

# bruteforce implementation to check for patterns
def investigation(n):
    i, s = 0, 0
    while 2**i <= n:
        subSum = 0
        for j in xrange(n + 1):
            subSum += 2 ** (2 ** i + 2 * j)

        s += subSum
        i += 1
    return s

def patterns(n):
    pattern = []
    for i in xrange(1, n):
        pattern.append(investigation(i) % 10)

    return pattern

# after looking for the pattern, I can see that
# all even number result in 0 in the end
# for odd number it is more complicated. The numbers follow the sequence: 6, 2, 8, 4, 0 which loops over
# each number shows up 2^i times. So
# 6 is 1 time,
# 2 is 2 times and
# 8 -> 4
# 4 -> 8
# 0 -> 16 and then it continues further
# 6 -> 32
# 2 -> 64
#
# sum of the geometric progression (a^(n + 1) - 1) / (a - 1) with a = 2
# 2^(n + 1) - 1
# knowing this it is possible to get the position of the index, and then check what number should correspond to it
from math import log
def real(number):
    if number & 1:
        return 0

    arr = [6, 2, 8, 4, 0]
    approximate = int(log(number + 1, 2))
    return arr[(approximate - 1) % len(arr)]

for i in xrange(input()):
    print real(input())
