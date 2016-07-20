mod = 10**9 + 7
def precomp_factorial(n):
    arr = [1]
    for i in xrange(1, n):
        arr.append(arr[-1] * i % mod)
    return arr

res = precomp_factorial(2 * 10**6 + 5)

def C(n, k):
    return (res[n] * pow(res[k], mod - 2, mod) * pow(res[n - k], mod - 2, mod)) % mod

for _ in xrange(input()):
    n, k = map(int, raw_input().split())
    print C(n - 1, k - 1)