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