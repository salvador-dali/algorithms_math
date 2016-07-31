# https://www.hackerrank.com/challenges/number-of-subsets
# after running a bruteforce justChecking, and looking for values in the oeis, I found this
# http://oeis.org/A000105 which happened to be the right sequence
# so here we have to calculate 2^(2^n - n) mod prime
def justChecking():
    from itertools import chain, combinations
    def powerset(s):
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


    def analyse(n):
        total = 0
        for i in powerset(range(pow(2, n))):
            ans = reduce(lambda a, b: a ^ b, i, 0)
            if not ans:
                total += 1

        print n, total

    for i in xrange(1, 5):
        analyse(i)

MOD = 10**9 + 7
for i in range(input()):
    n = input()
    print pow(2, (pow(2, n, MOD - 1) - n) % (MOD - 1), MOD)