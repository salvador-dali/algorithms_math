# https://www.hackerrank.com/challenges/circle-city
# basically checks the number of points on the circle with an integer coordinates.
# instead of checking the whole circle it is suffice to check just one quarter
for pp in xrange(input()):
    r, k = map(int, raw_input().split())
    r_root, cnt = r**0.5, 0
    if r_root == int(r_root):
        fl, r_root = True, int(r_root)
    else:
        fl, r_root = False, int(r_root) + 1

    for y in xrange(1, r_root):
        t = (r - y**2)**0.5
        if t == int(t):
            cnt += 1

    cnt *= 4
    if fl:
        cnt += 4

    print "possible" if cnt <= k else "impossible"