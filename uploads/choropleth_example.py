import pandas as pd
import plotly.express as px
import json
from urllib.request import urlopen


df = pd.read_csv('choropleth_for_wiki.csv', dtype={'fips': str})

counties_webpage = 'https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json'
with urlopen(counties_webpage) as response:
    counties = json.load(response)

fig = px.choropleth(
    df, 
    geojson=counties, 
    locations='fips', 
    color='val',
    color_continuous_scale='viridis',
    range_color=(df['val'].min(), df['val'].max()), 
    scope='usa'
)

fig.update_layout(
    margin={'l': 0, 'b': 0, 'r': 0, 't': 0},            
    coloraxis_showscale=True,                           
    coloraxis_colorbar={
        'title': 'Risk',                                
        'titlefont': {'size': 25, 'color': 'black'},    
        'lenmode': 'pixels',                            
        'len': 500,                                     
        'thicknessmode': 'pixels',                      
        'thickness': 15,                                
        'xpad': 25,                                     
        'x': .91,                                       
        'tickfont': {'size': 25, 'color': 'black'},     
        'ticks': 'inside',                              
        'ticklen': 14.5,                                
        'thicknessmode': 'pixels',                      
    }
)

fig.update_traces(marker_line_width=.1)

fig.write_image(
    file='choropleth_for_wiki.pdf', 
    format='pdf', 
    engine='kaleido',  
    width=1000,  
    height=600)

disable_interaction = True
if disable_interaction:
    config = {'scrollZoom': False, 'displayModeBar': False}
else:
    config = None
    
fig.show(config=config)

