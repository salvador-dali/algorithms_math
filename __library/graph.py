"""Things learned from various Graph courses:
- https://www.coursera.org/learn/teoriya-grafov

size of vertex cover of a graph is >= size of maximum matching
if graph has perfect matching - number of vertices is even
if graph has hamiltonian cycle and number of vertices even - it has a perfect matching
"""
import _combinatorics
from math import factorial

def num_simple_labeled_graphs(v):
    """ Number of simple labeled graphs with V nodes $2^{\frac{v(v-1)}{2}}$.
    If only with even/odd edges, divide this number by two
    """
    return pow(2, v * (v - 1) / 2)

def num_labeled_multigraphs(v, e):
    # number of labeled multigraphs with V, E is $\binom{\binom{V}{2}+E-1}{E}$
    return _combinatorics(v * (v - 1) / 2 + e - 1, e)

def num_labeled_graphs(v, e):
    # number of labeled graphs with V, E is $\binom{\binom{V}{2}}{E}$
    return _combinatorics(v * (v - 1) / 2, e)

def is_valid_degree_sequence(arr):
    """ Erdos Gallai theorem
    https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Gallai_theorem and it can be done in O(n)
    https://networkx.github.io/documentation/latest/reference/generated/networkx.algorithms.graphical.is_valid_degree_sequence_erdos_gallai.html
    """
    return False

def is_planar(f, e, v, k):
    """If a planar graph is drawn, then the number of
    Faces - Edges + Vertices = 1 + num_of_connected_components
    """
    return f - e + v == 1 + k

def num_labeled_graph(v):
    # https://en.wikipedia.org/wiki/Cayley%27s_formula
    # https://en.wikipedia.org/wiki/Pr%C3%BCfer_sequence
    return pow(v, v - 2)

def num_labeled_forests(v):
    # number of labelled rooted forests on n vertices
    return pow(v + 1, v - 1)

def num_unicycled_graphs(n):
    # \sum_{r=3}^{n}\frac{r!}{2}\cdot n^{n-r-1}\cdot C_n^r
    # https://www.coursera.org/learn/teoriya-grafov/lecture/qLGhj/formula-dlia-chisla-unitsiklichieskikh-ghrafov
    # number of graphs with one cycle (n vertices and n edges)
    return

def num_trees_with_degrees(arr):
    """ The number of labeled trees with vertices of the degree [d1, d2, ..., dn]
    https://www.coursera.org/learn/teoriya-grafov/lecture/fX8HH/dieriev-ia-s-zadannoi-posliedovatiel-nost-iu-stiepieniei
    \frac{(n-2)!}{\prod_{i=1}^{n}(d_i-1)!}

    if the vertex has degree D, it is clear that it will appear D-1 times in a pruffer code. So this
    is the multinomial coefficient

    The same formula is also the number of spanning trees in a Kn graph with degrees d1, ... dn
    """
    return

def is_eulerian(graph):
    # graph is eulerian if all the vertices are even (2n)
    pass

def is_hamiltonian(graph):
    # graph is hamiltonian if for every vertex, its degree is >= n/2,
    # where n is the number of all vertices
    pass

def num_hamilton_cycles_bipartite(n, m):
    """Number of hamiltonian cycles in bipartite graph K(n, m)
    https://www.coursera.org/learn/teoriya-grafov/lecture/ZAnxl/chislo-ghamil-tonovykh-tsiklov-v-polnom-dvudol-nom-ghrafie
    if we start from one part, we have to move in another part and alternate.
    Selecting the first vertex from one part you can do this in N times, the same is in another part
    and so on till you selected all of them (n!)^2. Now if n != m than there is no way to come back.

    If n == m, we actually calculated many cycles multiple times. How many times? For example if you
    have 1234, then you have 2341, 3412, 4123. So you have to divide by 2n
    """
    if n != m:
        return 0

    return factorial(n) ** 2 / 2 / n

