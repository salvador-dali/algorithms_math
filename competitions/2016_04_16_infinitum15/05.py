# x, y, z = sqrt(k/3), sqrt(k/2), sqrt(k/6)
# f1 = (-3 + 2 * sqrt(2) + 2 * sqrt(3)) k
# f2 = 8 sqrt(6) * k^2
# f3 = k^2 + k - 1
# S(k) = |15 * k^2 + 4*k - 4|
mod = 10**9 + 7
mod_2_inverse = 500000004
def summation(n):
    return (5 * pow(n, 3, mod) + 19 * pow(n, 2, mod) * mod_2_inverse + n * mod_2_inverse) % mod

def fast_solution(a, b):
    return (summation(b) - summation(a - 1) + (8 if not a else 0)) % mod