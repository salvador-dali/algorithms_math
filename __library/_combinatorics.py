from math import factorial
from bisect import bisect_right, bisect_left
import _number_theory

""" Various combinatorial identities

1) C_{n}^{k} = C_{n}^{n - k}
2) C_{n}^{k} = C_{n - 1}^{k - 1} + C_{n - 1}^{k}
3) (a + b)^{n} = \sum_{i=0}^{n}C_{n}^{i}a^{i}b^{n-i}
4) \sum_{i=0}^{n}C_{n}^{i}=2^{n}  using 3) and a = b = 1
5) \sum_{i=0}^{n}  (-1)^nC_{n}^{i}=0 using 3) and a=1, b=-1
6) \sum_{n_1 + ...+n_k=n}P(n_1,...,n_2)=k^n generalization of 3) where P is multinomial coefficient
7) \sum_{i=0}^{m} C_{n+i}^{n}= C_{n+m+1}^{n + 1}
8) using 7) with n=3 you can prove that 1*2*3 + 2*3*4 + ... + m(m+1)(m+2) = m(m+1)(m+2)(m+3)(m+4)/4. and similar formulas
9) \sum_{i=0}^{m} C_{p}^{i} C_{n-p}^{m-i} = C_{n}^{m}
10) \sum_{i=0}^{m} C_{n}^{i} C_{n-i}^{n - m} =2^{m} C_{n}^{m}
11) C_{n}^{k} C_{n-k}^{m - k} = C_{m}^{k} C_{n}^{m}
12) \sum_{i=0}^{m-n} C_{p+i}^{p} C_{m-p-i}^{n-p} = C_{m+1}^{n+1}
13) using 12 and n-p=m:  \sum_{i=0}^{n} C_{m}^{i} C_{n}^{i} = C_{n + m}^{n}
14) and if n=m in 13) \sum_{i=0}^{n} (C_{n}^{i})^2 = C_{2n}^{n}
"""

"""Things to learn

# http://mathworld.wolfram.com/EulerianNumber.html
# http://informatics.mccme.ru/mod/statements/print3.php?id=4663
# https://en.wikipedia.org/wiki/P%C3%B3lya_enumeration_theorem
# https://en.wikipedia.org/wiki/Lah_number
# https://en.wikipedia.org/wiki/Bell_number
# https://en.wikipedia.org/wiki/Lobb_number
# https://en.wikipedia.org/wiki/Narayana_number
# https://en.wikipedia.org/wiki/Wedderburn%E2%80%93Etherington_number
"""

def C(k, n):
    """Number of ways to select K elements out of N. Binomial coefficient choose k out of n

    http://en.wikipedia.org/wiki/Binomial_coefficient first two ifs are not necessary (will work
    correctly even without them), but just for the sake of speed.

    N is bigger than K
    """
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

    result = 1
    for i in xrange(1, k + 1):
        result = result * (n - i + 1) / i
    return result

def catalan_list(n):
    # Calculates the first n catalan numbers using the recursive formula
    catalan_nums = [1]
    for i in xrange(n):
        catalan_nums.append(catalan_nums[-1] * 2 * (2 * i + 1) / (i + 2))

    return catalan_nums

def catalan(n):
    """Catalan number using recursive formula

    https://en.wikipedia.org/wiki/Catalan_number
    There are many problems can be counted with Catalan numbers. It is the number of ways
    - a polygon with n+2 sides can be cut into n triangles
    - to use n rectangles to tile a stair step shape (1, 2, ..., n).
    - the number of planar binary trees with n+1 leaves
    - number of permutations that avoid the pattern 123
    - number of ways to put numbers 1, 2, ... 2 * n as a table (2 x n) that columns and rows are increasing
    """
    c = 1
    for i in xrange(n):
        c = c * 2 * (2 * i + 1) / (i + 2)

    return c

