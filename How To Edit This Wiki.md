# GOLLUM page 

https://github.com/gollum/gollum

https://github.com/gollum/gollum/wiki

# Top Level

Use the hash sign to organize levels, as in standard markdown syntax.
Single hash (#) is the top level, 2 hashes one level down etc.

# Organization

+ We have a few directories: [methods](http://34.66.189.202:4567/gollum/overview/methods/), [project](http://34.66.189.202:4567/gollum/overview/project/), [reading](http://34.66.189.202:4567/gollum/overview/reading/), [notes](http://34.66.189.202:4567/gollum/overview/notes/), [development](http://34.66.189.202:4567/gollum/overview/development/)
+ Put topics ie new pages in respective directories. For example any develooment notes goes into development. Any new poject goes into project
+ The [reading](http://34.66.189.202:4567/gollum/overview/reading/) pages are backgrouns information, and required or optional reading in the ZeDLab

# Inserting math

\\\( \alpha \\\)

$$ \alpha + \beta $$

# Inserting Images and Links

+ Home page only has the global TOC
+ Note that pages should be linked like: \[\[page name\]\]
+ External link:  [Alex Leow](alexxxllet@gmail.com) inserted as follows: \[Alex Leow\]\(alexxxllet@gmail.com\)
+ Images example: ![submission status](https://img.shields.io/badge/submission%20status-under%20review-green) inserted as follows \!\[text\]\(path_to_image\)
+ You can upload files as well
+ Link To Gihub Repo if Possible  [Manic Episode Prediction](https://github.com/zeroknowledgediscovery/pub_manic_)

# Status Badges
![submission status](https://img.shields.io/badge/submission%20status-under%20review-green)
![submission status](https://img.shields.io/badge/submission%20status-submitted-yellow)
![submission status](https://img.shields.io/badge/submission%20status-preparation-orange)
![submission status](https://img.shields.io/badge/submission%20status-preparation-lightgrey)

![draft](https://img.shields.io/badge/draft%20status-complete-green)
![draft](https://img.shields.io/badge/draft%20status-preparation-yellow)
![draft](https://img.shields.io/badge/draft%20status-preparation-orange)
![draft](https://img.shields.io/badge/draft%20status-preparation-lightgrey)

![results](https://img.shields.io/badge/draft%20status-complete-green)
![results](https://img.shields.io/badge/draft%20status-preparation-yellow)
![results](https://img.shields.io/badge/draft%20status-preparation-orange)
![resultss](https://img.shields.io/badge/draft%20status-preparation-lightgrey)


## UML Diagroams

@startuml
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response
Alice -> Bob: Another authentication Request
Alice <-- Bob: another authentication Response
@enduml


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