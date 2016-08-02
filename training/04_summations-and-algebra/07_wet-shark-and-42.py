# https://www.hackerrank.com/challenges/wet-shark-and-42
# check /challenges/infinum_9/01_wet_shark.py
def shark42(s):
    if s == 0:
        return 0
    t = (s / 20) * 42 + (s % 20) * 2
    if s % 20 == 0:
        return t - 2
    return t

for i in xrange(input()):
    print shark42(input()) % (10**9 + 7)