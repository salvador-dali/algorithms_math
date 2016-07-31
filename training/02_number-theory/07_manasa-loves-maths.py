# https://www.hackerrank.com/challenges/manasa-loves-maths
# the number is divisible by 8 only if the last 3 numbers are divisible by 8
# so create a list of hashes of all possible numbers from 1 to 1000 which are divisible by 8
# then create the hash2 of the number and check whether at least one of the hashes in a list is in hash2

from itertools import permutations
def createCache():
    arr = []
    for i in xrange(0, 1000/8):
        small = list(('00' + str(i * 8))[-3:])
        h = {}
        for j in small:
            if j not in h:
                h[j] = 1
            else:
                h[j] += 1
        arr.append(h)

    return arr

def isPermutationDivisible(num):
    if num < 1000:
        s = list(str(num))
        for i in permutations(s):
            if int(''.join(i)) % 8 == 0:
                return True
        return False


    numberCache = {}
    for i in str(num):
        if i in numberCache:
            numberCache[i] += 1
        else:
            numberCache[i] = 1

    for el in cache:
        flag = True
        for i in el:
            if i not in numberCache or numberCache[i] < el[i]:
                flag = False

        if flag:
            return True

    return False

cache = createCache()
for i in xrange(input()):
    print 'YES' if isPermutationDivisible(input()) else 'NO'