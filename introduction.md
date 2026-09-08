# Erdős Problem 142

## 1. Introduction

[Erdős Problem 142](https://www.erdosproblems.com/forum/thread/142), taken from the Erdős Problem database [[1]](#References) states that:
> Let $r_k(N)$ be the largest possible size of a subset $\{1\dots N\}$ that does not contain
> any non-trivial $k$-term arithmetic progression.  Prove an asymptotic formula for $r_k(N)$.

$$
r_k(N) = \max\left\{|A| : A\subseteq\{1,\ldots,N\}, \; A\text{ contains no non-trivial }k\text{-term arithmetic progression}\right\},\; k, N \in \mathbb{N}$$

This is a combinatorial problem concerning subsets of integers and arithmetic progressions.  The goals of this paper are threefold:
1. Provide clarity, in lay terms, to what the problem means.
1. Investigate $r_k(N)$ for small values of $k$ and $N$.
1. Examine how $r_k(N)$ grows as $N$ becomes large and why an asymptotic formula may exist.

A proof of an asymptotic formula for $r_k(N)$ is beyond scope of this paper at this time.

## 2. Meaning of the Problem

Mathematical problem statements and solutions have a tendency to converge toward the simple, concise, and elegant, often at the expense of accessibility to readers unfamiliar with the underlying concepts. This section provides a journey toward understanding Erdős Problem 142 and its origins by breaking the problem into its elementary components so that readers with a modest mathematical background can understand precisely what is being asked.

### 2.1 What is an Erdős Problem?

Before discussing the problems, it is helpful to understand the person who created them. Paul Erdős (1913–1996) was a Hungarian mathematician whose work focused heavily on discrete mathematics, number theory, combinatorics, and graph theory. He taught and collaborated at universities throughout the United States and Israel and published roughly 1,500 mathematical papers during his lifetime [[2]](#references).

Erdős was particularly well known for posing mathematical problems that were simple to state but often extremely difficult to solve. He was interested in problems that appeared to lie just beyond the reach of existing mathematical techniques, believing that their solutions might require new ideas and, in turn, lead to additional mathematical questions. Erdős frequently offered monetary prizes for solutions to problems he considered especially interesting or difficult. In general, larger prizes indicated that he believed a problem would be particularly difficult to resolve.

Problem 142 is one such problem. It appears in Erdős's published problem lists beginning in 1980, and a 1981 source records a prize of $10,000 for its solution. The problem remains open today [[1]](#references).

### 2.2 What is Problem 142 asking?

#### 2.2.1 What is a set?

The first part of the problem states that $r_k(N)$ *is the largest possible size of a subset of $\{1,\dots,N\}$*. Thus, $r_k(N)$ is an integer representing the number of elements in a particular set. The conditions that this set must satisfy will be discussed shortly. First, it is important to understand what is meant by a *set* and a *subset*.

> A set is an unordered collection of distinct objects, called *elements* or *members* of the set. A set is said to *contain* its elements. The notation $a\in A$ means that $a$ is an element of the set $A$, while $a\notin A$ means that $a$ is not an element of $A$. [[3, Ch. 2, p. 122]](#references)

Based on this definition, $\{1,\dots,N\}$ is a finite set containing the consecutive integers beginning with 1 and ending with $N$. It contains exactly $N$ elements. The problem asks for the maximum possible size of a particular *subset* of this set.

> The set $B$ is a *subset* of $A$ if and only if every element of $B$ is also an element of $A$. [[3, Ch. 2, p. 125]](#references)

For example, let

$$
A=\{1,\dots,N\}
$$

and let

$$
B=\{2,3,4\}.
$$

Provided that $N\ge4$, every element of $B$ is also an element of $A$. Therefore,

$$
B\subseteq A.
$$

#### 2.2.2 Characteristics of the target subset

The problem asks for the size of the largest subset of $\{1...N\}$ that does not contain a non-trivial $k$-term arithmetic progression.  Before addressing what *non-trivial* means it is helpful to first examine arithmetic progressions themselves.

> An *arithmetic progression* is a sequence of the form
>$$
>a, a + d, a + 2d,...a + nd, ...
>$$
> where the initial term $a$ and the common difference $d$ are real numbers. [[3, Ch. 2, p. 166]](#references)

Note that although an arithmetic progression may generally consist of real numbers, the arithmetic progressions considered in Erdős Problem 142 consist only of integers because they are drawn from $\{1,\ldots,N\}$.

A $k$-term arithmetic progression is an arithmetic progression containing exactly $k$ terms.  If $k=3$, then the arithmetic progression must contain 3 numbers that have a common difference.

Example 1:
Let 
$$
k = 3,\; C=\{2,3,4\}.
$$

This set contains a subset with a 3-term arithmetic progression since {2,3,4} all have a common difference of 1.

Example 2:
Let 
$$
k = 6,\; C=\{2,4,6,8,10,12,14,16,18,20\}.
$$

This set contains a subset with a 6-term arithmetic progression since $\{2,4,6,8,10,12\}$ all have a common difference of 2. Other 6-term arithmetic progressions exist here as well, such as $\{10,12,14,16,18,20\}$, and $\{6,8,10,12,14,16\}$.

Example 3:
Let 
$$
k = 4,\; C=\{1,2,3,5,7,9,10,11,13,15,16\}.
$$

This set also contains subsets of 4-term arithmetic progressions since $\{1,3,5,7\}$, $\{1,5,9,13\}$, $\{3,5,7,9\}$, $\{5,7,9,11\}$, and $\{7,9,11,13\}$ contain common differences of 2, 4, 2, 2, and 2, respectively.

Example 4:
Let 
$$
k = 4,\; C=\{1,2,7,9,11,15\}.
$$

This set contains no subsets with a 4-term arithmetic progression. 

With the meaning of an arithmetic progression established, the term *non-trivial* can now be examined.  

>A non-trivial arithmetic progression is one in which the common difference $d$ is nonzero. Thus, an arithmetic progression is non-trivial when $d\neq0$ and trivial when $d=0$. [4, p. 5265](#references)

When the terms are written in increasing order, as they may be in Erdős Problem 142, a non-trivial progression has $d>0$.

An example of a trivial 5-term arithmetic progression is

$$ 8,8,8,8,8. $$

Every term differs from the preceding term by zero, making the progression trivial.

It is important to note that $8,8,8,8,8$ cannot itself be a subset of $\{1,\ldots,N\}$. By definition, a set contains *distinct* elements, so repeated occurrences of $8$ collapse to the single-element set $\{8\}$. Consequently, a trivial arithmetic progression cannot occur within one of the subsets considered in Erdős Problem 142.

The qualifier *non-trivial* is therefore effectively redundant in this particular setting, but it makes explicit the standard convention that arithmetic progressions with common difference zero are excluded.

#### 2.2.3 Asymptotic formula for $r_k(N)$

Asymptotic analysis is a branch of analysis concerned with developing techniques for describing the approximate behavior of functions or solutions when variables become very large, very small, or approach points at which ordinary analytical methods may be difficult to apply [[5, p. 1]](#references). In the context of Erdős Problem 142, the primary interest is in the behavior of $r_k(N)$ as $N$ becomes arbitrarily large. The function $r_k(N)$ contains two parameters, $k$ and $N$. The problem asks how $r_k(N)$ behaves as $N\to\infty$.  This paper will fix $k$ to isolate the behavior of $r_k(N)$ as $N\to\infty$. Small values of $k$ and $N$ will first be examined to develop intuition before considering the large $N$ behavior relevant to an asymptotic formula. 

If there exists an asymptotic formula $A_k(N)$ that approximates $r_k(N)$, then the approximation becomes increasingly accurate relative to $r_k(N)$ as $N\to\infty$. Formally,

$$
\lim_{N\to\infty}\frac{r_k(N)}{A_k(N)}=1.
$$

This does not mean that $A_k(N)$ must equal $r_k(N)$ for every finite value of $N$; rather, the ratio between them approaches 1 as $N$ becomes arbitrarily large.

#### 2.2.4 Summary

In summary, there is a finite set, $S$, of positive integers represented by

$$
S=\{1,2,3,\dots,N\}.
$$

For given values of $k$ and $N$, the quantity $r_k(N)$ represents the largest number of elements that can be included in a subset of $S$ without that subset containing a non-trivial $k$-term arithmetic progression.

Erdős Problem 142 asks for an asymptotic formula for $r_k(N)$. In other words, the problem asks for a formula that describes the long-term behavior of $r_k(N)$ as the relevant variable or variables become arbitrarily large.

## 3. Experimental Investigation of $r_k(N)$ for Small Values of $k$ and $N$

For the purposes of this paper, $k$ will remain fixed at $3$ so that the behavior of $r_k(N)$ can be examined as $N$ increases. Choosing $k=3$ also makes it practical to examine the relevant subsets directly without excessive computational or cognitive complexity.

Furthermore, $k=3$ is the smallest value of $k\geq2$ for which a $k$-element subset may fail to be an arithmetic progression. When $k=2$, any two distinct integers necessarily form a two-term arithmetic progression.

For example, consider $N=4$:

$$
S_4=\{1,2,3,4\}.
$$

The $\binom{N}{k}=\binom{4}{2}=\frac{N!}{k!(N-k)!} = \frac{4!}{2!2!} = 6$ two-element subsets of $S_4$ are

$$
\{1,2\},\;
\{1,3\},\;
\{1,4\},\;
\{2,3\},\;
\{2,4\},\;
\{3,4\}.
$$

Each pair can be written in the form

$$
a,\;a+d,
$$

where $d>0$. The common differences of the subsets above are, respectively,

$$
1,\;2,\;3,\;1,\;2,\;1.
$$

Therefore, every two-element subset of $S_4$ is a non-trivial two-term arithmetic progression. More generally, any two-element subset $\{a,b\}$ with $a<b$ forms a two-term arithmetic progression with common difference

$$
d=b-a.
$$

The case $k=3$ is therefore the first case in which some $k$-element subsets can be arithmetic progressions while others are not.


With $k$ selected, the next consideration is the value of $N$.  For a manual evaluation, $N=5$ allows for a representative examination of the concepts involved in calculating $r_k(N)$ without requiring heavy computation or the evaluation of an excessive number of subsets.

### 3.1 Method for Determining $r_k(N)$ for Small $N$

For small values of $N$, $r_k(N)$ can be determined by exhaustively examining subsets of

$$
S_N=\{1,2,\ldots,N\}.
$$

For convenience, any subset of $S_N$ being considered as a possible progression-free subset will be referred to throughout this paper as a **candidate subset**. A $k$-element subset of $S_N$ whose elements form a non-trivial $k$-term arithmetic progression will be referred to as a **forbidden subset**. A candidate subset is **progression-free** if it contains no forbidden subset.

The following procedure will be used throughout the experimental investigation:

1. **Identify the forbidden subsets.**

   A $k$-term arithmetic progression has the form

   $$
   a,\;a+d,\;a+2d,\;\ldots,\;a+(k-1)d,
   $$

   where $a$ is the initial term and $d>0$ is the common difference.

   Because every term must belong to $S_N$, only values of $a$ and $d$ satisfying

   $$
   a+(k-1)d\leq N
   $$

   need to be considered.

   For example, when $N=5$, $k=3$, $a=1$, and $d=2$,

   $$
   1+(3-1)(2)=5\leq5.
   $$

   Therefore, a three-term arithmetic progression having common difference
   $d=2$ can occur within $S_5$. In contrast, if $d=3$,

   $$
   1+(3-1)(3)=7>5.
   $$

   Since $a=1$ is already the smallest possible initial term, no
   three-term arithmetic progression having common difference $d=3$
   can occur within $S_5$.

   The inequality above provides an algorithmic method for determining
   the possible values of $d$ and $a$. Solving first for $d$ gives

   $$
   a+(k-1)d\leq N
   $$

   $$
   (k-1)d\leq N-a
   $$

   $$
   d\leq\frac{N-a}{k-1}.
   $$

   To allow $d$ to be as large as possible, choose the smallest possible initial term, $a=1$. Since $d$ must be an integer, the floor can be taken, yielding:

   $$
   d_{\max} = \left\lfloor\frac{N-1}{k-1}\right\rfloor.
   $$

   Once the possible values of $d$ are known, the maximum initial term
   can be determined separately for each $d$. Solving the original
   inequality for $a$ gives

   $$
   a\leq N-(k-1)d.
   $$

   Therefore,

   $$
   a_{\max}(d)=N-(k-1)d.
   $$

   Thus the forbidden subsets can be generated systematically by taking

   $$
   d=1,2,\ldots,d_{\max}
   $$

   and, for each $d$, taking

   $$
   a=1,2,\ldots,a_{\max}(d).
   $$

   Each pair $(a,d)$ generates the forbidden subset

   $$
   \{a,\;a+d,\;a+2d,\;\ldots,\;a+(k-1)d\}.
   $$


2. **Begin with the largest possible candidate subset.**

   The first candidate is $S_N$ itself, which has cardinality $|S_N|=N$.  Cardinality is the number of elements in a set. If $S_N$ contains any forbidden subset, then it cannot be progression-free.  The cardinality of the set being examined will be known as $m$.


3. **Reduce the candidate size if necessary.**

   If no valid candidate of size $m$ exists, examine subsets of $S_N$ having cardinality $m-1$.

   The number of such candidate subsets is

   $$
   \binom{N}{m-1} = \frac{N!}{(m-1)!(N-m+1)!}.
   $$

4. **Compare each candidate against the forbidden-subset list.**

   For each candidate subset $C$, determine whether there exists a forbidden subset $F$ (identified in Step 1) such that

   $$
   F\subseteq C.
   $$

   If such a subset exists, then $C$ is rejected because it contains a non-trivial $k$-term arithmetic progression.  If no forbidden subset is contained in $C$, then $C$ is progression-free.

5. **Stop when the first valid candidate size is found.**

   Candidate sizes are examined from largest to smallest. Therefore, once at least one progression-free subset of size $m$ is found,

   $$
   r_k(N)=m.
   $$

   No subsets of smaller cardinality need to be examined. Removing elements from a progression-free subset cannot create a new arithmetic progression.


### 3.2 A Manual Example $k=3,\;N=5$

This section will apply the method described in section 3.1 for determining $r_k(N)$ for small $N$.  Let $k$ = 3 and $S_5 = \{1,2,3,4,5\}$.  

#### 3.2.1 Identify the forbidden subsets

$$
d_{\max} = \left\lfloor\frac{N-1}{k-1}\right\rfloor
=\left\lfloor\frac{5-1}{3-1}\right\rfloor
= \left\lfloor\frac{4}{2}\right\rfloor = 2 \;\therefore\; d \in \{1,2\},\;d_1 = 1, d_2 = 2
$$ 

For each allowable value of $d$:
$$
a_{\max}(d_1)=N-(k-1)d_1 = 5-(3-1)(1) = 5-2 = 3 \;\therefore\; a(1) \in \{1,2,3\}
$$

$$
a_{\max}(d_2)=N-(k-1)d_2 = 5-(3-1)(2) = 5-4 = 1;\therefore\; a(2) \in \{1\}
$$

Recalling the $k$-term arithmetic progression form:

   $$
   a,\;a+d,\;a+2d,\;\ldots,\;a+(k-1)d,
   $$

and using $d_{max}$ and $a_{max}(d)$ yields the forbidden subsets:

| $d$ | Allowable $a$ | Arithmetic progression | Forbidden subset |
|---:|:---:|:---|:---|
| $1$ | $1$ | $1,\;1+1,\;1+2(1)$ | $\{1,2,3\}$ |
| $1$ | $2$ | $2,\;2+1,\;2+2(1)$ | $\{2,3,4\}$ |
| $1$ | $3$ | $3,\;3+1,\;3+2(1)$ | $\{3,4,5\}$ |
| $2$ | $1$ | $1,\;1+2,\;1+2(2)$ | $\{1,3,5\}$ |


#### 3.2.2 Begin with the largest possible candidate subset

The first candidate is $S_N$, or $S_5$, which has cardinality 5. If $S_5$ contains even one forbidden subset, then it is not progression-free and must be rejected as a candidate.

The number of possible 3-element subsets of $S_N$ is $\binom{5}{3} = \frac{5!}{3!2!} = 10$.  They are:

$$
\{1, 2, 3\},\; \{1, 2, 4\},\; \{1, 2, 5\},\; \{1, 3, 4\},\; \{1, 3, 5\},\; \{1, 4, 5\},\; \{2, 3, 4\},\; \{2, 3, 5\},\; \{2, 4, 5\},\; \{3, 4, 5\}
$$


From Section 3.2.1, the forbidden subsets are:
$$
\{1, 2, 3\}, \{2, 3, 4\}, \{3, 4, 5\}, \{1, 3, 5\}
$$

Since, for example: $\{1, 2, 3\} \subseteq S_5$, $S_5$ contains a forbidden subset and therefore is not progression-free.  Thus, the candidate of cardinality $5$ fails, and subsets of cardinality $m - 1=5-1= 4$ must next be examined.

Optimization:

In this example, testing $S_5$ directly also reveals a broader fact: For any $N\geq k\geq2$, the full set $S_N$ necessarily contains the $k$-term arithmetic progression

$$
\{1,2,\ldots,k\}.
$$

Therefore, $S_N$ can never itself be progression-free when $N\geq k$, and future searches may begin with candidate subsets of cardinality $N-1$.

#### 3.2.3  Reduce the candidate size

Since the single candidate of cardinality $5$ is not progression-free, the next step is to examine candidate subsets $C$ of cardinality 4, or $|C|=4$. $m$ is now $4$.

The number of possible $4$-element candidate subsets of $S_5$ is

$$
\binom{5}{4} = \frac{5!}{4!1!} = 5.  
$$

They are:
$$
\;\{1, 2, 3, 4\}, \;\{1, 2, 3, 5\}, \;\{1, 2, 4, 5\}, \;\{1, 3, 4, 5\}, \;\{2, 3, 4, 5\}
$$

The number of possible $3$-element subsets of each candidate $C$ is

$$
\binom{4}{3} = \frac{4!}{3!1!} = 4.
$$
These will be reviewed in the next section.

#### 3.2.4 Compare each candidate against the forbidden-subset list

The forbidden subsets from section 3.2.1 are reproduced here for convenience:
$$
\;\{1, 2, 3\}, \;\{2, 3, 4\}, \;\{3, 4, 5\}, \;\{1, 3, 5\}
$$

The $4$-element subsets of $S_5$, combined with the forbidden subsets, allow for the evaluation of each candidate C from section 3.2.3 to determine if it contains any forbidden subset $F$.  The results are in the table below:

| Candidate subset $C$ | 3-element subsets of $C$ | Forbidden subsets $F\subseteq C$ |
|:---|:---|:---|
| $\{1,2,3,4\}$ | $\{1,2,3\},\;\{1,2,4\},\;\{1,3,4\},\;\{2,3,4\}$ | $\{1,2,3\},\;\{2,3,4\}$ |
| $\{1,2,3,5\}$ | $\{1,2,3\},\;\{1,2,5\},\;\{1,3,5\},\;\{2,3,5\}$ | $\{1,2,3\},\;\{1,3,5\}$ |
| $\{1,2,4,5\}$ | $\{1,2,4\},\;\{1,2,5\},\;\{1,4,5\},\;\{2,4,5\}$ | None |
| $\{1,3,4,5\}$ | $\{1,3,4\},\;\{1,3,5\},\;\{1,4,5\},\;\{3,4,5\}$ | $\{1,3,5\},\;\{3,4,5\}$ |
| $\{2,3,4,5\}$ | $\{2,3,4\},\;\{2,3,5\},\;\{2,4,5\},\;\{3,4,5\}$ | $\{2,3,4\},\;\{3,4,5\}$ |

Of the five candidates, only

$$
C=\{1,2,4,5\}
$$
contains no forbidden subset $F$. Therefore $C$ is progression-free.  

#### 3.2.5 Stop when the first valid candidate size is found

As a reminder, candidate sizes are examined from largest to smallest. Therefore, once at least one progression-free subset of size $m$ is found,

$$
r_k(N)=m.
$$

The candidate

$$
C=\{1,2,4,5\}
$$

is progression-free and has cardinality

$$
|C|=m=4.
$$

Since all candidates of cardinality $5$ have already been eliminated, no larger progression-free subset exists. Thus,

$$
\boxed{r_3(5)=4}.
$$

### 3.3 A Computational Method

Examining $r_3(5)$ manually assists with the conceptual understanding of the problem and helps identify opportunities to optimize the calculations.  However, correctly identifying candidate subsets and forbidden subsets of $S_N$ becomes increasingly tedious, error-prone, and time-consuming as $N$ grows.  It is therefore helpful to translate the algorithms and logic developed in the previous sections into programming code that can produce fast, consistent, and reproducible results.

This section does not directly contribute toward a solution of Erdős Problem 142. Rather, it describes the computational foundation used by the author to calculate $r_k(N)$ for somewhat larger values of $N$.

The examples in this section use Python, a general-purpose programming language chosen in part for its readable syntax and convenient support for combinatorial operations.  The code presented here is intended to be fit for the purposes of this investigation rather than an optimized implementation for large-scale computation.

#### 3.3.1 Identifying subsets

Python provides the `combinations()` function in its `itertools` module. Given a collection of elements and a desired subset size, `combinations()` generates every possible combination of that size without regard to order.

The following function generates all $k$-element subsets of $S_N$:

Function definition:
```
from itertools import combinations

def get_subsets(S: range, k: int) -> list:
    return list(combinations(S, k))

```
Example usage for $N=5, k=3$:
```
N = 5
k = 3
subsets = get_subsets(range(1, N + 1), k)
print(f"C({N},{k}) = {len(subsets)}")
print(subsets)

```
Output:
```
C(5,3) = 10
[(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]

```
For $N=5$ and $k=3$, the function returns $10$ subsets, agreeing with the manual calculation

$$
\binom{5}{3}=10.
$$

Observe that Python represents each combination as a tuple and therefore displays the elements using parentheses. In the mathematical context of this investigation, each tuple represents the corresponding subset of $S_N$.

#### 3.3.2 Identifying forbidden subsets

The next step is to identify which $k$-element subsets form arithmetic progressions. Rather than generating every $k$-element subset and testing each one individually, the arithmetic progression structure can be used directly.

From Section 3.1,

$$
d_{\max} = \left\lfloor\frac{N-1}{k-1}\right\rfloor
$$

and, for each allowable $d$,

$$
a_{\max}(d)=N-(k-1)d.
$$

The function below uses these bounds to generate every allowable pair $(a,d)$ and construct the corresponding arithmetic progression

$$
a,\;a+d,\;a+2d,\;\ldots,\;a+(k-1)d.
$$

Function definition:
```
def get_arithmetic_progression_subsets(N: int, k: int) -> list:
    progressions = []

    d_max = (N - 1) // (k - 1) #floor division to get the maximum possible common difference

    for d in range(1, d_max + 1):
        a_max = N - (k - 1) * d

        for a in range(1, a_max + 1):
            progression = tuple(a + i * d for i in range(k))
            progressions.append(progression)

    return progressions
```

Example usage for $N=5,k=3$
```
N = 5
k = 3

ap_subsets = get_arithmetic_progression_subsets(N, k)
print(f"Count: {len(ap_subsets)}")
print(ap_subsets)
```

Output:
```
Count: 4
[(1, 2, 3), (2, 3, 4), (3, 4, 5), (1, 3, 5)]
```

For $N=5$ and $k=3$, the program identifies the same four forbidden subsets found manually in Section 3.2.1:

$$
\{1,2,3\},\;
\{2,3,4\},\;
\{3,4,5\},\;
\{1,3,5\}.
$$

This provides a computational equivalent of the manual forbidden-subset generation process.

#### 3.3.3 Testing whether a candidate is progression-free

Once the forbidden subsets are known, a candidate subset $C$ can be tested by determining whether any forbidden subset $F$ satisfies

$$
F\subseteq C.
$$

The function below performs this subset-containment test. If even one forbidden subset is contained in the candidate, the function immediately returns `False`. If no forbidden subset is found, the function returns `True`, indicating that the candidate is progression-free.

Function definition:
```
def is_ap_free(candidate: tuple, progressions: list) -> bool:
    candidate = set(candidate)
    for progression in progressions:
        if set(progression).issubset(candidate):
            return False

    return True
```

Example usage:
```
N = 5
k = 3

ap_subsets = get_arithmetic_progression_subsets(N, k)

combination = (1, 2, 3, 5)
combination2 = (1, 2, 4, 5)

print(f"{combination} is AP-free: {is_ap_free(combination, ap_subsets)}")
print(f"{combination2} is AP-free: {is_ap_free(combination2, ap_subsets)}")
```

Output:
```
(1, 2, 3, 5) is AP-free: False
(1, 2, 4, 5) is AP-free: True
```

In the example above, $\{1,2,3,5\}$ is rejected because it contains forbidden subsets such as $\{1,2,3\}$. In contrast, $\{1,2,4,5\}$ contains none of the forbidden subsets and is therefore identified as progression-free.  This aligns with the findings from section 3.2.4.

#### 3.3.4 Calculating $r_k(N)$

The previous functions provide the components necessary to calculate $r_k(N)$. The remaining task is to examine candidate subsets by cardinality, beginning with the largest possible size and decreasing until a progression-free candidate is found.

Because the search proceeds from larger candidate sizes to smaller ones, the first progression-free candidate encountered determines $r_k(N)$. Once such a candidate is found, no smaller candidate sizes need to be examined.

```
def r(N: int, k: int) -> tuple:
    S = range(1, N + 1)
    progressions = get_arithmetic_progression_subsets(N, k)

    for size in range(N, 0, -1):
        for candidate in combinations(S, size):
            if is_ap_free(candidate, progressions):
                return size, candidate
```

Example usage:
```
N = 5
k = 3

max_size, candidate = r(N,k)
print(f"\nLargest {k}-AP-free subset of {{1, 2, ..., {N}}} has size {max_size}: {candidate}")
```

Output:
```
Largest 3-AP-free subset of {1, 2, ..., 5} has size 4: (1, 2, 4, 5)
```
For $N=5$ and $k=3$, the function returns a maximum size of $4$ and identifies $\{1,2,4,5\}$ as one progression-free candidate. This agrees with the manual result

$$
r_3(5)=4.
$$

#### 3.3.5 Calculating $r_3(N)$ for a range of $N$

Once the calculation of a single value $r_k(N)$ has been automated, the same function can be applied repeatedly while $N$ increases. This allows a sequence of values

$$
r_k(N),\;r_k(N+1),\;r_k(N+2),\ldots
$$

to be generated without manually repeating the subset analysis for each value of $N$.

The following code fixes $k=3$ and evaluates $r_3(N)$ over a consecutive range of values of $N$. The resulting values are stored so that they can later be tabulated, plotted, and examined for possible growth patterns.

Example usage:
```
N = 5
k = 3

cases = 17
results = []

print(f"{'N':>3} | {'r_k(N)':>6}")
print("-" * 12)

for i in range(N, N + cases):
    max_size, candidate = r(i, k)
    print(f"{i:>3} | {max_size:>6}")

    # Save point for Desmos
    results.append((i, max_size))
```

Output:
```
  N | r_k(N)
------------
  5 |      4
  6 |      4
  7 |      4
  8 |      4
  9 |      5
 10 |      5
 11 |      6
 12 |      6
 13 |      7
 14 |      8
 15 |      8
 16 |      8
 17 |      8
 18 |      8
 19 |      8
 20 |      9
 21 |      9

```

The output provides the first computational sequence of values for $r_3(N)$ used in this investigation. As $N$ increases, the values form a nondecreasing step-like sequence. These results provide the data used in the following sections to examine computational limitations and the apparent growth behavior of $r_3(N)$.


### 3.4 Computational Growth and Practical Limitations

A proposed approach for an initial empirical examination of the asymptotic behavior of $r_3(N)$ is to:

1. **Calculate $r_3(N)$ over a broad range of values of $N$.**

   An experimental range such as

   $$
   3\leq N\leq600
   $$

   spans a factor of

   $$
   \frac{600}{3}=200
   $$

   between the smallest and largest values of $N$. Such a range would provide substantially more information about long-term growth than the relatively small values examined manually.

2. **Separate the data into fitting and validation ranges.**

   One possible approach is to use

   $$
   3\leq N\leq100
   $$

   as an exploratory range for developing and fitting candidate growth models, while reserving

   $$
   101\leq N\leq600
   $$

   as a validation range.

   Candidate formulas developed using the first range could then be evaluated against values of $r_3(N)$ that were not used during the fitting process. Of particular interest would be whether the approximation becomes more accurate, remains stable, or deteriorates as $N$ increases.

One challenge with the approach outlined here is the sheer amount of computation required. The author noted a surprising increase in the time required to calculate $r_3(N)$ as $N$ grew larger. Upon further investigation, the root cause is the number of candidate subsets that must potentially be evaluated as the candidate cardinality, $m$, decreases.

The approach outlined in this paper evaluates candidate subsets one cardinality layer at a time, beginning with the largest possible cardinality. These layers can be represented by


$$
\binom{N}{N}, \binom{N}{N-1}, \binom{N}{N-2}, \binom{N}{N-3}\ldots
$$

If all cardinality layers are added together, the result is:

$$
\sum_{m=0}^{N} \binom{N}{m} = 2^N
$$

The quantity $2^N$ is the cardinality of the power set of $S_N$:

$$
|\mathcal{P}(S_N)|=2^N.
$$

The power set $\mathcal{P}(S_N)$ contains every possible subset of $S_N$ and therefore represents the complete space of possible candidate subsets. The algorithm does not necessarily examine every member of the power set, since it terminates once a progression-free candidate is found at the largest possible cardinality. Nevertheless, the size of the complete candidate space illustrates how rapidly the computational problem grows as $N$ increases.  Observe the following table:


The growth of the candidate space can be seen in the following examples:

| $N$ | $\binom{N}{3}$ | $\lvert\mathcal{P}(S_N)\rvert=2^N$ |
|---:|---:|---:|
| $3$ | $1$ | $8$ |
| $5$ | $10$ | $32$ |
| $30$ | $4,060$ | $1,073,741,824$ |
| $60$ | $34,220$ | $\approx1.15\times 10^{18}$ |
| $600$ | $35,820,200$ | $\approx4.15 \times 10^{180}$ |


### 3.5 Experimental Values of $r_3(N)$


### 3.6 Initial Examination of Asymptotic Behavior



## Acknowledgments

ChatGPT was used for editorial assistance, clarification of mathematical terminology, LaTeX formatting, Python coding assistance, and discussion of problem interpretation. Mathematical claims, computations, conclusions, and source verification remain the responsibility of the author.

## References

1. Erdős Problems, "Problem 142", [https://www.erdosproblems.com/142](https://www.erdosproblems.com/142). Accessed September 5, 2026.

2. Wikipedia contributors, "Paul Erdős," *Wikipedia, The Free Encyclopedia*.  
   [https://en.wikipedia.org/wiki/Paul_Erdős](https://en.wikipedia.org/wiki/Paul_Erd%C5%91s). Accessed September 5, 2026.

3. Kenneth H. Rosen, *Discrete Mathematics and Its Applications*, 8th ed.  
   New York, NY: McGraw-Hill Education, 2019.

4. Jacob Fox and Huy Tuan Pham, "Popular Progression Differences in Vector Spaces,"
   *International Mathematics Research Notices*, vol. 2021, no. 7,
   pp. 5261–5289, 2021. [https://doi.org/10.1093/imrn/rny240](https://doi.org/10.1093/imrn/rny240)

5. J. D. Murray, *Asymptotic Analysis*.  
   New York, NY: Springer, 2012.