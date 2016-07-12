from math import factorial

def binomialCoefficient(n, k):
    """
    Problem statement:
    Unordered samples without replacements
    You have n elements. In how many ways you can select k elements if the order does not matter
    http://en.wikipedia.org/wiki/Binomial_coefficient

    Example:
    You have 20 teams, in how many ways you can select 3 teams from them

    Explanation:
    We can select k permutation from n elements in N!/(N - K)! ways. Because we do not care about the order,
    then we can divide by K!
    So in the end N!/(N - K)!/K!

    :param n: total number of elements
    :param k: number of combinations we have to select. k is smaller then n.
    :return:
    """

    # first two ifs are not necessary (will work correctly even without them), but just for the sake of speed
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

    result = 1
    for i in xrange(1, k + 1):
        result = result * (n - i + 1) / i
    return result

def multinomialCoefficient(occupancy, chance=False):
    """
    Problem statement:
    We have N different balls and R bins. How many ways we can select balls in such a way
    that there will be k1 balls in a first bin, k2 in the second and so on.
    Note that k1 + ... +kR = N. The order of ball in the bin does not matter.

    Alternative explanation:
    We have R different types of objects. There is K1 objects of type 1, K2 of type 2, ... and Kr of type r
    How many permutations can we achieve

    Example:
    How many ways to select balls in such a way that there will be 5 balls in the first bin
    2 balls in the second, 0 in the third and 3 in the forth.

    You have 3 letters A, 6 letters B and 1 letter C. How many words can you create
    multinomialCoefficient([5, 2, 0, 3], True)

    Explanation:
    The balls for the first bin we can select in C(N, k1)
    for the second C(N - k1, k2), the third C(N - k1 - k2, k3) and so on. So the total number
    is the multiple of all of them.
    After writing down C(a, b), you everything will be simplified and you will end up with
    N! / (k1! * k2! * ... * kR!)

    If all the elements would be different, we would have N! permutations, but because k1 of them are the same, we
    divide this number by k1!, the same with k2, and till kR. So: N! / (k1! * k2! * ... * kR!)

    ReadMore:
    http://mathworld.wolfram.com/MultinomialCoefficient.html

    :param occupancy: array which shows how many balls are in each bin.
    :param chance: whether we calculate total number of occurrences or a probability
    :return:    integer number of possibilities, if chance is False
                float - probability that this configuration will happen if change is True
    """
    n = sum(occupancy)
    total = factorial(n) / reduce(lambda x, y: x * factorial(y), occupancy, 1.0)
    return total / len(occupancy) ** n if chance else int(total)

def unorderedSamplesWithReplacements(n, t):
    """
    Problem statement:
    Number of unordered samples with replacements
    You have unlimited number of elements of T types. How can you select N elements from them

    Examples:
    You have balls of T types. In how many ways you can select N elements

    Explanation:
    We can select elements of any type.
    For example we can select 5 elements of type1 and 2 elements of type2, 4 elements of type 3
    So we can write it in this way: 00000|00|000. Here 0 are elements and | are boundaries between types.
    Notice that for T types, we have T-1 boundaries between types. So right now we have to calculate in
    how many ways we can select N elements out of N + T - 1 (N zeros and T-1 boundaries)
    We can do this in C(N + T - 1, N)

    Alternative explanation. After presenting each combination as 0 and |. So we need to find the number
    of permutations of N zeros and T - 1 boundaries. This can be done with:
    multinomialCoefficient([N, T - 1]) which will give the same result

    :param n:   number of elements you have to select
    :param t:   number of types you have
    :return:
    """
    return binomialCoefficient(n + t - 1, n)

def successiveTrials(p, r, n):
    """
    Having a coin which has a probability of landing T p,
    what is the probability of having r T in a row in n tosses.

    good explanation: https://class.coursera.org/probability-001/lecture/292
    Let's define a success run of length.
    [11001011101111] if r = 2, the success runs are
    [-1-----1---1-1] if we see r ones, we start all over again.

    So let's define a couple of events
    S_n - at least one success of length r occurs at or before trial n
    F_n - the first success run occurs at trial n
    U_n - any success run (first or subsequent) occurs at trial n

    and probabilities s_n = P(S_n), f_n = P(F_n), u_n = P(U_n)

    Let's consider p = 0.5, r = 5, just for the sake of simplicity and later we will generalize
    Lets see that for 1-4 our probabilities f_i, u_i, s_i = 0,
    and f_5 = u_5 = s_5 = 1/2^5

    Obvious observation is that if we got a success run at or before length n, then
    it can happen if it happened on at trial 1, or trial 2 or ... trial n
    so S_n = \bigcup_{i=1}^{n}F_i or bringing it to the probability space s_n = \sum_{i=1}^{n}s_i

    Important note that if any success run occurs at trial n, then there is a FIRST success run occurring at some trial
    j at or before n (and a success run occurs at trial n). It is nice to draw the list of 0 and 1 to understand why it works.
    so u_n = \sum_{i=1}^{n-1}f_i \cdot u_{n-i} + f_n, which is a recursion which depends on the previous f_i and u_i
    we can extract f_n = u_n - \sum_{i=1}^{n-1}f_i \cdot u_{n-i}

    Right now nothing depended on the coin toss.
    u_n = p^r - \sum_{i=1}^{r-1}u_{n-i} \cdot p^i

    After generalization we get:
    s_n = \sum_{i=1}^{n}f_i\\
    f_n = u_n - \sum_{i=1}^{n-1}f_i \cdot u_{n-i} \\
    u_n = p^r - \sum_{i=1}^{r-1}u_{n-i} \cdot p^i

    :param p: probability of landing T
    :param r: number of T in the row
    :param n: the total number of the experiments
    :return: list of probabilities for every s[i] from 0 (which is not needed) to n
    """
    pr = p**r
    U = [0] * r + [pr]
    F = [0] * r + [pr]
    for k in xrange(r + 1, n + 1):
        U.append(pr - sum(U[k - i] * p**i for i in xrange(1, r)))
        F.append(U[k] - sum(F[i] * U[k - i] for i in xrange(1, k)))

    cumSum = [0]
    for i in xrange(1, n + 1):
        cumSum.append(cumSum[-1] + F[i])

    return cumSum

