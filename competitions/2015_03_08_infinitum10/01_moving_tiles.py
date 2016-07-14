# https://www.hackerrank.com/contests/infinitum10/challenges/sherlock-and-moving-tiles

# let's fix the first tile and move only the second with the speed v = |s1 - s2|
# then the equation, which describes the motion, can be written as
# t = 2^(1/2) * (l - q^(1/2)) / v
def move(l, s1, s2, q):
    return 2**0.5 * (l - q**0.5) / float(abs(s1 - s2))

l, s1, s2 = map(int, raw_input().split())
for i in xrange(input()):
    print move(l, s1, s2, input())


# for some reason python did not gave me a correct precision, so I was forced to use Ruby
# def move(l, s1, s2, q)
#     v = (s1 - s2).abs
#     return Math.sqrt(2) * (l - Math.sqrt(q)) / v
# end
#
# ar = gets.chomp.split " "
# array = ar.map{ |a| a.to_i }
# $i = 0
# number = gets.to_i
# begin
#     q = gets.to_i
#     puts move(array[0], array[1], array[2], q)
#     $i +=1;
# end until $i > $num