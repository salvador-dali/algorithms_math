# https://www.hackerrank.com/challenges/palindromes
def perm(s):
    all_list, n = [], len(s) * (len(s) - 1) / 2
    for i in xrange(len(s)):
        for j in xrange(i + 1, len(s)):
            arr = list(s)
            arr[i], arr[j] = s[j], s[i]
            all_list.append(''.join(arr))
    print n, '*', s, '=', all_list

perm("abbcc")

