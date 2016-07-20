def findPosition(res, p):
    for i in xrange(len(res)):
        if res[i] >= p:
            return i

import sys
sys.setrecursionlimit(15000)

def different_birthdays_excluding_Feb_29(n):
    if n == 1:
        return 365.0/365.25

    return different_birthdays_excluding_Feb_29(n-1) * (365.0 - (n-1)) / 365.25

def different_birthdays_including_Feb_29(n):
    if n == 1:
        return 0.25 / 365.25

    return different_birthdays_including_Feb_29(n-1) * (365.0-(n-2)) / 365.25 + different_birthdays_excluding_Feb_29(n-1) * 0.25 / 365.25

def sol(n):
    return 1.0 - different_birthdays_excluding_Feb_29(n) - different_birthdays_including_Feb_29(n)

res = [0, 0] + [sol(i) for i in xrange(2, 366)]

for i in xrange(input()):
    print findPosition(res, input())