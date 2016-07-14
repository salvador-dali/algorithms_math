#MOD = 10**9 + 7

from random import randint
# rands = [randint(1, 10**9) for i in xrange(100)]
# def gcd_multiple(arr):
#     return reduce(gcd, arr)
# def gcd_fib(arr):
#     GCD = gcd_multiple(arr)
#     return fibonacci(GCD)
# def lcm_multiple(arr):
#     return reduce(lcm, arr)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def fibonacci(n):
    def helper(n):
        if n == 0:
            return 0, 1

        a, b = helper(n / 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2:
            return d, (c + d)
        else:
            return c, d

    return helper(n)[0]

def modInv(a, mod):
    def egcd(a, b):
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

def divisibleMod(a, b, mod):
    return ((a % mod) * modInv(b, mod)) % mod

def fibonacci_mod(n, mod):
    def helper(n):
        if n == 0:
            return 0, 1

        a, b = helper(n / 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2:
            return d % mod, (c + d) % mod
        else:
            return c % mod, d % mod

    return helper(n)[0]

def lcm_fibonacci_brute(a, b):
    f1, f2 = fibonacci(a), fibonacci(b)
    return lcm(f1, f2)

def lcm_fibonacci_2(a, b, mod):
    x = (fibonacci_mod(a, mod) * fibonacci_mod(b, mod) % mod)
    y = fibonacci_mod(gcd(a, b), mod)
    return divisibleMod(x, y, mod)

def lcm_multiple(arr):
    return reduce(lcm, arr)

def lcm_multiple_mod(arr, mod):
    a1, a2 = arr.pop(), arr.pop()
    l = lcm(a1, a2) % mod
    while len(arr):
        l = lcm(l, arr.pop()) % mod

    return l

arr = [7, 23, 12, 98, 16]
mod = 577
print lcm_multiple(arr) % mod
print lcm_multiple_mod(arr, mod)

