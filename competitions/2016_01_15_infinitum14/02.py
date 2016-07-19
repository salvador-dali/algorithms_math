mod = 10**9+7

def tangentMod(p, q, n):
    arr = map(int, bin(n)[2:])[::-1]
    val = (p * pow(q, mod - 2, mod)) % mod
    tans = [val]
    for i in xrange(len(arr) - 1):
        val = (2 * val * pow(1 - pow(val, 2, mod), mod - 2, mod)) % mod
        tans.append(val)

    val = 0
    for i in xrange(len(arr)):
        if arr[i]:
            val = (val + tans[i]) * pow(1 - (val * tans[i] % mod), mod - 2, mod) % mod
    return val

for i in xrange(input()):
    p, q, n = map(int, raw_input().split())
    print tangentMod(p, q, n)
