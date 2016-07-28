def farey(n, asc=True):
    a, b, c, d = 0, 1, 1, n
    epsilon = 0.000001

    checkPoints = ([1 / float(i) for i in xrange(1, n + 1)] + [0])[::-1]
    numsArr = [0] * n
    numsArr[0] = 1
    while c < n:
        k = int((n + b) / d)
        a, b, c, d = c, d, k * c - a, k * d - b
        num = float(a) / b
        # print num
        # print "======", num, "======"
        for i in xrange(len(checkPoints) - 1):
            if checkPoints[i] < num + epsilon < checkPoints[i + 1]:
                inclusion = 'X'
                numsArr[i] += 1
            else:
                inclusion = '.'

    #         print '[', checkPoints[i], checkPoints[i + 1], ')\t', inclusion
    #     print
    #
    # print
    # print
    s = float(sum(numsArr))
    print n, s, s / numsArr[-2], s / numsArr[-3], s / numsArr[-4], s / numsArr[-5], s / numsArr[-6], s / numsArr[-7], s / numsArr[-8], s / numsArr[-9], s / numsArr[-10], s / numsArr[-11]
    # z = [i - 1 for i in numsArr]
    # print z, sum(z)

n = 1000
for i in xrange(n, n + 10):
    farey(i)