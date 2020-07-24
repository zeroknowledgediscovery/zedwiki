# Non-parametric vs Parametric Statistics

The main idea of nonparametric statistics is to make inferences about unknown quantities without resorting to
simple parametric reductions of the problem For example, suppose \\\(X \sim F\\\) , and we wish to estimate, say
\\\(E(X) or P(X > 1)\\\)

The approach taken by parametric statistics is to assume that \\\( F \\\) belongs to a family of distribution functions that can be described by a small number of parameters, e.g., the normal distribution:

$$ f(x) = \frac{1}{\sqrt{2 \pi \sigma^2}} exp \{ -\frac{(x-\mu)^2}{2 \sigma^2} \} $$

These parameters are then estimated, and we make inferences
about the quantities we were originally interested in (\\\(E(X)\\\) or \\\(P(X > 1)\\\)) based on assuming \\\(X \sim N(\mu,\sigma^2) \\\)

Or suppose we wish to know how \\\(E(Y )\\\)  changes with \\\(x\\\)
Again, the parametric approach is to assume that
\\\(E(Y \vert x) = \alpha + \beta x\\\). We estimate \\\(\alpha \\\) and \\\(\beta\\\), then base all future inference on those
estimates.

Both of the aforementioned parametric approach rely on a reduction of the original problem, assuming that all uncertainty can be reduced to just two unknown numbers. If these assumptions are true, then of course, there is nothing
wrong with making them. If they are false, however:

+ The resulting statistical inference will be questionable
+ We might miss interesting patterns in the data

# \\\(1-\alpah\\\) Confidence Bounds from DKW 

$$ \epsilon = \sqrt{\frac{1}{2n} \log \frac{2}{\alpha}} $$
