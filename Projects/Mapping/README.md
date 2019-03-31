# course-python-mega

Application: Create Webmaps with Python and Folium

Inputs: Volcanoes.csv, world.json, webmappingviafile.py
Outputs: Map2.html
*See also the sytled version of this script.

Prerequisites:
1. Install Folium library from the terminal (used for the webmapping):
    pip3 install folium
2. Install Pandas library from the terminal (used to read CSV):
    pip3 install pandas

Description:
This project reads in a comma separated values file (txt or CSV) which contains a list of the volcanoes within the US. It
also reads a JSON file which contains population data throughout the world.
The program inputs the csv file and creates markers, changing them to a color which represents elevation.
The JSON population data is used to create a polygon layer representing different populations through the world.
Each layer is added to a feature group and can be turned on or off.

It will:
- use python dictionary's type
- Import JSON data which contains key/value pair
- Import excel (or comma separated values)
- use if-elif-else
- use for loops
- use lists
- use lambda function



