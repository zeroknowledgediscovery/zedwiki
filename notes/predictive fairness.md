Briefly, I was recently asked to review a paper for the Journal of the Academy of Consultation-Liaison Psychiatry. The paper uses archival data to compare the sensitivity and specificity of a suicide screener (the ASQ) across white and black youth in emergency departments. Results showed these two scale properties are essentially identical across those two groups. They use this result to conclude the ASQ performs equivalently well for these two racial groups.

> In my review, I explained when base rates are unequal across groups, you cannot have both equal sensitivity/specificity and equal PPV/false positive rate at the same time. In this case, I explained the base rates of suicidal behavior are known to be lower for black youth than white youth – and have been for at least 30 years, despite some recent gap-closing. Thus, if the sensitivity and specificity of the ASQ is held constant across both two groups, then the false positive rate (FPR) is guaranteed to be higher for black youth. I calculated that gap to be about a 5% higher FPR in this case. This might seem like a small discrepancy, but for a screener designed to be applied frequently in ED settings, these recurring errors add up to a non-ignorable problem that field should think through proactively.


In cases like this, you simply cannot avoid the ASQ producing at least some kind of cross-group disparity. Instead, you unfortunately forced to choose just between different types of disparities (e.g., in FPR or sensitivity or different scale cutoffs by race). I argued you should therefore be explicit about how you made that choice, rather than defaulting simply to optimizing sensitivity/specificity.

Although the author’s (somewhat aggressively) declined to address this issue as a limitation/future direction in the paper, the editor (also our department chair) asked me to write a commentary on the paper exploring this issue.

Personally, I’m excited by the editor/chair’s request. I think the idea of a forced choice between different types of “predictive fairness” presents the field with an opportunity to be much more thoughtful about how our the design and use of  our predictive instruments going forward. If we can no longer pretend that anything is possible with just the right set of questions, what would we prefer to do instead? Other fields like computer science have already dived head in to this new area of algorithmic fairness and I’d like to make an argument that the health sciences should do the same.

 With that said, I’d be especially grateful for input from someone more senior, especially someone who has been in the position of balancing different scale features in the past – even better, someone who has had to think through those issues for suicide screening. If you could ask Dr. Gibbons for his thoughts on the topic, I would again be very grateful.

 Specifically, does he agree that the commentary has sufficiently fertile content to be worth writing? For example, is a frank discussion of forced choices in the types of “predictive fairness” worth proactive consideration for screener design and implementation? If yes, does he have thoughts on the best way to address those forced choices? For example, should we just maximize PPV at the cost of all else? Or maybe should we survey stakeholders to see what kinds of predictive errors they think are most fair?
 
 
 1. You are aboslutely correct that we cannot have same sensitivity in two groups with different base rates. This easy to see, of course, from:
 $$PPV = \frac{s}{s+ (\frac{1}{p}-1)(1-c)} $$

we can conclude:

$$\frac{f_p}{f^B_p} = \frac{\frac{1}{p}-1}{\frac{1}{p^B}-1}\times \frac{P}{P^B}$$
 
 So $$p^B < p \Rightarrow  fp < f_p^B$$
 
 if we are choosing the two groups as having the same number of positive cases.
 
 
 
 