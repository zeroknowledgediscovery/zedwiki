We nned to plot the spatial correlation function \\\(C(r)\\\) for \\\(r\in [0, R]\\\).
where \\\(R\\\) is potentially the max distance between tiles.

$$
C(r) = \frac{1}{c_0} \frac{\sum_{i} {\gamma_i} \delta(r-r_{i})}{\sum_{i} \delta(r-r_{i})}
$$

where 

$$
\delta(r) = \frac{1}{a\sqrt{\pi}}e^{-(x/a)^2}
$$
for some small value of $a$ (say a=0.01) 

and \\\( c_0\\\)  is chosen such that \\\(C(r=0) = 1\\\)

and  \\\(r_{i}\\\) is the distance between tiles

