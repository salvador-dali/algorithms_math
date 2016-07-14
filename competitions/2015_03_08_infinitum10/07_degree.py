# http://en.wikipedia.org/wiki/Minimal_polynomial_(field_theory)
# http://math.stackexchange.com/questions/38763/how-to-find-a-polynomial-from-a-given-root
# http://www.mathpages.com/home/kmath111/kmath111.htm
# http://www.qc.edu.hk/math/Advanced%20Level/Polynomial%20Equations.htm
def printMatrix(m):
    for i in m:
        print i

def fromDigits(digits, b):
    # convert the array of digits to a number in base 10
    n = 0
    for d in digits:
        n = b * n + d
    return n

def factorization(n, how='list'):
    # factorize a number into list/set/dict of primes
    # can handle arbitrary huge number, with the only thing that the maximum prime should
    # be smaller then 17 digits prime: 51975335556428597. Then it will run approximately 1 minute
    # with 16 digits prime it will run approximately 5 seconds
    # 70804992178217648712301640058361235396058
    # [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 7, 7, 7, 7, 7, 7, 577, 577, 19237, 51975335556428597L]
    # is equal to
    def helper(n):
        # factorize the number to the list of integers
        # TODO needs nice explanation. Faster then easy method
        step = lambda x: 1 + (x << 2) - ((x >> 1) << 1)
        maxq = n ** 0.5
        d = 1
        q = n % 2 == 0 and 2 or 3
        while q <= maxq and n % q != 0:
            q = step(d)
            d += 1
        return q <= maxq and [q] + helper(n/q) or [n]

    arr = helper(n)
    if how == 'dict':
        res = {}
        for i in arr:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        return res

    if how == 'set':
        return set(arr)

    return arr

def removeSquares(d):
    newDict = set()
    for i in d:
        if d[i] % 2:
            newDict.add(i)

    return newDict

def GF2MatrixToNums(matrix):
    return sorted([fromDigits(i, 2) for i in matrix], reverse=True)

arr = [60, 22, 33, 330, 10]
squareFreePrimes = [removeSquares(factorization(i, 'dict')) for i in arr]
union = sorted(list(reduce(set.union, squareFreePrimes)))

matrix, l = [], len(union)
for i in squareFreePrimes:
    row = [0] * l
    for j in xrange(l):
        if union[j] in i:
            row[j] = 1
    matrix.append(row)


def GaloisRank(arr):
    values = arr[:]
    valSet = set(arr)
    print values
    print valSet


    for i in x:
        pass

arr = GF2MatrixToNums(matrix)
GaloisRank(arr)