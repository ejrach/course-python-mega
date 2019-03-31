# First need to do a "pip3 install folium"
import folium

# Create a map object, zoomed in at the location you provide.
# To get coordinates, go to a google map, zoom in to a location
# and right click "What's here?". Copy and paste coordinates.
map = folium.Map(location=[33.953329, -116.508226], zoom_start=7, tiles="Mapbox Bright")

# Using feature groups help you to organize your code, when you add a layer control feature.
fg = folium.FeatureGroup(name="My Map")

# Now we want markers on the base map. Go to terminal window and type "dir(folium)" 
# to see available methods. If you find something, to get help on it type "help(folium.Marker)"
# in the terminal window.
# fg.add_child(folium.Marker(location=[33.5,-116.2], popup="Hi I am a marker", icon=folium.Icon(color='green')))
# fg.add_child(folium.Marker(location=[33.2,-116.9], popup="Hi I am a marker", icon=folium.Icon(color='green')))

# Or the points can be added in a for loop
for coordinates in [[33.5,-116.2],[33.2,-116.9]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a marker", icon=folium.Icon(color='green')))


map.add_child(fg)

# Save the map
map.save("Map1.html")


