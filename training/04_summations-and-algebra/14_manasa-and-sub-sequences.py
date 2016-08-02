# https://www.hackerrank.com/challenges/manasa-and-sub-sequences/
# after checking a few elements like ab, abc, abcd you can see that
# total sum will be (l - the length of the number):
# a * 2^0 * 11^(l - 1) + b * 2^1 * 11^(l - 2) + ... + z * 2^(l - 1) * 11^0
def sum_subsequence(s):
    total, l, mod = 0, len(s), 10**9 + 7
    for i in xrange(l):
        total = (total + int(s[i]) * pow(2, i, mod) * pow(11, l - i - 1, mod)) % mod

    return total

print sum_subsequence(raw_input())