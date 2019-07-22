
#http://www.google.com/finance/historical?q=NASDAQ:ADBE&startdate=Jan+01%2C+2009&enddate=Aug+2%2C+2012&output.csv

from bokeh.plotting import figure, output_file, show
import pandas

#load the dataframe object
df=pandas.read_csv("http://www.google.com/finance/historical?q=NASDAQ:ADBE&startdate=Jan+01%2C+2009&enddate=Aug+2%2C+2012&output.csv",parse_dates=["Date"])

p=figure(width=500, height=250, x_axis_type="datetime", responsive=True)

p.line(df["Date"],df["Close"],color="Orange",alpha=0.5)

output_file("TimeSeries.html")

show(p)
