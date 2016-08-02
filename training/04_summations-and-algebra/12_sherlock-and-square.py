# https://www.hackerrank.com/challenges/sherlock-and-square
# this is a sum of geometric progression + 4
def lengthOfLines(n):
    return (2 + pow(2, n + 1, 1000000007)) % 1000000007

for i in xrange(int(raw_input())):
    print lengthOfLines(int(raw_input()))