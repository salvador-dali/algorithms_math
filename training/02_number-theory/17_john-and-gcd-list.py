# https://www.hackerrank.com/challenges/john-and-gcd-list
def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def convertList(arr):
    res = [arr[0]]
    for i in xrange(1, len(arr)):
        res.append( lcm(arr[i - 1], arr[i]) )
    res.append(arr[-1])

    return res

for i in xrange(int(raw_input())):
    raw_input()
    print ' '.join(map(str, convertList(list(map(int, raw_input().split())))))
