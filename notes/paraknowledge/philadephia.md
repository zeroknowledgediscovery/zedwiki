# Data source


+ OpenDataPhilly. Here’s shooting victims: 
https://opendataphilly.org/datasets/shooting-victims/

+ And here’s incidents: 
https://opendataphilly.org/datasets/crime-incidents/


## incidents

https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272023-01-01%27%20AND%20dispatch_date_time%20%3C%20%272024-01-01%27

## API documentation

https://cityofphiladelphia.github.io/carto-api-explorer/#incidents_part1_part2

# contact
Bob Kothari