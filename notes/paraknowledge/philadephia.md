# Data source


+ OpenDataPhilly. Here’s shooting victims: 
https://opendataphilly.org/datasets/shooting-victims/

+ And here’s incidents: 
https://opendataphilly.org/datasets/crime-incidents/

## LA

https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8

## SF

https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-2018-to-Present/wg3w-h783

## maricopa

https://police.maricopa.edu/daily-crime-log

## incidents

https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&format=csv&q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272020-01-01%27%20AND%20dispatch_date_time%20%3C%20%272024-01-01%27

## API documentation

https://cityofphiladelphia.github.io/carto-api-explorer/#incidents_part1_part2

## Code

```

import requests

def fetch_incidents(start_year, end_year):
    base_url = "https://phl.carto.com/api/v2/sql"
    
    # Construct the SQL query with given years
    query = f"""SELECT *, ST_Y(the_geom) AS lat, ST_X(the_geom) AS lng 
                FROM incidents_part1_part2 
                WHERE dispatch_date_time >= '{start_year}-01-01' 
                AND dispatch_date_time < '{end_year}-01-01'"""

    params = {
        "filename": "incidents_part1_part2",
        "format": "csv",
        "q": query
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises a HTTPError if the HTTP request returned an unsuccessful status code

        # Return CSV data or save it as needed
        return response.text

    except requests.RequestException as error:
        print(f"Error fetching data: {error}")
        return None

if __name__ == "__main__":
    start_year = input("Enter start year (e.g., 2020): ")
    end_year = input("Enter end year (e.g., 2024): ")

    data = fetch_incidents(start_year, end_year)
    if data:
        # Print the fetched data or save it as required
        print(data)

```



# contact
Bob Kothari