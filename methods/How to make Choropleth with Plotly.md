First, let us start with some helpful tutorial webpages:

1. [plotly Choropleth in general.](https://plotly.com/python/choropleth-maps/)
2. [Colorbar parameters.](https://plotly.github.io/plotly.py-docs/generated/plotly.graph_objects.choropleth.html#plotly.graph_objects.choropleth.ColorBar)
3. [Layout.](https://plotly.com/python/reference/layout/#layout-legend)
4. [Trace.](https://plotly.com/python/reference/choropleth/)
4. [Color scale.](https://plotly.com/python/builtin-colorscales/)

Here is a minimal(ish) working example:

I cut it up in parts to provide some explanation in between, I will link you to the full example code and data files used by the end of this tutorial.
```
import pandas as pd
import plotly.express as px
import json
from urllib.request import urlopen
```
Plotly Choropleth works with pandas data frame, so if you have data another form, you still need to organize it in `pandas.dataframe` format ([tutorial here](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html)). 
Now, let us load the data:
**IMPORTANT:** When loading the data frame, the fips column must be read as string (`type`) or otherwise the leading zeros will disappear.
A minimal working data frame for choropleth only need two columns:

1. a `fips` column, specifying locations;
2. a `val` column, specifying the colors of the heat map;

```
df = pd.read_csv('choropleth_for_wiki.csv', dtype={'fips': str})
```

Now we get the geojson file that contains the polygons of county boundaries.

```
counties_webpage = 'https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json'
with urlopen(counties_webpage) as response:
    counties = json.load(response)
```
Now we plot. In this example, we plot all the US counties (including Alaska and Hawaii). 
```
fig = px.choropleth(
    df, 
    geojson=counties, 
    locations='fips', 
    color='val',
    color_continuous_scale='viridis',
    # this is one example, feel free to choose your own range
    range_color=(df['val'].min(), df['val'].max()), 
    scope='usa'
)
```
I got terribly confused at the beginning, so here is a little reminder: The `fig` object above has nothing to do with a Matplotlib `figure` object although it is also conventionally named as `fig`. 
Fundamentally, Plotly figure object is designed for *interactivity* (zooming in and out, moving, and showing information when pointing your mouse to a part of the map).

Now we update the layout of the figure object `fig`. 
There are a lot more parameters then shown here that you can modify
(See the *layout* and *colorbar parameters* links on the top).
```
fig.update_layout(
    margin={'l': 0, 'b': 0, 'r': 0, 't': 0},                    # can only have >=0 values
    coloraxis_showscale=True,                                   # weather to show colorbar or not
    coloraxis_colorbar={
        'title': 'Risk',                                        # colorbar title
        'titlefont': {'size': 25, 'color': 'black'},            # title font size and color
        ##=========================== Shape ===========================##
        'lenmode': 'pixels',                                    # the unit of color bar height (['fraction', 'pixels'])
        'len': 500,                                             # color bar height (in this case, 500 pixels)
        'thicknessmode': 'pixels',                              # the unit of color bar width (['fraction', 'pixels'])
        'thickness': 15,                                        # color bar width (in this case, 20 pixels)
        ##=========================== Positioning ===========================##
        'xpad': 25,                                             # sets the amount of padding (in px) along the x direction
        'x': .91,                                               # the x relative position ([-2,3]) of the colorbar
        ##=========================== Tick parameters ===========================##
        'tickfont': {'size': 25, 'color': 'black'},             # tick font size and color
        'ticks': 'inside',                                      # the little ticks can stick out or inside
        'ticklen': 14.5,                                        # the length of the ticks
        'thicknessmode': 'pixels',                              # the unit of color bar width
    }
)
```
We can also change the county boundary parameters by update traces.
```
fig.update_traces(marker_line_width=.1)
```
Since we sometimes just want to use the plot for publication, we need to disable the interactions (shown below) since it can be a little annoying (and slow) when you want the plot to stay put for viewing.  
```
disable_interaction = True
if disable_interaction:
    config = {'scrollZoom': False, 'displayModeBar': False}
else:
    config = None
fig.show(config=config)
```
