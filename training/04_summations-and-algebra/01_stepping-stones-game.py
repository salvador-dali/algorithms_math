# https://www.hackerrank.com/challenges/stepping-stones-game
# check potential candidates by solving the equation and taking integer value then checking
# values close to potential value and if some of them correctly works, then return it's value
def stepping(res):
    attempt = int((2 * res) ** 0.5)

    for i in [-1, 0, 1]:
        a = attempt + i
        check = a * (a + 1)/ 2
        if check == res:
            return a

    return -1

for i in xrange(input()):
    r = stepping(input())
    if r != -1:
        print 'Go On Bob ' + str(r)
    else:
        print 'Better Luck Next Time'