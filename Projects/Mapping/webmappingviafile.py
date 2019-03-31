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

# Set a feature groups
fg = folium.FeatureGroup(name="My Map")

# The zip method allows you to iterate through two lists, side by side
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m", 
    fill_color=color_producer(el), color = 'grey', fill=True, fill_opacity=0.7))

map.add_child(fg)

map.save("Map2.html")


