# https://www.hackerrank.com/challenges/mathematical-expectation
# wrote brute force approach analysed solutions tried to find a pattern.
# Found that all of them is a polynomial ok K degree. Spent a lot of time figuring out a polynomial
import fractions

def solution(n, k):
    if k == 1:
        a = 2 * n - 4
        return fractions.Fraction(a, 3)
    if k == 2:
        a = 40 * n ** 2 - 144 * n + 131
        return fractions.Fraction(a, 90)
    if k == 3:
        a = 280 * n ** 3 - 1344 * n**2 + 2063 * n - 1038
        return fractions.Fraction(a, 945)
    if k == 4:
        n2 = n * n
        n3 = n2 * n
        n4 = n3 * n
        a = 2800 * n4 - 15680 * n3 + 28844 * n2 - 19288 * n + 4263
        return fractions.Fraction(a, 14175)
    if k == 5:
        n2 = n * n
        n3 = n2 * n
        n4 = n3 * n
        n5 = n4 * n
        a = 12320 * n5 - 73920 * n4 + 130328 * n3 - 29568 * n2 - 64150 * n - 5124
        return fractions.Fraction(a, 93555)

k, n = map(int, raw_input().split())
print ' / '.join(str(solution(n, k)).split('/'))