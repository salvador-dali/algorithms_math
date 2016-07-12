# ========== Modular arithmetic     ==========
def modInv(a, mod):
    # calculate the modular inverse for 1 number
    def egcd(a, b):
        # extended Eucledian algorithm
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            q, r = b / a, b % a
            m, n = x - u * q, y - v * q
            b, a, x, y, u, v = a, r, u, v, m, n
        GCD = b
        return GCD, x, y

    g, x, y = egcd(a, mod)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % mod

def modInvTill_n(n, mod):
    """calculate the modulo inverse for N numbers from 1 to N.
    It has 0 = 1 only for easiness of use
    explanation here: https://www.hackerrank.com/contests/infinitum9/challenges/demidenko-computer-virus/editorial
    1^(-1) % mod = 1
    i^(-1) $ mod = -floor(mod/i) * (mod % i)^(-1) % mod
    :param n:
    :param mod:
    :return:
    """
    x = [1] * n
    for i in xrange(2, n):
        x[i] = (mod - mod / i) * x[mod % i] % mod
    return x

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


# ========== Binomial Coefficient   ==========
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

def binomialCoefficientModulo(n, m, p):
    # calculate binomial coefficient modulo any square-free number
    # uses chinese reminder theorem and lucas theorem
    def factors(n):
        # calculates the prime factors of the number
        # TODO rewrite it in a nicer way
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

    if p == 1:
        return 0

    modulos, remainders = [], []
    for i in factors(p):
        modulos.append(i)
        remainders.append(binomialCoefficientModuloPrime(n, m, i))

    return chinese_remainder(remainders, modulos)


# ========== Different Numbers      ==========
def isTriangular(n):
    """Checks if the number is triangular.
    just solve the square equation in O(1)
    :param n:
    :return:
    """
    return not (8 * n + 1)**0.5 % 1

def Delannoy(a, b, MOD):
    """Delannoy numbers calculate:
    - number of paths from 0, 0 to a, b using left, right, diagonal
    - number of a dim points that have Manhattan distance at most b from origin
    - number of global alignments of 2 sequences len a and b

    D(a, b) = D(a-1, b) + D(a, b-1) + D(a-1, b-1) - straightforward O(n^2) method
    better one is http://math.stackexchange.com/a/1068843/50804 with binomial formula
    which can be calculated in O(min(a, b))

    If a = b, then there is an easier way to calculate Delannoy
    :param a:
    :param b:
    :param MOD:
    :return:
    """
    s, prev, m = 1, 1, min(a, b) + 1
    inv_square2 = [2 * i * i % MOD for i in modInvTill_n(m, MOD)]
    for i in xrange(1, m):
        prev = (prev * (a - i + 1) * (b - i + 1) * inv_square2[i]) % MOD
        if prev == 0:
            break

        s += prev
    return s % MOD


# ========== Random stuff           ==========
def toFraction(numerator, denominator):
    # converts any numerator/denominator to a fraction 8/9.
    # 0 is converted to 0/1, any number like 9/81 is 1/9
    from fractions import Fraction
    s = str(Fraction(numerator, denominator))
    if len(s.split('/')) != 2:
        return s + '/1'
    return s

def findGenerator(p):
    # find a generator for a multiplicative group modulo prime
    # https://www.hackerrank.com/contests/infinitum9/challenges/minion-of-the-year/editorial
    def isGenerator(g, p, factors):
        for i in factors:
            if i < p - 1:
                if pow(g, i, p) == 1:
                    return 0

        return 1

    factors = getDivisors(p - 1)
    g = 1
    while not isGenerator(g, p, factors):
        g += 1

    return g

def toDigits(n, b):
    # convert a number to an array of arbitrary base
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return digits[::-1]

def fromDigits(digits, b):
    # convert the array of digits to a number in base 10
    n = 0
    for d in digits:
        n = b * n + d
    return n

def makeListSameSize(l1, l2, el=0):
    # makes two list of the same size, pre-pending el in the beginning of the array
    l = [el] * abs(len(l1) - len(len(l2)))
    if len(l1) > len(l2):
        l2 = l + l2
    else:
        l1 = l + l1

    return l1, l2

def dLog(a, b, m):
    """
    Solves the discrete algorithm: $a^x \bmod m = b$, finds x.
    It uses baby-step, giant step approach.

    my implementation:
    https://www.hackerrank.com/contests/infinitum11/challenges/discrete-logarithm/submissions/code/3126436
    :param a:
    :param b:
    :param m:
    :return:
    """
    k, A, c = int(m**0.5) + 1, {}, 1
    for i in xrange(k):
        if c in A:
            return -1
        if c == b:
            return i
        A[c] = i
        c = c * a % m
    inv, c = modInv(c, m), 1
    for i in xrange(k):
        if c * b % m in A:
            return k * i + A[c * b % m]
        c = c * inv % m
    return -1

def permutationSign(arr, debug=False):
    """for a permutation check all $i < j$ and count all of them that produce f(i) > f(j). Let it be x
    sign = (-1)^x. If x = -1, permutation is odd, otherwise evens..
    Here it is in O(n^2), but parity can be calculated in O(n)
    http://stackoverflow.com/q/20702782/1090562
    """
    total = 0
    for i in xrange(len(arr)):
        for j in xrange(i + 1, len(arr)):
            if arr[i] > arr[j]:
                if debug: print "{" + str(i) + ", " + str(j) + "}"
                total += 1
    if total % 2:
        return -1, 'odd'
    return 1, 'even'

def firstDigits(n, m, k):
    """ get first K digits of N^M
    https://www.hackerrank.com/challenges/ajourney
    """
    import decimal
    ln10 = decimal.Decimal(10).ln()
    lnN = decimal.Decimal(n).ln()
    sqrt10 = decimal.Decimal(10).sqrt()
    a = ((m * lnN / ln10 - decimal.Decimal(0.5)) % 1) * ln10
    return int(str(sqrt10 * a.exp()).replace(".", "")[0:k])
