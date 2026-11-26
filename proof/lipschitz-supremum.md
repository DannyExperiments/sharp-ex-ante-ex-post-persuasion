# Q489 appendix: the sharp supremum for Lipschitz utilities

In the notation of the delivered result, the worst-case sharp factor n/A_n, n=m+1, also holds as a supremum when the sender utility is restricted to be Lipschitz. No claim that this factor is always attained in that class.

Let u:Δ→[0,1] be the upper-semicontinuous tree utility. Write U_r(x)=max{u(z): z∈Δ, ||z−x||≤r} and V_ε(x)=ε^(−1)∫_0^ε U_r(x)dr. The maximum exists by compactness and upper semicontinuity; the integrand is monotone in r and bounded. If x',y' maximize in their respective radius-r balls, then λx'+(1−λ)y' lies within r of λx+(1−λ)y and belongs to the simplex. Applying the original pairwise M-inequality to x',y' proves the identical inequality for U_r, and integration proves it for V_ε. No change in M is needed.

For d=||x−y|| the ball inclusion gives U_r(x)≤U_(r+d)(y). The difference between the radius integrals from d to ε+d and from 0 to ε is at most d, since the integrand is in [0,1] (for d>ε the claim also follows from 0≤V_ε≤1). Reverse x,y to obtain |V_ε(x)−V_ε(y)|≤d/ε. Upper semicontinuity and containment of x in its own ball imply U_r(x)↓u(x) as r↓0, and hence V_ε(x)↓u(x).

Use uniform p on n states and m ex-post constraints x_i≤1/n, i≤m. The ex-ante optimum is 1 under full revelation, since V_ε(e_i)=1. In any ex-post feasible Bayes-plausible distribution each of the first m coordinates is 1/n almost surely, so the sole posterior is p. Use the infinity norm and 0<ε<1/n, so balls around p have full support. Each eligible tree form has coefficient sum at most A_n and nonnegative coefficients, hence at every z in the r-ball its value is at most A_n/n+A_n r. Therefore V_ε(p)≤A_n/n+A_n ε/2 and the ratio is at least (n/A_n)/(1+nε/2). Together with the existing universal upper bound, this gives the sharp supremum and an explicit approximation error. This coefficient-sum estimate slightly strengthens the bound nε/2 on the value error.

[Source model, §5](https://arxiv.org/html/2012.03272v2#S5).
