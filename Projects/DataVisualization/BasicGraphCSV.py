# Making a basic Bokeh Line graph from CSV file

#importing bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#prepare some data from csv
df = pandas.read_csv("data.csv")
x = df["x"]
y = df["y"]

#prepare the output file
output_file("LineCSV.html")

#create a figure object
f=figure()

#create line plot
#f.line(x,y)

#triangle glyphs
#f.triangle(x,y)

#circle glyphs
f.circle(x,y)



show(f)