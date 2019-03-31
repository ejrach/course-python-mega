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
name = list(data["NAME"])

html = """
<h4>Volcano name:</h4>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

# Set the zoom on a certain area. Coordinates can eb obtained by going to google maps and right clicking "What's here?"
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")

# Set a feature groups
fg = folium.FeatureGroup(name="My Map")

# The zip method allows you to iterate through two lists, side by side
for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))

map.add_child(fg)

map.save("webmappingviafile_styled.html")


