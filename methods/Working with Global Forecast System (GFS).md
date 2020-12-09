# GFS Data portal
The data portal Global Forecast System (GFS) is [here](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs).

Scroll down to the **Product Types/GFS Forecasts** section of the webpage.
And we are going to use **GFS 003 (1º)-Domain**. 
The 003 is a code for the grid used for covering the earth. There are finer choices.  

The `HTTPS` and `TDS` data access links only have the most recent data, so for historical forecast data, we use `AIRS`.

[[/uploads/GFS_portal.png|height=400px,alt=GFS forecast]]

# Submit request to `AIRS`

[[/uploads/GFS_AIRS.png|height=400px,alt=GFS AIRS Request submission page]]

It seems GFS does forecast 4 times a day at 0, 6, 12, 18. I don't think we actually need all 4 model cycles, but I download them all and probably average the predictions later. A single request has an upper limit of 250GB, and a month worth (4 cycles) of data is okay to be request at the same time. After choose the cycle(s) and data, input an email address, and press `Proceed with Order`. It will take a while to submit and process the order, so be patient. 

If a request is submitted correctly, you can press `Check order status` button to see the progress of your order.

[[/uploads/GFS_order_status.png|height=400px,alt=GFS order status]]

After the order is done, you can find the download link at `Delievery Location`. Here is the an example of the download page

[[/uploads/GFS_download_page.png|height=300px,alt=GFS download page]]

Download one `tar` file, for example `gfs_3_2019010100.g2.tar`, and save it to a directory and in the directory run
```
$ tar -xf gfs_3_2019010100.g2.tar
```
Each tar file contains many files, one for each horizon. For day 0 to day 9, GFS forecasts for every 3 hours, and for day 9 to day 15, every 12 hours. The file names last field is the prediction horizon in hours. 

In the example below, we will use the file `gfs_3_20190101_0000_384.grb2`, so download [here](/uploads/gfs_3_20190101_0000_384.grb2) if you want to try out the code.

## Naming rule of GFS forecast file
The GFS forecast is named as follows: `gfs_[grid type]_[forecast-on date YYYYMMDD]_[cycle00]_[horizon].grb2` and `cycle` takes value in `00, 06, 12, 18`.

# The organization of a `grb` file
The GFS forecast `grb` file is organized as follows: it records locations and values for many variables. Each record of a `grb` files is a 3-tuple: (variable description, locations (a 2d matrix), values (a 2d matrix)).

# Process the `grb` file with python
We first have to install a package that can process `grb` file. 
```
$ python3 -m pip install --user pygrib
```
The PyPi page: https://pypi.org/project/pygrib/
Usage example: https://jswhit.github.io/pygrib/api.html#example-usage

We first load packages `pygrid` and `pandas`. We use pandas to process the meta data of the `grb` file 
```
import pandas as pd
import pygrib
```
Here we show how to save the variable descriptions to a more conventional dataframe. 
Note: the columns here is specific to the `grb` file we are interested in. 
```
fname = 'gfs_3_20190101_0000_384.grb2'
gr = pygrib.open(fname)

with open('meta.csv', 'w') as handle:
    for i, g in enumerate(gr):
        handle.write(str(g) + '\n')

df = pd.read_csv('meta.csv', sep=':', header=None, index_col=0)
df.columns = ['name', 'units', 'gridType', 'typeOfLevel', 'level', 'forecastTime', 'dataDate']
df.to_csv('meta.csv', index=False)
df.head()
```
Output is:


Use the following 
```
grb = grbs.message(1)
print(grb)
data, lats, lons = grb.data(lat1=20,lat2=70,lon1=220,lon2=320)
```
Output: `1:Visibility:m (instant):regular_ll:surface:level 0:fcst time 384 hrs:from 201901010000`
