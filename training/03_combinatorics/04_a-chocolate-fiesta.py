# https://www.hackerrank.com/challenges/a-chocolate-fiesta
# it is clear that we do not care what numbers are there. Only number of odd and even numbers
# the first used fact is that the set of n elements have 2^n subsets (one of them is empty).
# if we have only even numbers we can select any of them. So 2^n - 1
#
# if we have some odd elements, let's fix last of them. Select all possible subsets from these
# 2^(n-1) elements. Now if the sum of the subset is even we have to add the last even value, if it
# is odd, we do not have to add it. In any way we can select it in 2^(n-1) way. This include empty
# subset.
input()
odd, even, mod = 0, 0, 10**9 + 7
for i in map(int, raw_input().split()):
    if i % 2:
        odd += 1
    else:
        even += 1

if odd == 0:
    print (pow(2, even, mod) - 1) % mod
else:
    res = pow(2, odd + even - 1, mod) - 1
    print res % mod
