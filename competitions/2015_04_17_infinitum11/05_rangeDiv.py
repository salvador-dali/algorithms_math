# https://www.hackerrank.com/contests/infinitum11/challenges/divisor-ranges
# preprocess all elements from the array to the hash where keys are numbers
# and values are the array of positions of the numbers, which are divisible by this
# number.
# to calculate the number of continuous elements which are divisible by K, C(n,m) is used
# and this number is saved in the hash
def getDivisors(n):
    # O(n^0.5)
    # get the list of divisors of a number in a sorted order
    # the main idea is to divide divisors into big and small and to remember that they come in pairs. So big = n / small
    small, large = [], []
    for i in xrange(1, int(n**0.5) + 1):
        if n % i == 0:
            small.append(i)
            if i != n / i:
                large.append(n / i)

    return small[1:] + large[::-1]

def preProcess(arr):
    from collections import defaultdict
    h = defaultdict(list)
    for i in xrange(len(arr)):
        for d in getDivisors(arr[i]):
            h[d].append(i)

    return dict(h)

def cont(arr):
    prev, num, total = arr[0], 0, 0
    for i in xrange(1, len(arr)):
        curr = arr[i]
        if curr - prev == 1:
            num += 1
        else:
            if num:
                total += (num + 1) * (num + 2) / 2
                num = 0
            else:
                total += 1
        prev = curr

    if num:
        total += (num + 1) * (num + 2) / 2
    else:
        total += 1

    return total

def answer(preArr, queries):
    h = {}
    for q in queries:
        if q not in h:
            if q == 1:
                res = (len(preArr) + 1) * (len(preArr) + 2) / 2
            else:
                res = cont(preArr[q])
            h[q] = res

        print h[q]

input()
arr = list(map(int, raw_input().split()))
q = [input() for i in xrange(input())]
preArr = preProcess(arr)
answer(preArr, q)