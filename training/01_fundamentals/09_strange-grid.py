# https://www.hackerrank.com/challenges/strange-grid
def strangeGrid(r, c):
    row = (r - 1) / 2
    if r % 2:
        col = (c - 1) * 2
    else:
        col = 2 * c - 1

    return row * 10 + col

print strangeGrid(*map(int, raw_input().split()))