def permutations_with_signature(signature):
    """
    Let's select a random permutation: 6, 2, 3, 1, 5, 4 and check when the numbers are increasing
    and when they are decreasing 6 > 2 < 3 > 1 < 5 > 4. Now we define these sequence of:
    Down, Up, Down, Up, Down as a signature of the permutation (we can use [0, 1, 0, 1, 0] for brevity).
    Surely there are other permutations of 6 that has the same signature.

    The question is how many permutations satisfy a particular signature
    Example of a use: permutations_with_signature([0, 1, 1, 1, 0, 1, 0, 1, 0, 1])

    Runs in O(n^2)

    - http://arxiv.org/pdf/math/0607763.pdf Page 10
    - http://arxiv.org/pdf/1008.1512.pdf  Page 7
    - http://oeis.org/A060351
    - http://www.emis.de/journals/INTEGERS/papers/m1/m1.pdf
    - http://www.sciencedirect.com/science/article/pii/S0012365X0000176X
    - http://www.emis.de/journals/INTEGERS/papers/m1/m1.pdf

    Partial case, where the signature is alternating: [0, 1, 0, 1, ...]
    http://www.artofproblemsolving.com/wiki/index.php/Alternating_permutation

    Taken from: https://www.hackerrank.com/contests/w18/challenges/gg
    :param signature: [0, 1, 1, 1, 0, 1, 0, 1, 0, 1]
    :return: number
    """
    res = [1]
    for i in xrange(len(signature)):
        res2 = [0] * (i + 2)
        if signature[i] == 1:
            res = res[::-1]
        for j in xrange(i + 1):
            res2[j + 1] = res2[j] + res[j]
        if signature[i] == 1:
            res = res2[::-1]
        else:
            res = res2[:]

    return sum(res)

def alternating_permutation(num):
    """
    Read about permutations_with_signature. Alternating permutation is a particular case,
    where signature alternates [0, 1, 0, 1, ...]. So:
    alternating_permutation(6) = permutations_with_signature([0, 1, 0, 1, 0])
    Off by one

    Example: alternating_permutation(40)
    Runs slower than permutations_with_signature. Can be done 2 times faster, by doing half of the
    computation

    Material:
    - https://oeis.org/A000111
    - https://en.wikipedia.org/wiki/Alternating_permutation
    - http://www.artofproblemsolving.com/wiki/index.php/Alternating_permutation
    - http://math2.uncc.edu/~hbreiter/m6105/snakes.pdf
    :param n: integer
    :return: integer
    """
    E, row = [1, 1], [1]
    for n in xrange(2, num + 1):
        row = [l + r for l, r in zip(row + [0], [0] + row)]
        E.append(sum(row[i] * E[i] * E[n - 1 - i] for i in xrange(n)) / 2)

    return E[-1]

def entringer_number(n, k):
    """
    E(n,k) are the number of permutations starting with k+1, which after initially falling,
    alternately fall then rise. http://math.stackexchange.com/a/1552862/50804

    http://oeis.org/A008281
    http://mathworld.wolfram.com/EntringerNumber.html
    http://mathworld.wolfram.com/Seidel-Entringer-ArnoldTriangle.html
    :param n: integer
    :param k: k <= n
    :return: integer
    """
    E = [[0] * (n + 1) for _ in xrange(n + 1)]
    E[0][0] = 1

    for i in xrange(1, n + 1):
        for j in xrange(1, i + 1):
            E[i][j] = E[i][j - 1] + E[i - 1][i - j]

    return E[n][k]

def number_of_tuples(n, m):
    """
    how many tuples a1, a2, ..., an are there such that
    0 < a1 < a2 < ... < an <= m

    I started to solve from the easiest case 0 < a1 < a2 < a3 < m
    Fixed a1 and calculated m * (m - 1), fixed a2 and it is (m - 1) * (m - 2)
    summed it up and it is 1/6 * (n - 2) * (n - 1) * n

    Doing the following things I found out that for n variables and number m
    the total number is

    (m - n + 1) * (m - n + 2) * ... * m / n!
    """
    total = 1
    for i in xrange(n):
        total *= m - i

    total /= factorial(n)
    return total

