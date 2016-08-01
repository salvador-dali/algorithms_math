from itertools import product

def analyseMatrix(M):
    for i in xrange(len(M) - 1):
        for j in xrange(len(M[0]) - 1):
            if M[i][j] == M[i + 1][j] or M[i][j] == M[i][j + 1]:
                return False

    i = len(M) - 1
    for j in xrange(len(M[0]) - 1):
        if M[i][j] == M[i][j + 1]:
            return False

    j = len(M[0]) - 1
    for i in xrange(len(M) - 1):
        if M[i][j] == M[i + 1][j]:
            return False
    return True

def bruteforce(n, m, k):
    s = set([])
    for arr in product(range(k), repeat=n * m):
        M = [arr[i*m: i*m+m] for i in xrange(n)]
        if analyseMatrix(M):
            s.add(arr)


    return len(s)






