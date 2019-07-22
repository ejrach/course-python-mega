# Making a basic Bokeh Line graph from Bachelors CSV file

#importing bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#prepare some data from csv
df = pandas.read_csv("bachelors.csv")
x = df["Year"]
y = df["Engineering"]

#prepare the output file
output_file("BachelorsCSV.html")

#create a figure object
f=figure()

#create line plot
f.line(x,y)

#triangle glyphs
#f.triangle(x,y)

#circle glyphs
#f.circle(x,y)

show(f)