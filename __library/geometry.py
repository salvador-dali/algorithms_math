def hyperRectangleIntersection(arr):
    """calculates the intersection of m N-dimensional rectangles. N > 1

    intersection will be an N-dimensional rectangle, where some of the lengths can be 0.
    arr = [(s1, e1), (s2, e2), ..., (sm, em)] where m is the number of rectangles
    s, e - is the N-dimensional point, which is a tuple (x1, x2, ..., xn)

    To understand the code start with the 2D arrays
    :param arr:
        [
            ((1, 2, 3), (5, 9, 7)),
            ((3, 4, 2), (7, 11, 8)),
            ((4, 6, 2), (6, 8, 9))
        ]
    :return:
    """
    s = tuple([max(i) for i in zip(*[i[0] for i in arr])])
    e = tuple([min(i) for i in zip(*[i[1] for i in arr])])

    if any([e[i] - s[i] < 0 for i in xrange(len(s))]):
        return -1
    else:
        return s, e

def distance(X, Y, p=2):
    """Calculates Minkovski distance for various p

    http://en.wikipedia.org/wiki/Minkowski_distance

    Distance has 4 rules:
    1) d(x, y) >= 0
    2) d(x, y) = 0 iff x = y
    3) d(x, y) = d(y, x)
    4) d(x, y) <= d(x, z) + d(z, y)

    the biggest one is L1 and the smallest is infinity

    :param X, Y: n-dimensional points, [1, 6, 2, 6], [3, 2, 9, 0]
    :param p: parameter from 1 to infinity. Infinity == 'inf'
    :return: positive value of a distance
    """
    if p < 1:
        raise Exception('Triangle equality does not hold')

    if p == 'inf':
        return max(abs(a - b) for a, b in zip(X, Y))

    return sum(abs(a - b)**p for a, b in zip(X, Y))**(1.0 / p)

def dotProduct(x, y):
    """ Calculates dot product (inner product, scalar product) between two vectors.

    From algebraic point of view this is $\sum x_i \cdot  y_i$ and from geometric
    $||x|| \cdot ||y|| \cdot cos(a)$, where a is angle between the vectors and ||a|| - length of the vector

    almost 2 times faster than http://stackoverflow.com/a/4094006/1090562
    :param x: list (n-dimensional vector)
    :param y: list (n-dimensional vector)
    :return: scalar
    """
    return sum(x[i] * y[i] for i in xrange(len(x)))

def normalize(v):
    """Creates a vector of the same direction, but with the length of 1

    :param v: n dimensional vector
    :return: normalized n-dimensional vector
    """
    l = dotProduct(v, v)**0.5
    if not l:
        raise Exception("0 length vector")
    return tuple([i / l for i in v])

def isOrthogonal(x, y):
    #Two vectors are orthogonal if their dot product is equal to 0
    return not dotProduct(x, y)

def projectOnVector(x, y):
    """
    project the vector x onto vector y.
    after drawing the picture, one can see that the length of projection is equal to $||x|| \cdot cos(a)$
    $cos(a) = \frac{x \cdot y}{||x|| \cdot ||y||}$, so the length = $\frac{x \cdot y}{||y||}$.

    After multiplying the length with the unit vector y (y/||y||) we taking into account
    that ||y|| * ||y|| = y \cdot y

    $proj_x y = \frac{x \cdot y}{y \cdot y} y$

    :param x: list (n-dimensional vector)
    :param y: list (n-dimensional vector)
    :return:
    """
    if not any(y) or not any(x):
        return [0] * len(y)

    a = float(dotProduct(x, y)) / dotProduct(y, y)
    return [a * i for i in y]

def projectOnBasis(v, basis):
    """
    if the basis is orthogonal then projection of $v$ onto this basis is the sum of the projections on each vector.
    E.x. $v_{i}$ is orthogonal basis, then projection: $\sum \frac{v \cdot v_{i}}{v_{i} \cdot v_{i}} v_{i}$
    :param v:       a vector which we are planning to project. (-2, 2, 2)
    :param basis:   the list of orthogonal vectors. [(1, 2, 1), (1, -1, 1)]
    :return:
    """
    from operator import add
    projection = [0] * len(v)
    for i in basis:
        projection = map(add, projection, projectOnVector(v, i))

    return projection

def orthogonalization(vectors, orthonormal=False):
    """
    for a given list of vectors, creates an orthogonal/orthonormal vectors
    Uses Gram-Schmidt orthogonalization algorithm http://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process
    http://www.cliffsnotes.com/math/algebra/linear-algebra/real-euclidean-vector-spaces/projection-onto-a-subspace
    :param vectors:     the list of vectors
    :param orthonormal: if we want orthonormal vectors
    :return: the list of orthogonal/orthonormal vectors
    """
    from operator import sub
    orthogonal = []
    for v in vectors:
        orthogonal.append(tuple(map(sub, v, projectOnBasis(v, orthogonal))))

    if orthonormal:
        return [normalize(i) for i in orthogonal]

    return orthogonal

def distanceToPlane(w, x, b):
    """
    If we have an n-dimensional hyperplane $Wx + B = 0$ and a point $X$,
    the shortest distance is $d = \frac{|w \cdot x_0+ b|}{||w||}$    http://math.stackexchange.com/q/1210545/50804
    :param w:   part of the equation Wx + B = 0
    :param x:   to point to which we find the shortest distance
    :param b:   part of the equation Wx + B = 0
    :return:
    """
    l = dotProduct(w, w)**0.5
    if not l:
        raise Exception('0-length w')

    return abs(dotProduct(w, x) + b) / l

