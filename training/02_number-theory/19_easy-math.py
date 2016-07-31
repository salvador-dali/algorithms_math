# https://www.hackerrank.com/challenges/easy-math
# if the number is in the form of 4...40...0 (k 4 elements and n 0)
# then it can be rewritten as 1...1 * 2^(n + 2) * 5^n (where number of 1 is k)
# you can find how many divisors of 2 and of 5 are there in the number.
# then you can use this knowledge to find the number k
# then iterate through the numbers 1, 11, 111 and find which one is divisible by remainder
def four_zero(n):
    two, five = 0, 0
    while n % 2 == 0:
        n /= 2
        two += 1

    while n % 5 == 0:
        n /= 5
        five += 1

    numOfZeros = max(two - 2, five)
    i = 1
    numOfFours = 1
    while i % n != 0:
        i = (i * 10 + 1) % n
        numOfFours += 1

    return 2 * numOfFours + numOfZeros

for i in xrange(input()):
    print four_zero(input())
