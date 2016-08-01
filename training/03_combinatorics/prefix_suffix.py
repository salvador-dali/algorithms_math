from itertools import permutations

def is_prefix(arr):
    s = 0
    for i in arr:
        s += i
        if s < 0:
            return False

    return True

def is_sufix(arr):
    return is_prefix(arr[::-1])

def analyse(n):
    total = 0
    arr = [-1] * n + [1] * (2 * n)
    for i in set(i for i in permutations(arr)):
        if is_prefix(i) and is_sufix(i):
            total += 1

    return total

i = 6
# http://codeforces.com/blog/entry/12071
print i, analyse(i)
# 1 -> 1
# 2 -> 4
# 3 -> 21
# 4 -> 121



