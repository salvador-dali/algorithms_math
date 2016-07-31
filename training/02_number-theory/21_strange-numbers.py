# https://www.hackerrank.com/challenges/strange-numbers
# checking all the numbers are not feasible.
# so to reduce the space of checks, one can notice that every potential strange number should be
# created in the way: strangeNumber * (len(strangeNumber) + i), where i can be 0, 4
# there is not really a lot of these strange numbers.
# so we can pre-calculate them and store.
# for each test case we check how many of them are in the interval
strange = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def isStrange(number):
    arrOfStrange = []
    while number not in strange:
        n = len(str(number))
        if number % n:
            return False
        arrOfStrange.append(number)
        number /= n

    for i in arrOfStrange:
        if i not in strange:
            strange.append(i)
    return True

def generateStrange():
    cur = 1
    while cur < len(strange):
        num = strange[cur]

        for i in xrange(4):
            candidate = num * (len(str(num)) + i)
            if candidate < 3*10**18:
                isStrange(candidate)

        cur += 1

def findNumber(start, end):
    num = 0
    for i in strange:
        if start <= i <= end:
            num += 1
    return num

generateStrange()

for i in xrange(input()):
    a, b = map(int, raw_input().split())
    print findNumber(a, b)