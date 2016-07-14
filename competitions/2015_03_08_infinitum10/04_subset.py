MOD = 10**9 + 7
# https://www.hackerrank.com/contests/infinitum10/challenges/number-of-subsets
# you are given a number N and the set {0, 1, ..., 2^N - 1}
# how many subsets are in this set that has xor equal to 0
# there will be 2^((2^n) - n)
for i in range(input()):
    n = input()
    print pow(2, (pow(2, n, MOD - 1) - n) % (MOD - 1), MOD)