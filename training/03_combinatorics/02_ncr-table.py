# https://www.hackerrank.com/challenges/ncr-table
# calculate the list of all C_n_k
# C_n_0, C_n_1, C_n_2, C_n_3 and so on
#
# this can be calculated, knowing that
# C_n_k = C_n_(k-1) * (n - i) / (i + 1)
def C_row(n):
    arr = [1]
    for i in xrange(n):
        arr.append(arr[-1] * (n - i) / (i + 1))

    return arr

for i in xrange(int(raw_input())):
    arr = C_row(int(raw_input()))

    arr2 = [i % 10**9 for i in arr]
    print ' '.join(map(str, arr2))