def ballotProblem(n, m):
    """
    You have an election and A got n votes, B got m votes. What is the probability that A leads at every steps.
    https://class.coursera.org/probability-001/lecture/205

    First of all if m \geq n the probability is equal to 0. Also if m = 0, then P = 1
    Lets see what happen at every step of the game and lets start from the very end.
    Let P_{n, m} will be the probability that A wins at every step, having n A's ballots and m B's ballots.

    Anyone can take the last ballot, so we can partition the space. Knowing that the probability of taking
    the last ballot by A is \frac{n}{n + m}, we come up with the following recursion
    P_{n, m} = \frac{n}{n + m} \cdot P_{n-1, m} + \frac{m}{n + m} \cdot P_{n, m - 1}

    So using boundary conditions it is not hard to build a couple of elements, and see that
    the solution looks like \frac{n-m}{n+m}
    Using induction one can prove that it is really the solution
    :param n:
    :param m:
    :return:
    """
    return float(n - m) / (n + m) if n > m else 0

def binomialDistribution(n, r, p):
    """
    Calculates the probability of R successes in a sequence of N independent 1|0 experiments
    where the probability of 1 is P. The probability is equal to $C_n^r \cdot p^r \cdot (1-p)^{n-r}$

    If we will check all potential outcomes they will be N zeros, N-1 zeros and 1 one, N-2 zeros and 2 ones till N ones
    we are interested about the one that has R successes, so N-R zeros and R ones, which has a probability of
    $p^r \cdot (1-p)^{n-r}$ but it can be selected in $C_n^r$ times. Hence the result.

    Mean of the distribution is n * p
    Variance is n * p * (1 - p)

    :param n:
    :param r:
    :param p:
    :return:
    """
    if r > n:
        return 0

    return binomialCoefficient(n, r) * p**r * (1 - p)**(n - r)

def poissonDistribution(a, k):
    """
    probability that a given number $k$ of events will occur in a fixed interval in time/space,
    if events are independent and appear on average $a$ times are following Poisson Distribution

    Can be found from binomial distribution if a = n * p and n goes to infinity

    Mean of the distribution is a
    Variance of the distribution is a

    The sum of two independent Poisson distributions P(a1, k), P(a2, k) is a Poisson distribution P(a1 + a2, k)
    :param a:
    :param k:
    :return:
    """
    from math_ import factorial, exp

    if a < 0 or k < 0:
        return 0

    return float(pow(a, k)) * exp(-a) / factorial(k)

def negativeBinomial(p, r, n):
    """
    Having a coin, with the probability of success P, we are throwing it till we will get R successes.
    What is the probability that we will get R-th success at the N-th toss?

    The result is $C_{n-1}^{r-1} \cdot p^r \cdot (1-p)^{n-r}$

    https://class.coursera.org/probability-001/quiz/feedback?submission_id=9406
    :param p: probability of success
    :param r: number of successes we aim for
    :param n: our last throw
    :return:
    """
    return binomialCoefficient(n - 1, r - 1) * pow(p, r) * pow(1 - p, n - r)

def couponCollector(n):
    """
    http://en.wikipedia.org/wiki/Coupon_collector%27s_problem
    You have n different items and can win each of them with equal probability. Once you won the item,
    you can still win the same item next time with the same probability.

    Expected
    :return:
    """
    from math_ import log
    return n * (log(n) + 0.577215664901532860606) + 0.5


def numberOfPermutationsStartedWithOne(numZeros, numOnes):
    """
    Having a string of zeros and ones: 00101110101110
    how many unique permutations that starts with 0 will there be

    If we fix the first 1, then we are left with `numZeros + numOnes - 1` elements.
    Out of which there are left `numOnes - 1` ones. So total number is:
    C(numZeros + numOnes - 1, numOnes - 1)
    """
    return binomialCoefficient(numZeros + numOnes - 1, numOnes - 1)

def factorial_mod(n, mod):
    if mod <= n:
        return 0

    res = 1
    for i in xrange(1, n + 1):
        res = (res * i) % mod

    return res

def binomialCoefficientModuloPrime(n, k, mod):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

    a, b, c = factorial_mod(n, mod), factorial_mod(k, mod), factorial_mod(n - k, mod)
    d = (b * c) % mod
    return a * pow(d, mod - 2, mod) % mod

