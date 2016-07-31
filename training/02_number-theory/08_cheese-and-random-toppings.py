# https://www.hackerrank.com/challenges/cheese-and-random-toppings
def binomialCoefficient(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

    result = 1
    for i in xrange(1, k + 1):
        result = result * (n - i + 1) / i
    return result

def toDigits(n, b):
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return digits[::-1]

def makeListSameSize(l1, l2, el=0):
    if len(l1) > len(l2):
        l2 = [el] * (len(l1) - len(l2)) + l2
    else:
        l1 = [el] * (len(l2) - len(l1)) + l1

    return l1, l2

def binomialCoefficientModuloPrime(n, m, p):
    l1, l2 = makeListSameSize(toDigits(n, p), toDigits(m, p))

    res = 1
    for i in xrange(len(l1)):
        res = (res * binomialCoefficient(l1[i], l2[i])) % p
        if res == 0:
            return 0

    return res

def chinese_remainder(a, n):
    def mul_inv(a, b):
        b0, x0, x1 = b, 0, 1
        if b == 1:
            return 1

        while a > 1:
            q = a / b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0

        if x1 < 0:
            x1 += b0

        return x1

    l, p, i, prod, sm = len(a), 1, 1, 1, 0
    for i in range(l):
        prod *= n[i]

    for i in range(l):
        p = prod / n[i]
        sm += a[i] * mul_inv(p, n[i]) * p
    return sm % prod

def factors(n):
    if n == 1:
        return [1]

    res, limit, check, num = [], int(n**0.5) + 1, 2, n
    for check in range(2, limit):
        while num % check == 0:
            res.append(check)
            num /= check
    if num > 1:
        res.append(num)
    return res

def main(n, m, p):
    if p == 1:
        return 0

    modulos, remainders = [], []
    for i in factors(p):
        modulos.append(i)
        remainders.append(binomialCoefficientModuloPrime(n, m, i))

    return chinese_remainder(remainders, modulos)

for i in xrange(input()):
    print main(*map(int, raw_input().split()))
