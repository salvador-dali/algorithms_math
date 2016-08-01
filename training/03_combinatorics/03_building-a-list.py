# https://www.hackerrank.com/challenges/building-a-list/
def f(start, arr, s):
    for i in xrange(s, len(arr)):
        print start + arr[i]
        f(start + arr[i], arr, i + 1)

for i in xrange(input()):
    input()
    s = raw_input()
    s = ''.join(sorted(s))
    f('', s, 0)
