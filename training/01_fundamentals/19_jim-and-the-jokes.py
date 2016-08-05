# https://www.hackerrank.com/challenges/jim-and-the-jokes
def f(base, string):
    try:
        return int(str(string), int(base))
    except:
        return None

def jokes(arr):
    h = {}
    for i in xrange(len(arr)):
        value = f(arr[i][0], arr[i][1])
        if value:
            if value not in h:
                #h[value] = [(arr[i][0], arr[i][1])]
                h[value] = 1
            else:
                #h[value].append((arr[i][0], arr[i][1]))
                h[value] += 1

    s = 0
    for i in h:
        if h[i] > 1:
            s += h[i] * (h[i] - 1) / 2

    return s



print jokes([list(map(int, raw_input().split())) for i in xrange(int(raw_input()))])