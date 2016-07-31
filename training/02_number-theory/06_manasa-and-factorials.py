# https://www.hackerrank.com/challenges/manasa-and-factorials
# the main idea is to have a fast helper to calculate the number of zeros in the factorial
# after this with the help of the binary search find the location of the the correct element
def numberOfZerosInFactorial(n):
    k = 0
    while n / 5:
        n /= 5
        k += n

    return k

def smallestFactorialWithNZeros(n):
    rightEstimate, test = 5 * n, numberOfZerosInFactorial(5 * n)
    if test == n:
        return rightEstimate

    while test > n:
        lastRightEstimate = rightEstimate
        rightEstimate = int(rightEstimate * 0.9)
        test = numberOfZerosInFactorial(rightEstimate)

    left, right = rightEstimate, lastRightEstimate
    middle = (left + right) / 2

    while middle != n:
        if numberOfZerosInFactorial(middle) < n:
            left = middle
        else:
            right = middle

        middleNew = (left + right) / 2
        if middleNew == middle:
            break

        middle = middleNew

    tmp = numberOfZerosInFactorial(middle)
    while tmp >= n:
        middle -= 1
        tmp = numberOfZerosInFactorial(middle)
    else:
        return middle + 1

for i in xrange(input()):
    print smallestFactorialWithNZeros(input())