# https://www.hackerrank.com/challenges/bus-station

# checks whether the number can be used to take all the groups of people in the bus
# it simply goes through the whole list of numbers and maintains the current sum. If it even passes above the sum
# then False, if it is equal to the number we are checking -> good, put sum to 0 and continue
def check(arr, n):
    s = 0
    for i in arr:
        s += i
        if s == n:
            s = 0
        if s > n:
            return False

    return True

# get the list of divisors of a number
# the main idea is to divide divisors into big and small and to remember that they come in pairs. So big = n / small
def getDivisors(n):
    small, large = [], []
    for i in xrange(1, int(n**0.5) + 1):
        if n % i == 0:
            small.append(i)
            if i != n / i:
                large.append(n / i)

    return small + large[::-1]

# main idea is to notice that buses can hold any number that is
# a divisor of the sum of the array and bigger then the maximum
def bus(arr):
    m = sum(arr)
    smallest = max(arr)
    possibleBuses = getDivisors(m)
    realBuses = []

    for i in possibleBuses:
        if i >= smallest and check(arr, i):
            realBuses.append(i)

    return realBuses

input()
arr = list(map(int, raw_input().split()))
print ' '.join(map(str, bus(arr)))