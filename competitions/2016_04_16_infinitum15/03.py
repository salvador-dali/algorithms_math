def find_solutions(p, k, n):
    mod, res = n % p, []
    for i in xrange(p):
        if pow(i, k, p) == mod:
            res.append(i)

    return res

p, N = map(int, raw_input().split())
for i in xrange(N):
    k, n = map(int, raw_input().split())
    res = find_solutions(p, k, n)
    if not res:
        print 'NONE'
    else:
        print ' '.join(map(str, res))