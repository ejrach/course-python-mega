import folium
import pandas

# read the data
data = pandas.read_csv("Volcanoes.csv")

# If you check the type of data, it is "DataFrame"
#print(type(data))

# Split the column data into their own lists for easier iteration
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# define a function to return a color based on elevation.
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

# Set the zoom on a certain area. Coordinates can eb obtained by going to google maps and right clicking "What's here?"
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

# Set a feature group for volcanoes
fgv = folium.FeatureGroup(name="Volcanoes")

### Add the Marker Layer ###
# The zip method allows you to iterate through two lists, side by side
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m", 
    fill_color=color_producer(el), color = 'grey', fill=True, fill_opacity=0.7))


### Add the JSON Population Layer ###
# Set a feature group for Population
fgp = folium.FeatureGroup(name="Population")

# Creates a GeoJson oject, add adds polygons. This json file could also contain lines as well
data_json = open("world.json", 'r', encoding='utf-8-sig').read()

# To understand how the population is obtained, ['properties']['POP2005'] is used 
# to access the data.
fgp.add_child(folium.GeoJson(data=data_json, 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map2.html")


