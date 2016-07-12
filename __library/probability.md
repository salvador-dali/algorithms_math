##some things from probability##

**events are independent** if $P(A\cup B) = P(A) \cdot P(B)$

**total probability** if we can partition a space in $A_i$ non intersected events, then $P(H) = \sum P(H | A_i) \cdot P(A_i)$

**posterior probability** from the total probability, one can see that $P(A_k|H) = \frac{P(H|A_k) \cdot P(A_k)}{\sum P(H | A_i) \cdot P(A_i)}$

**law of succession** we have a binary event (T, F) . If we observed that the last $r$ times occurred T, what is the 
probability that the next event will be T. Let $H_r$ means that T appeared $r$ times in the row. So we need to find
$P(H_{r+1} | H_r)$. You can read more [here](https://class.coursera.org/probability-001/lecture/213)

We can convert this problem to balls and urns problem. Let's have $N + 1$ urns and each urn has N balls out of each $i$
balls are red and then $N - i$ are black. Each urn is equally likely, so $P(A_i) = \frac{1}{N+1}$. If we selected an urn
$i$, the probability of selecting red ball is $\frac{i}{N}$. This mean that to select N balls with replacements from i-th
urn $P(H_r | A_i) = \frac{i^r}{N_r}$. By the total probability law:
$P(H) = \sum_{i=1}^{N} P(H | A_i) \cdot P(A_i) = \frac{1}{N+1} \sum_{i=1}^{N}\frac{i^r}{N_r} \approx  \int_{0}^{1}x^rdx=\frac{1}{r+1}$
check [my question](http://math.stackexchange.com/q/1213708/50804) if it is not understandable. So now 
$P(H_{r+1} | H_r) = \frac {P(H_{r+1} \cup H_r)}{P(H_r)}= \frac {P(H_{r+1})}{P(H_r)} = \frac{r+1}{r+2}$

So we see that $P(H_{r+1} | H_r) = \frac{r+1}{r+2}$ and $P(H_{r+s} | H_r) = \frac{r+1}{r+s+1}$

**conditional independence** $P(A \cup B | C) = P(A|C) \cdot P(B|C)$ or for many element $P(\bigcap_{i=1}^{n}A_i) = \prod_{i=1}^{n}P(A_i)$
Also events determined by disjoint subsets of independent events are also independent