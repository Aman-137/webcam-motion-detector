from motion_detector import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

df["Start_String"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

p = figure(width=500, height=100, x_axis_type='datetime', responsive=True, titll = "Motion Graph")    # I think "responsive" is removed from bokeh so it will show error.

p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.designed_num_tick = 1

hover = HoverTool(tooltips = [("Start", "@Start_String"), ("End", "@End_string")])   #List of tuples

q = p.quad(left="Start", right="End", bottom=0, top=1, color="Green", source=cds)

output_file("Graph.html")

show(p)
