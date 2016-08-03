# https://www.hackerrank.com/challenges/polar-angles/
from math import sqrt, atan2, degrees
def getPolar(arr):
    polar = []
    for i in arr:
        angle, r = degrees(atan2(i[1], i[0])), sqrt(i[0]**2 + i[1]**2)
        polar.append([(angle + 360) % 360, r, i[0], i[1]])

    polar = sorted(polar, key = lambda x: (x[0], x[1]))
    return [[i[2], i[3]] for i in polar]

arr = []
for i in xrange(int(raw_input())):
    arr.append( list(map(int, raw_input().split())) )

for i in getPolar(arr):
    print str(i[0]) + ' ' + str(i[1])