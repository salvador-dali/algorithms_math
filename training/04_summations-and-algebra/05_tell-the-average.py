# https://www.hackerrank.com/challenges/tell-the-average
# all the permutations will have the same sum.
def calcS(arr):
    s = 0
    for i in range(len(arr)):
        s += arr[i] * (s + 1)

    return s % 1000000007

raw_input()
print calcS(list(map(int, raw_input().split())))