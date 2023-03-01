import json
from plotly.graph_objs import Layout
from plotly import offline

filename = 'Projects/Data-Visualization/chapter_16/mapping_global_data/data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_text = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    text = eq_dict['properties']['place']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(text)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text,
    'marker': {
        'size': [5*mag for mag in mags],
        'color':mags,
        'colorscale': 'Viridis',
        'reversescale':True,
        'colorbar':{'title': 'Magnitude'},
    }
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
