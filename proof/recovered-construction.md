# Sharp price of replacing average constraints by per-posterior constraints

A signal scheme is a distribution of posteriors p on a finite-state probability simplex with barycenter p0. Let u≥0 be upper semicontinuous with λu(p)+(1−λ)u(q)≤M u(λp+(1−λ)q) for all p,q and λ∈[0,1]. Let m continuous convex constraints f_j have caps c_j. Assume M≥1. Write β=1/M, n=m+1, A_1=1 and
```
A_s = β max_{1≤i<s}(A_i+A_(s−i))  for s≥2.
```
Then the least universal constant is C(m,M)=n/A_n. This compares the average-feasible optimum to the pointwise-feasible optimum, including when the latter is zero.

## Upper bound

A full binary tree with leaf depths d_i yields a bound for any weighted posterior mixture: u(Σw_i p_i)≥Σw_i β^(d_i) u(p_i). This follows recursively from the pairwise inequality with child masses normalized at each node. Zero masses contribute nothing; for a node with only one positive child, the bound is still true since β≤1 and u≥0. The recursive definition of A_s gives the highest sum of leaf discount factors among s-leaf trees. Fix a maximizing n-leaf tree. For any mixture supported on at most n points, pad with zero weights and uniformly permute its entries onto the leaves. Averaging the tree inequality over those permutations gives
```
u(Σw_i p_i) ≥ (A_n/n) Σw_i u(p_i).
```

Start with any finite average-feasible scheme on posteriors p_i, weights w_i. Consider the polytope of all vectors v≥0 with Σv_i=1 and Σv_i f_j(p_i)≤c_j for each j. There is no barycenter restriction in this auxiliary polytope. Decompose w as a convex combination of its vertices. Each vertex v has support at most m+1: with more than m+1 positive entries, a nonzero perturbation supported there can preserve normalization and all m constraint expectations, so both sufficiently small signs of it remain feasible. For each vertex weight vector use one posterior p(v)=Σv_i p_i in the new scheme, with probability given by the decomposition. The new barycenter remains p0, and each p(v) satisfies the caps by convexity. The tree inequality ensures expected utility at least A_n/n times the old expected utility.

An arbitrary scheme can first be replaced by a finite one. The set of vectors (p,f_1(p),…,f_m(p),z) for 0≤z≤u(p) is compact by upper semicontinuity, boundedness of finite real-valued u on the compact simplex, and continuity of the f_j. Its convex hull is compact by finite-dimensional Carathéodory. The expectation vector for the original scheme belongs to that convex hull; represent it by a finite convex combination. Raising the represented z values back to u(p) does not change the barycenter or constraints and does not lower utility. Apply the finite argument and take suprema. There is no division by either optimum.

## Matching instance

Use n states, uniform prior p0, and the m=n−1 linear constraints f_i(p)=p_i, c_i=1/n for i=1,…,n−1. Bayes plausibility makes them always hold on average. Under pointwise feasibility, E p_i=1/n and p_i≤1/n force p_i=1/n almost surely, hence all posteriors are p0.

Define u(p) as the maximum over full binary trees whose leaves are bijectively labelled by supp(p) of Σ_i p_i β^(depth(i)). This lies in [0,1] and equals 1 at every point mass. It is upper semicontinuous: along any convergent sequence, extract a subsequence realizing its limsup with one fixed support and maximizing labelled tree. At the limit prune leaves of zero mass and suppress unary vertices, which cannot decrease the objective. The remaining tree is permitted at the limit point.

For pairwise approximate concavity when both mixture weights are positive, attach maximizing trees for p and q under a new root. The weighted discounted total is β[λu(p)+(1−λ)u(q)]. If a state occurs twice, transfer its total mixture weight to one of its shallowest occurrences and discard the other; this cannot decrease the total at fixed depths. Prune unused leaves and suppress unary vertices, again not decreasing the total. The resulting tree is permitted for the mixed posterior. This proves the required pairwise condition (the endpoint mixtures are automatic). Full revelation attains average-feasible utility 1. The unique pointwise-feasible posterior gives u(p0)=A_n/n. Hence the universal constant is attained.

## Closed forms

- For 1≤M≤2, let k=floor(log₂ n). Then A_n=(2^(k+1)−n)β^k+(2n−2^(k+1))β^(k+1). For 1<M<2, if a shallowest leaf depth a and deepest pair depth b satisfy b≥a+2, expand the shallow leaf and collapse the deepest sibling pair. This is a legitimate full-tree change preserving leaf count, and gains (2β−1)(β^a−β^(b−1))>0. A deepest leaf has a leaf sibling. Hence an optimum is balanced within one level, with the displayed counts by Kraft equality. For M=1 every tree sums to n; for M=2 every tree sums to 1, consistent at the endpoints.
- For M>2, A_1=1 and, for n≥2, A_n=Σ_{j=1}^{n−2}β^j+2β^(n−1). Indeed this comb sequence has increments β^(n−2)(2β−1), which are increasing, so its split-sum A_i+A_(n−i) is discretely convex and maximized at an endpoint. Induction verifies the recurrence.

In particular C(m,2)=m+1 and C(1,M)=M. The earlier [Babichenko–Talgam-Cohen–Zabarnyi, §5](https://arxiv.org/abs/2012.03272) argument gives M^m and its Proposition 5.5 gives the m+1 lower bound for M=2. This supplies the optimum for arbitrary m and M. No publication priority claimed.