def subfactorial(n):
    """
    Given a set of numbers from 1 to n, find the number of permutations of this set that
    no numbers are at the correct position. Sometimes called subfactorial

    Let Ai - the permutation where the number i is correctly placed and Ai' where it is not placed
    correctly. Then we are looking for the number of permutations
    N(A1', A2', ... An'). We can calculate it using inclusion/exclusion principle.

    But this method is not the fastest one: The faster is to use a recursion:
    f(n) = (n-1) * (f(n-1) + f(n-2))

    https://en.wikipedia.org/wiki/Derangement
    http://oeis.org/A000166
    http://oeis.org/wiki/Number_of_derangements


    have to read:
    http://www.artofproblemsolving.com/wiki/index.php/Principle_of_Inclusion-Exclusion
    """
    arr = [1, 0]
    if n < 2:
        return arr[n]

    for i in xrange(2, n + 1):
        tmp = (i - 1) * (arr[0] + arr[1])
        arr[0], arr[1] = arr[1], tmp

    return tmp

def subfactorial_mod(n, mod):
    # the same as subfactorial but with modulo (any modulo >= 2)
    # f(n) = (n-1) * (f(n-1) + f(n-2))
    arr = [1, 0]
    if n < 2:
        return arr[n]

    for i in xrange(2, n + 1):
        tmp = (i - 1) * (arr[0] + arr[1]) % mod
        arr[0] = arr[1]
        arr[1] = tmp

    return tmp

def partial_dearrangement(n, k):
    """ number of the permutations of (1, ... N) so that K elements stay on the same positions.
    When K = 0 it is subfactorial https://en.wikipedia.org/wiki/Rencontres_numbers

    D(n, k) = C(n, k) * subfactorial(n - k)
    """
    return subfactorial(n - k) * C(k, n)

def stirling_second(m, n):
    """ Number of ways to put M balls into N boxes, so that every box would be non empty. M >= N

    Or N objects into K non-empty subsets. This can be solved using inclusion-exclusion.
    Let's take a look at the same problem, when the boxes are different. The number of all partitions
    is n^m if you allow empty one. Let's A_i means that the box i is empty, then by
    inclusion-exclusion principle our number
    n^m - \sum|A_i| + \sum|A_i \cap A_j| - ... + (-1)^n \sum|A_i \cap ...  \cup  A_n|

    But the first sum is (n - 1)^m*C(1, n), the second is (n - 2)^m*C(2, n) and so on. So the answer
    is \sum_{k=0}^{m}(-1)^k\cdot C_n^k(n-k)^m

    Now if the boxes are the same, than you have to divide by n!

    But in order to calculate this number you have to use another formula. Let S(m, n) is the number
    S(m, n) = m * S(m, n - 1) + S(m - 1, n - 1), which is really close to
    C(m, n) = C(m - 1, n)     + C(m - 1, n - 1)

    Boundary conditions are: S(0, 0) = 1 and S(0, i) = S(i, 0) = 0
    """
    prev_ = [0] * (n + 1)
    prev_[0] = 1

    for i in xrange(1, m + 1):
        next_ = [0] * (n + 1)
        for j in xrange(1, n + 1):
            next_[j] = j * prev_[j] + prev_[j - 1]

        prev_ = next_[::]

    return prev_[n]

def generatePascalDiagonal(n, m):
    """ generate N numbers on the M-th diagonal
    http://mathforum.org/workshops/usi/pascal/images/pascal.hex2.gif

    C(m, i + 1) = C(m, i) * (i + 1) / (i + 1 - m); where i from m to n
    TODO improve it by adding ability to calculate modulo prime
    """
    arr, m = [1], m - 1
    for i in xrange(m, n + m - 1):
        arr.append(arr[-1] * (i + 1) / (i + 1 - m))

    return arr

def C_row(n):
    """
    calculate the list of all C_n_k
    C_n_0, C_n_1, C_n_2, C_n_3 and so on
    this can be calculated, knowing that
    C_n_k = C_n_(k-1) * (n - i) / (i + 1)
    """
    arr = [1]
    for i in xrange(n):
        arr.append(arr[-1] * (n - i) / (i + 1))

    return arr

def get_shifts(arr):
    # get all cyclic shifts of a sequence
    d, res = set([]), []
    for i in xrange(1, len(arr) + 2):
        el = tuple(arr)
        res.append(el)
        if el in d:
            return res
        d.add(el)
        arr = arr[1:] + [arr[0]]

