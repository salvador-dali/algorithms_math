# https://www.hackerrank.com/challenges/sherlock-and-probability
# the probability can be found as valid / total, where total is len(s)**2. Valid can be found in
# O(n), noticing that the number of values in a string of length K (assuming that i - j <=k) will
# be equal to the number of 1s in this string squared. After this, notice that the while iterating
# through this number by one element at a time, some of the values will be intersecting.
from Queue import Queue
from fractions import Fraction

def probability(s, k):
    q, n, intersection, total = Queue(), 0, 0, 0
    for _ in s[0:k + 1]:
        i = int(_)
        q.put(i)
        if i:
            n += 1

    total += n**2 - intersection**2
    for _ in xrange(k + 1, len(s)):
        addedElement = int(s[_])
        removedElement = q.get()
        q.put(addedElement)
        tmp = n + addedElement - removedElement
        intersection = n - removedElement
        if addedElement:
            total += tmp**2 - intersection**2
        n = tmp

    return total

def formatting(numerator, denominator):
    s = str(Fraction(numerator, denominator))
    if len(s.split('/')) != 2:
        return s + '/1'
    return s

def res(s, k):
    l = probability(s, k)
    total = len(s)**2
    print formatting(l, total)

for i in xrange(input()):
    _, k = map(int, raw_input().split())
    res(raw_input(), k)