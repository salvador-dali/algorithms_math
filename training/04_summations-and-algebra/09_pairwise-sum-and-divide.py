# https://www.hackerrank.com/challenges/pairwise-sum-and-divide
def fun(A):
    l, total = len(A), 0
    count1 = A.count(1)
    count2 = A.count(2)

    total += count1 * (count1 - 1)      # sum of all floor which is from 1 and 1
    total += count1 * (l - count1)      # sum of all floor which is from 1 and any other numbers
    total += count2 * (count2 - 1) / 2  # sum of all floor which is from 2 and 2

    return total

for i in xrange(int(raw_input())):
    raw_input()
    print fun(list(map(int, raw_input().split())))