def get_cycle_length(arr):
    # get the length of the cycle of the sequence
    d = set([])
    for i in xrange(1, len(arr) + 2):
        el = tuple(arr)
        if el in d:
            return i - 1
        d.add(el)
        arr = arr[1:] + [arr[0]]

    return -1 # something wrong

def number_of_cyclic_sequences(n, r):
    """Calculate the number of Cyclic Sequences of length N over the alphabet of R symbols
    Uses the formula 2. Bruteforce without optimizations.

    https://www.coursera.org/learn/modern-combinatorics/home/week/4
    $T_r(n)$ - number of different cyclic sequences of length $n$ over the alphabet of length $r$
    number of linear sequences of length $n$ is $r^n$

    If linear sequence of length $l$ has a period $d$, than it looks $a1, a2, ..., ad$ with this block
    being replicated $l/d$ times.

    The number of linear sequences of length $n$ and period $d$ is the same with the number of sequences
    of length $d$ and period $d$. (1)

    $V(d_i)$ is a set of all linear sequences of length $n$ and period of $d_i$, then V = \bigcup V(d_i),
    And therefore the cardinality of |V| = \sum |V(d_i)| and because we know that the cardinality of
    the $V(d_i)$ is the same that the cardinality of length $d$ and period $d$ (from 1), we can write:
    $r^n= \sum |W(d_i)|$. But the number of cyclic sequences of length $n$ would be in d_i times smaller
    than the number of linear sequences of length $n$ and if |U(d_i)| is the number of cyclic sequences
    of length $n$, then $|U(d_i)| = \frac{|W(d_i)|}{d_i}$ and the equation is equal to:

    $r^n = \sum_{d_i|n}|U(d_i)| \cdot d_i$ Applying mobius inversion formula for it, you will get:
    $d \cdot |U(d)| = \sum_{d|n}\mu (d)\cdot r^{n/d}$ or |U(d)| = \frac{1}{d}\sum_{d|n}\mu (d)\cdot r^\frac{n}{d}

    But because |U(d)| is the number of cyclic sequences of length $n$, all you need to know is to calculate
    the sum of all such $n$. And the answer is:
    $\sum_{d|n} \left ( \frac{1}{d}\sum_{d'|d}\mu (d')\cdot r^\frac{d}{d'} \right )$ (2)

    :param n: length of a cyclic sequence
    :param r: cardinality of the alphabet
    :return: number of cyclic sequences of length n over the alphabet of cardinality r
    """
    total = 0
    for d in _number_theory.get_divisors(n):
        total += sum(_number_theory.mobius(d_prime) * pow(r, d/d_prime) for d_prime in _number_theory.get_divisors(d)) / d
    return total

def number_of_cyclic_sequences_prime(p, r):
    # the same as numberOfCyclicSequences, only if N is a prime number
    return (pow(r, p) - r) / p + r

def number_of_linear_sequences_with_period(p, r):
    """Number of linear sequences with period P constructed from the alphabet of R symbols
    My correct reasoning and a better explanation here http://math.stackexchange.com/q/1601822/50804
    """
    return sum(_number_theory.mobius(p/d) * pow(r, d) for d in _number_theory.get_divisors(p))

def number_of_ordered_partitions(n, numbers):
    """counts the number of ways to partition the number N into sum of natural numbers (numbers).
    Here 1 + 2 and 2 + 1 are different partitions

    Not hard to see that the number of partitions is:
    F(n; n_1, ..., n_k) = \sum_{i=1}^kF(n-n_i; n_1, ..., n_k); where F(0) = 1

    Take a look at Euler 76, 78
    """
    numbers.sort()
    results = [1] + [0] * n
    for i in xrange(1, n + 1):
        for j in numbers:
            if j > i:
                break
            results[i] += results[i - j]

    return results[-1]

def number_of_ordered_partitions_into_k(n, k):
    """Calculate the number of ways to partition N into natural numbers if you can have only
    k summations.

    Here is the idea. Write down 1 + 1 + ... + 1, where you have n ones. Now put k different |
    anywhere: 1 + 1 + 1 | 1 + 1| ,.... . You just partitioned your elements. How many ways? You have
    to select k-1 elements out of n-1.
    """
    return C(k - 1, n - 1)

