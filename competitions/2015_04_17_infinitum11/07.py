# https://www.hackerrank.com/contests/infinitum11/challenges/fibonacci-gcd-again
# The question asks to find a GCD of two numbers
# a_0 \cdot F_n + a_1 \cdot F_{n+1} + a_2 \cdot F_{n+2}
# b_0 \cdot F_n + b_1 \cdot F_{n+1} + b_2 \cdot F_{n+2}
#
# first of all it is obvious that it can be changed to
# (a_0 + a_1)\cdot F_n + (a_1 + a_2) \cdot F_{n+1}
#
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def Fibonacci_fastDoubling(n):
    def Fibonacci_fastDoubling_helper(n):
        if not n:
            return 0, 1

        a, b = Fibonacci_fastDoubling_helper(n / 2)
        tmp = a ** 2
        c, d = 2 * a * b - tmp, b ** 2 + tmp
        return (d, (c + d)) if n % 2 else (c, d)

    return Fibonacci_fastDoubling_helper(n)[0]

def fibonacci_starting(a, b, n):
    if not n:
        return a

    x1, x2 = Fibonacci_fastDoubling_helper(n - 1)
    return x1 * a + x2 * b



def calc(a1, a2, a3, n):
    b1 = a1 + a3
    b2 = a2 + a3
    return fibonacci_starting(b1, b2, n + 1)

a = calc(15, 37, 13, 12)
b = calc(5, 7, 3, 10)



a1, a2, n, m = 2, 5, 17, 18
a = fibonacci_starting(a1, a2, n)
b = fibonacci_starting(a1, a2, m)
print gcd(a, b)





