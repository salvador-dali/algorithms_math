"""
Find next and previous element in Farey sequence
here only previous one,
http://math.stackexchange.com/a/39597/50804
http://math.stackexchange.com/q/1322241/50804

here is another approach http://www.maths.ed.ac.uk/~aar/fareyproject.pdf on chapter 3
"""

def modinv(a, m):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = egcd(b % a, a)
            return g, x - (b / a) * y, y

    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def nextFarey(p, q, n):
    r = modinv(p, q)
    # d = -r % q
    # while d <= n - q:
    #     d += q
	#
    # c = (d * p + 1) / q
    #print c, '/', d

    b = r % q
    x = (n - b) / q
    b += x * q

    a = (b * p - 1) / q
    print a, '/', b





nextFarey(28, 61, 100)
# nextFarey(3, 7, 1112343)
