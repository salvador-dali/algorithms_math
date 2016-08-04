# https://www.hackerrank.com/challenges/bday-gift
# it is easy to see that this is expected value, where the probability is equal to 1/2
# so sum everything and divide by 2
s = 0
for i in xrange(input()):
    s += input()

print "%.1f" % (s / 2.0)