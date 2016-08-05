from datetime import datetime

"""
Let $P(a, b) = \prod_{i=a}^{a + b - 1}i$
For example:
$P(1, 3) = \prod_{i=1}^{3}i = 1 \cdot 2 \cdot 3$
$P(7, 4) = \prod_{i=7}^{10}i = 7 \cdot 8 \cdot 9 \cdot 10$
$P(2, 5) = \prod_{i=2}^{6}i = 2 \cdot 3 \cdot 4 \cdot 5 \cdot 6$

and $Z(n, m, k) = \sum_{i=n}^{m}P(i, k)$
For example:
$Z(1, 3, 4) = \sum_{i=1}^{3}P(i, 4) = P(1, 4) + P(2, 4) + P(3, 4)$
$Z(3, 6, 8) = \sum_{i=3}^{6}P(i, 8) = P(3, 8) + P(4, 8) + P(5, 8) + P(6, 8)$


Given n, m, k and MOD, where
$0 \leq n \leq 10^16$
$n \leq m \leq 10^16$
$0 \leq k \leq 5 \cdot 10^6$
$1 \leq mod \leq 10^{16}$

your task is to find A(n, m, k, mod) = Z(n, m, k) % mod
for example:
$A(1, 3, 4, 10^9) = Z(1, 3, 4) % 10^9$ = 504 because
$Z(1, 3, 4) = \sum_{i=1}^{3}P(i, 4) = 1 \cdot 2 \cdot 3 \cdot 4 + 2 \cdot 3\cdot 4\cdot 5 + 3 \cdot 4 \cdot 5 \cdot 6 = 504$

$A(0, 3, 2, 10^9) = Z(0, 3, 2) % 10^9 = 20$ because
$Z(0, 3, 2) = \sum_{i=0}^{3}P(i, 2) = 0 \cdot 1 + 1 \cdot 2 + 2 \cdot 3 + 3 \cdot 4 = 20$

$A(5, 8, 0, 10^9) = Z(5, 8, 0) % 10^9 = 0$ because
$Z(5, 8, 0) = \sum_{i=5}^{8}P(i, 0) = 0$

and
$A(4, 12, 5, 123) = Z(4, 12, 5) % 123 = 102$ because
$Z(4, 12, 5) = \sum_{i=4}^{12}P(i, 5) = 4 \cdot 5 \cdot 6 \cdot 7 \cdot 8 + 5 \cdot 6 \cdot 7 \cdot 8 \cdot 9 + 6 \cdot 7 \cdot 8 \cdot 9 \cdot 10 + ... + 12 \cdot 13 \cdot 14 \cdot 15 \cdot 16 = 1481760
and 1481760 % 123 = 102


And at last few other tests:
A(28, 127, 19, 413 ) = 336
A(10, 53, 85, 672 ) = 0
A(22, 62, 55, 167 ) = 83
"""

def Z_brute(n, m, k, mod):
    def P(start, num):
        res = 1
        for i in xrange(start, start + num):
            res = (res * i) % mod

        return res

    total = 0
    for i in xrange(n, m + 1):
        t = P(i, k)
        total += t

    return total % mod

def Z(n, m, k, mod):
    def helper(a, b, mod):
        total, num = 1, a + 1
        for i in xrange(b, b + a + 1):
            if i % num == 0:
                multiple = (i / num) % mod
            else:
                multiple = i % mod

            total = (total * multiple) % mod

        return total

    return (helper(k, m, mod) - helper(k, n - 1, mod)) % mod

# from random import randint
# for i in xrange(3):
#     n = randint(0, 10**2)
#     m, k, mod = n + randint(0, 10**2), randint(0, 10**2), randint(1, 10**3)
#
#     a = Z_brute(n, m, k, mod)
#     b = Z(n, m, k, mod)
#     if a != b:
#         print n, m, k, mod, ' : ', a, b
#
#     print 'A(', n, m, k, mod, ') = ', b


n, m, k, mod = 10**15 - 2, 10**15, 5 * 10**6, 10**16 + 123
# startTime = datetime.now()
# a = Z_brute(n, m, k, mod)
# print datetime.now() - startTime


startTime = datetime.now()
b = Z(n, m, k, mod)
print datetime.now() - startTime

#print a
print b
#print a == b



# amazing probability problem:
# https://class.coursera.org/probability-001/lecture/209
# tableau 8.2f