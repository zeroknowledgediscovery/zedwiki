## Code to download csv from [USGS](https://earthquake.usgs.gov/)
API documentation [page](https://earthquake.usgs.gov/fdsnws/event/1/)

**NOTE:** USGS has 20000 items per query limits. If we only want to download earthquake with magnitude greater than 2.0, we can try a query a month at a time. I queried 3 day at a time just to be safe.

**Query Parameters:**

1. `eventtype=earthquake`;

2. `minmagnitude=2.0`;

3. `format=csv`; (there are other formats but it seems that csv is most convenient for cynet application)

4. `starttime` and `endtime`;

The first 3 paramters are fixed, while `starttime` and `endtime` has to be given for each "sub-query".
```
import requests
import csv
import pandas as pd

api_url_base = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&eventtype=earthquake&minmagnitude=2.0&starttime={}&endtime={}'

date_range = pd.date_range(start='2009-01-01', end='2020-01-01', freq='3D')

dfs = []
bad_requests = []
for i in range(len(date_range) - 1):
    starttime = date_range[i]
    endtime = date_range[i + 1]
    api_url = api_url_base.format(starttime.date(), endtime.date())
    
    with requests.Session() as s:
        download = s.get(api_url)
        status = download.status_code
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
    
    if status != 200:
        bad_requests.append(api_url)
        print('{}-{}: bad request!'.format(starttime, endtime))
    else:
        columns = my_list[0]
        data = my_list[1:]
        df = pd.DataFrame(columns=columns, data=data)
        dfs.append(df)
        print('{}-{}: {} events'.format(starttime, endtime, len(df)))

df = pd.concat(dfs)
df.sort_values(by='time').to_csv('earthquakes_2009-01-01_2019-12-31.csv', index=False)
```