def FibonacciBig(n, c={0:1, 1:1}):
    # calculates a gcd of a very large number modulo something else. Almost any number can be passed
    # can calculate 10**7 without MOD in 3 seconds. With normal Fibonacci 10**6 can be calculated in 15 seconds
    # N.B. it is shifted by one, so if the F(n) should be calculated, n + 1 should be passed
    MOD = 10**9 + 7
    if n not in c:
        x = n / 2
        c[n] = (FibonacciBig(x - 1) * FibonacciBig(n - x - 1) + FibonacciBig(x) * FibonacciBig(n - x)) % MOD
    return c[n]

def Fibonacci_fastDoubling_helper(n):
    """Do not use this method by itself. It just a helper for a couple of
    Fibonacci functions
    """
    if not n:
        return 0, 1

    a, b = Fibonacci_fastDoubling_helper(n / 2)
    tmp = a ** 2
    c, d = 2 * a * b - tmp, b ** 2 + tmp
    return (d, (c + d)) if n % 2 else (c, d)

def Fibonacci_fastDoubling(n):
    # O(log(N)) algorithm which relies on the following property
    # http://en.wikipedia.org/wiki/Fibonacci_number
    # it is derived from a matrix from removing redundant calculation
    # helper returns [F(n) and F(n + 1)]
    #
    # takes approximately the same amount of time as FibonacciBig
    # if you need MOD, then just add it to the return statement
    return Fibonacci_fastDoubling_helper(n)[0]

def fibonacci_starting(a, b, n):
    # if you start your fibonacci sequence with a, b then
    # 1a,   0b
    # 0a,   1b
    # 1a,   1b
    # 1a,   2b
    # 2a,   3b
    # 3a,   5b
    # 5a,   8b
    # and it is clear that the numbers are from the fibonacci sequence shifted by 1
    # all is needed is to calculate two previous fibonacci numbers and to multiply them by a and b

    # helper is taken from Fibonacci_fastDoubling
    # converting to MOD is straightforward
    if not n:
        return a

    x1, x2 = Fibonacci_fastDoubling_helper(n - 1)
    return x1 * a + x2 * b

def presentationAsFibonacci(n):
    # Any number can be presented as a sum of Fibonacci numbers
    # notice that there are no 2 consecutive Fibonacci numbers
    # works in log time, so super huge N can be used
    # greedy algorithm which selects the biggest Fib number, which is less then N, then N -= thatFib works fine
    # this returns the array which looks as [1, 0, 0, 1, 0] which means that it is the sum of 5-th number and 2 number
    # 5-th = 8 and 2-nd = 2

    from bisect import bisect_right
    # get the hash of all Fib numbers smaller then N. I
    # f many times function should be invoked, it is nice to cache the result
    # looks like this can be improved further (I am two times slower then the best guy).
    # read here: https://www.hackerrank.com/contests/infinitum8/challenges/chandrima-and-xor
    fibList = [1, 1]
    while fibList[-1] < n:
        fibList.append(fibList[-1] + fibList[-2])

    # start a greedy algorithm
    num = 0
    while True:
        pos = bisect_right(fibList, n) - 1
        if n <= 0:
            break

        num += 1 << (pos - 1)
        n -= fibList[pos]

    return num

def FibonacciQueries(arr):
    # you need to calculate many Fibonacci number from the range from 1 to N
    # N is known beforehand and the number of queries is much less then n
    # https://www.hackerrank.com/contests/infinitum10/challenges/fibonacci-lcm/editorial
    # TODO how to solve it
    pass

def numberOfBinaryStringsWithNoRepeatedZeros(n):
    """Let F(n) is the number of binary string of length N with no repeated zeros
    It can end with either 0 or 1. If it ends with 1 than the number is equal to xxxxx1
    F(n-1). If it ends with 0, than the previous element should be 1. So the string is F(n-2)
    So it is a fibonacci sequence http://math.stackexchange.com/q/81805/50804

    Another way of looking into it is by calculating the number of m zeros and k ones, where
    m + k = n. It will be binomial. Now sum them all
    """
    return FibonacciBig(n + 1)

print numberOfBinaryStringsWithNoRepeatedZeros(12)