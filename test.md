@startuml
salt
{
{T
 + World
 ++ America
 +++ Canada
 +++ USA
 ++++ New York
 ++++ Boston
 +++ Mexico
 ++ Europe
 +++ Italy
 +++ Germany
 ++++ Berlin
 ++ Africa
}
}
@enduml

@startuml
[foo] lasts 21 days
[foo] is 40% completed
[sub] lasts 10 days
[sub] is 0% completed
[sub] starts at [foo]'s end
[bar] lasts 30 days and is 10% complete

@enduml

1. cynet has much lower number fo variables(2 orders of magnitude less)
2. nu. of variables inferred in cynet positively correlates with RNN performance (this implies that when the pattern is encode just as more states, rnns cope better. WHen it is encoded in teh structure and non-sync structure, then rnns fail)
3. physical system decay phase with distance, social systems dont
4. phase never goes negative for EQ (since within a delay of months, since events often lead to aftershocks, and absence of events increase prob of event.. no it is always positive phse on average)



# Figure 4 in FNet

## parsimony
> compare number of parameters

## depth 
> by link multiplicity, synthetic example, and from data

## multi-scale 
> no vanishing gradient (show nice spatial decay for weather and seismic, and not for crime)

## partial updates 
> show for crime

