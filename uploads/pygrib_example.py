import pandas as pd
import pygrib


fname = 'gfs_3_20190101_0000_384.grb2'
grbs = pygrib.open(fname)

with open('meta.csv', 'w') as handle:
    for i, g in enumerate(grbs):
        handle.write(str(g) + '\n')

df = pd.read_csv('meta.csv', sep=':', header=None, index_col=0)
df.columns = ['name', 'units', 'gridType', 'typeOfLevel', 'level', 'forecastTime', 'dataDate']
df.to_csv('meta.csv', index=False)
print(df.head())

# Get forecast for the north America for Visibility (record 1) 
grb = grbs.message(1)
print(grb)
data, lats, lons = grb.data(lat1=20,lat2=70,lon1=220,lon2=320)

