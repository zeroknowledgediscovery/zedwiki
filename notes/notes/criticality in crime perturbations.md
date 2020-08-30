We nned to plot the spatial correlation function \\\(C(r)\\\) for \\\(r\in [0, R]\\\).
where \\\(R\\\) is potentially the max distance between tiles.

$$
C(r) = \frac{1}{c_0} \frac{\sum_{i,j} {\mathbf{U_i}} \cdot {\mathbf{U_j}} \delta(r-r_{ij})}{\sum_{i,j} \delta(r-r_{ij})}
$$

where 

$$
\delta(r) = \frac{1}{a\sqrt{\pi}}e^{-(x/a)^2}
$$
for some small value of $a$ (say a=0.01) and

+ \\\(r_{ij}\\\) is the distance between \\\(r_i,r_j\\\)
+ \\\(U_i\\\) is the perturbation response vector defined as the vector   where \\\( U_{prop}\\\) is the deviation of the average perturbation response of the tile, ie:

$$
U^{prop}_i = V^{prop}_i - \frac{1}{N} \sum_i V^{prop}_i
$$

where \\\(V^{prop}_i\\\) is the property crime response averaged over all perturbations at tile \\\(i\\\)