# https://www.hackerrank.com/contests/infinitum9/challenges/wet-shark-and-42
# https://www.hackerrank.com/challenges/wet-shark-and-42
# every every 42 moves a shark loses 20 power.
# so knowing it's starting power, you can get how many full 42 moves it will do.
# for the remainder of the power, it will make 2 * remainder moves
def shark42(s):
    if s == 0:
        return 0
    t = (s / 20) * 42 + (s % 20) * 2
    if s % 20 == 0:
        return t - 2
    return t

for i in xrange(input()):
    print shark42(input()) % (10**9 + 7)