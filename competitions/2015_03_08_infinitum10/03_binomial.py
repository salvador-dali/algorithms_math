# https://www.hackerrank.com/contests/infinitum10/challenges/cheese-and-random-toppings
# https://www.hackerrank.com/challenges/cheese-and-random-toppings
def binomialCoefficient(n, k):
    # calculate binomial coefficient choose k out of n
    # http://en.wikipedia.org/wiki/Binomial_coefficient
    # first two ifs are not necessary (will work correctly even without them), but just for the sake of speed
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

    result = 1
    for i in xrange(1, k + 1):
        result = result * (n - i + 1) / i
    return result

def toDigits(n, b):
    # convert a number to an array of arbitrary base
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return digits[::-1]

def makeListSameSize(l1, l2, el=0):
    # makes two list of the same size, pre-pending el in the beginning of the array
    if len(l1) > len(l2):
        l2 = [el] * (len(l1) - len(l2)) + l2
    else:
        l1 = [el] * (len(l2) - len(l1)) + l1

    return l1, l2

def binomialCoefficientModuloPrime(n, m, p):
    # calculates binomial coefficient modulo prime
    # uses Lucas Theorem http://en.wikipedia.org/wiki/Lucas%27_theorem
    # http://math.stackexchange.com/a/95484/50804
    l1, l2 = makeListSameSize(toDigits(n, p), toDigits(m, p))

    res = 1
    for i in xrange(len(l1)):
        res = (res * binomialCoefficient(l1[i], l2[i])) % p
        if res == 0:
            return 0

    return res

def chinese_remainder(a, n):
    # solves the system of linear modular equations of the form
    # x = a[i] mod n[i]
    # returns the value of X, where A is the list of reminders, and n is the list of modulos
    # http://en.wikipedia.org/wiki/Chinese_remainder_theorem
    # http://math.stackexchange.com/a/95507/50804
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
    # calculates the prime factors of the number
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
