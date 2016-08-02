# https://www.hackerrank.com/challenges/shashank-and-list
# calculates all possible sublists of the list, for each of this sublists get their sum
# if s_i is the sum, then we need to calculate the following sum: 2^s_i
#
# I started with a list of two elements a + b
# and saw that S = 2^a + 2^b + 2^(a+b) = (1 + 2^a)(1 + 2^b) -1
# then I checked that for each list S = (1 + 2^a)(1 + 2^b)*...*(1 + 2^z) -1
# It is not hard to transform it to modular version
# it runs in N * log(maximum element in array)
def sum_of_sublists(arr):
    s, mod = 1, 10**9 + 7
    for i in arr:
        cur = 1 + pow(2, i, mod)
        s = (s * cur) % mod

    return (s - 1) % mod

input()
print sum_of_sublists(list(map(int, raw_input().split())))