def number_of_ordered_partitions_all(n):
    """counts the number of ways to partition the number N into various sum of natural numbers
    Here 1 + 2 and 2 + 1 are different partitions

    The same as number_of_ordered_partitions, where numbers are any numbers.
    Obvious from number_of_ordered_partitions_into_k
    """
    return pow(2, n - 1)

def number_of_unordered_partitions(n, numbers):
    """counts the number of ways to partition the number N into sum of natural numbers (numbers).
    Here 1 + 2 and 1 + 2 are the same partitions.

    F(n; n_1, ..., n_k) = F(n - n_1; n_1, ..., n_k) + F(n; n_2, ..., n_k)
    with the idea that the number of partitions will either have n_1 or will not have them

    This is very unoptimized solution
    """
    if n < 0:
        return 0
    if n == 0:
        return 1

    el1 = number_of_unordered_partitions(n - numbers[0], numbers[:])
    if len(numbers) > 1:
        el2 = number_of_unordered_partitions(n, numbers[1:])
    else:
        el2 = 0

    return el1 + el2

def number_of_unordered_partitions_all(n):
    """counts the number of ways to partition the number N into sum of natural numbers (numbers).
    Here 1 + 2 and 1 + 2 are the same partitions.

    The same as number_of_unordered_partitions, where numbers are any numbers
    http://en.wikipedia.org/wiki/Pentagonal_number_theorem
    check https://www.hackerrank.com/contests/projecteuler/challenges/euler078
    """
    pass

def young_diagram(arr):
    """Number of standard tableaux with this shape

    Let us have unordered partition n = \sum x_i . Because they are unordered, then let
    x_i \leq x_{i+1} (in wikipedia x_i \geq x_{i+1}). We can draw a picture:
    ...     - x1 dots
    ....    - x2 dots
    ....    - x3 dots
    .................
    .....   - xn dots

    This is called Young tablau which corresponds to the partition.


    Interesting theorem:
    number of unordered partitions N into <= K additions is equal to the number of unordered
    partitions of N + K into exactly K additions
    https://www.coursera.org/learn/modern-combinatorics/lecture/0XZ6C/5-7-tieoriemy-o-kolichiestvie-nieuporiadochiennykh-razbiienii

    http://math.mercyhurst.edu/~lwilliams/Applets/YoungDiagramCalculator.html
    https://www.coursera.org/learn/modern-combinatorics/lecture/k1TSb/5-6-diaghramma-iungha
    young([7, 5, 5, 3, 3, 1])
    """
    reverse, l, fact = arr[::-1], len(arr), factorial(sum(arr))
    for i in xrange(l):
        for j in xrange(arr[i]):
            n = arr[i] - j + l - i - bisect_right(reverse, j) - 1
            fact /= n
    return fact

def conjugate_young_diagram(arr):
    """Return a conjugate young diagram. Can be done by counting by columns instead of rows
    Can be done
    https://www.coursera.org/learn/modern-combinatorics/lecture/A3arj/5-8-dvoistviennaia-diaghramma-iungha
    """
    arr.sort()
    conjugate, i = [], 1

    while True:
        el = len(arr) - bisect_left(arr, i)
        i += 1
        if not el:
            break
        conjugate.append(el)

    return conjugate

def young_diagrams_with_columns_rows(n, m):
    """Number of young diagrams with at most N columns and M rows
    https://www.coursera.org/learn/modern-combinatorics/lecture/zUkHh/sieminar-zadacha-5-2
    Drawing the table one can see that all of the diagrams are in rectangle N*M. The diagram
    can be bound by its frontier. The frontier consists of arrows Down or Left. So C(n+m, m).

    We do not count the diagram that runs by a bound, so -1
    """
    return C(m, n + m) - 1

def row_of_pascal_triangle(n):
    # Generates n-th row of the pascal's triangle
    row = [1]
    for x in xrange(n):
        row = [l + r for l, r in zip(row + [0], [0] + row)]
    return row

def calculateBernuli(n):
    # https://github.com/bhajunsingh/programming-challanges/blob/master/hackerrank/mathematics/summing-the-k-n-series/summing-the-k-n-series-v2.py
    pass
