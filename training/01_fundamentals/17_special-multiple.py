# https://www.hackerrank.com/challenges/special-multiple
# in the beginning generates a cache which stores all the possible values from 1 to 500 till
# where the value is the smallest number which is divisible by this key
import itertools
def generateHash():
    h = {i: 1 for i in range(1, 500)}
    cache = {}

    for i in itertools.product([0, 9], repeat=13):
        n = int(''.join(map(str, i)))
        if n:
            toRemove = []
            for j in h:
                if n % j == 0:
                    cache[j] = n
                    toRemove.append(j)

            for j in toRemove:
                del h[j]

    return cache

cache = generateHash()

for i in xrange(input()):
    print cache[input()]