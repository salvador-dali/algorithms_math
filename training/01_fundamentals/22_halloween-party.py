# https://www.hackerrank.com/challenges/halloween-party
def barSlice(n):
    d = n / 2
    if n % 2:
        return d * (d + 1)

    return d * d

for i in range(0, int(raw_input())):
    print barSlice(int(raw_input()))
