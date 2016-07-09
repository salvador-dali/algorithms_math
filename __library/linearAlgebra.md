##Some things from linear algebra##

**linear combination** of vectors ${V_{i}$ is any vector $v = \sum{a_{i} \cdot v_{i}}$ where $a_{i}$ is a scalar.
linear combination is **non trivial** if $\exists a_i\neq 0$

**span** is the set of all linear combinations

vectors $v_{i}$ are **linear independent** if none of them is a linear combination of others. In other word if 
$\sum{a_{i}v_{i}} = 0$ only if all $a_{i}=0$

**row rank** is the maximum number of linear independent rows of a matrix, the same for **column rank**

**rank** or **image** of the matrix is always equal to row rank and to column rank (in every matrix they are equal)

**basis** of $R^{n}$ is a collection of linear independent vectors that spans in $R^{n}$, any vector in $R^{n}$ can be 
written uniquely in basis.

**basis of a linear space** if we have $Ax=0$ and need to find a basis, we need to transform $A_{m \times n}$ to 
echelon form (I D), where $I_{m \times m} and D is some matrix (D_{m \times n - m}). Then the column of the matrix 
created from (-D; I) where we take only part of the I with the size $m-n$ is the basis. Check that we have ; there.

we say that set of vectors $e_1, e_2, ... e_n$ **generates a linear space** if any vector from that liner space can be
presented as a linear combination of the vectors.

**orthogonal vectors** are the vectors $v_{i}$ such that for any vectors $i \neq j$ their dot product equal to 0

**orthonormal vectors** are orthonormal and each of their length is equal to 1

if the **basis is orthogonal** then projection of $v$ onto this basis is the sum of the projections on each vector.
E.x. $v_{i}$ is orthonormal basis, then projection: $\sum \frac{v \cdot v_{i}}{v_{i} \cdot v_{i}} v_{i}$.
If we have an orthogonal basis, then every vector can be easily divided into components, is just a dot product between
a vector and each vector in the basis.

Every basis can be transformed to a orthogonal basis using **Gram-Schmidt orthogonalization algorithm**.
The algorithm works in the following way. It starts with an empty set of orthogonal vectors and on each iteration
(the number of iterations is equal to the number of vectors) it adds a new vector with is orthogonal to the previous.
These [links](http://www.cliffsnotes.com/math/algebra/linear-algebra/real-euclidean-vector-spaces/projection-onto-a-subspace)
were [helpful for me](http://math.stackexchange.com/q/1208551/50804).
So if we have vectors ${v_1, v_2, ..., v_n}$, then in the beginning the orthogonal set is empty, then we add $v_1$ there as $w_1$,
then on the second iteration we project $v_2$ onto the subspace of ${v_1}$ (let this projection be $v_2'$ and we know 
how to find it from the previous paragraph) and then find the difference $v_2 - v_2'$ (mark it as $w_2). 
Add this to the orthogonal bases. On the third iteration project $v_3$ on the subspace ${w_1, w_2}$. Continue this till
the last element. If we want, we can normalize the vectors in the end.

Grand-Schmidt orthogonalization is important not only because it creates the orthogonal basis, but also because if 
our starting vectors are ${v_1,v_2,...v_n}$ and the algorithm produced ${w_1,w_2,...w_n}$, then
$$span({v_1}) = span({w_1})$$
$$span({v_1, v_2}) = span({w_1, w_2})$$
$$...$$
$$span({v_1, v_2, ..., v_n}) = span({w_1, w_2, ..., w_n})$$

**null space** or **kernel** of the matrix is a set of vectors $v$ such that $A \cdot v = 0$. 0-vector is always in null space

**rank nullity theorem** states that for any matrix A (m x n) $rank(A) + nullity(A) = n$, you can write the same with 
$im(A) + kernel(A) = n$

$rank(AB) \leq min(rank(A), rank(B))$

elementary operations for a matrix:

 - multiplication with a non-zero number
 - addition of one row to another
 - interchange two rows

if a matrix B is created from A with one elementary operation, then there exist $S \cdot A = B$.


**Multiplication of a permutations:**
Havin g two permutation $\sigma$ and $\tau$, their product is a permutation $\rho = \sigma\circ \tau$ and calculated as 
$\rho(x) = \sigma(\tau(x))$. For example: \begin{pmatrix}1 & 2 & 3 & 4\\4 & 3 & 1 & 2\end{pmatrix}\circ \begin{pmatrix}1 & 2 & 3 & 4\\3 & 1 & 4 & 2\end{pmatrix}=\begin{pmatrix}1 & 2 & 3 & 4\\1 & 4 & 2 & 3\end{pmatrix}
 
As you see you take 1 -> 3 -> 1, 2 -> 1 -> 4 and so on. Do not forget that you start with the second one.

**The sign of a permutation**
for a permutation check all $i < j$ and count all of them that produce f(i) > f(j). Let it be x
sign = (-1)^x. If x = -1, permutation is odd, otherwise evens.

sign(a \circ b) = sign(a) \cdot sign(b)
another way to find the sign of a transposition is to find how many transpositions should return it to original (1,...,n)

Permutation is a cyclic permutation if a_1 -> a_i -> a_j -> ... -> a_k -> a_1
 
 
 
https://stepic.org/lesson/Determinants-7608/step/16?path=undefined
Solved by using this one, http://www.mathopenref.com/coordtrianglearea.html

https://stepic.org/lesson/Change-of-basis-11184/step/5?course=Linear-Algebra-Problems-and-Methods&unit=2404
https://stepic.org/lesson/Change-of-basis-11184/step/14?path=undefined
https://stepic.org/lesson/Invariant-subspaces-11197/step/2?path=undefined