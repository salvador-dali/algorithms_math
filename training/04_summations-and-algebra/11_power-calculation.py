# https://www.hackerrank.com/challenges/power-calculation

# last two digits of m**i for some i will become repetitive
# this finds out the length of the cycle for the repetitions
def findCycle(m):
    h, i, cycle = {}, 2, []
    while True:
        digits = m**i % 100
        if digits not in h:
            h[digits] = 1
            cycle.append(digits)
        else:
            break
        i += 1

    return i - 2, cycle

# gets the last two digits of k**n
def lastKtoPowerN(k, n):
    cycleNum, cycleList = findCycleHashed[k]
    return cycleList[(n - 2) % cycleNum]

findCycleHashed = {}
for i in xrange(1, 100):
    findCycleHashed[i] = findCycle(i)

# not all numbers should be calculated. Last 2 digits of everything
# bigger then 100 are already calculated. This can be simplified even further
def powerCalculations(k, n):
    # xrange(1, k + 1)
    # pre populate dictionary with various 2 digits
    h = {i: lastKtoPowerN(i, n) for i in xrange(1, 100)}

    s = k / 100 * sum(h.values())
    tmp = (k + 1) % 100
    for i in xrange(1, tmp if tmp else 100):
        s += h[i]

    return ('00' + str(s % 100))[-2:]


for i in xrange(input()):
    k, n = map(int, raw_input().split())
    print powerCalculations(k, n)


