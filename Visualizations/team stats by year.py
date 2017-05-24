#import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from bokeh.plotting import figure, output_file, show, ColumnDataSource, curdoc
from bokeh.layouts import row, column
from bokeh.models import Legend, Select, Jitter, HoverTool, BoxSelectTool
from bokeh.client import push_session

min_year = 1981
max_year = 2016


#overlay all three
team_colors = {"WAS": ["#773141", "#FFB612", "black", "Redskins"], "PHI": ["#003B48", "#708090", "black", "Eagles"],
         "NYG": ["#192F6B", " #CA001A", "#A2AAAD", "Giants"], "DAL": ["#0D254C", "#87909B", "black", "Cowboys"],
         "GB": ["#175E22", "#FFB81C", "black", "Packers"], "MIN": ["#582C81", "#F0BF00", "black", "Vikings"],
         "CHI": ["#051C2C", "#DC4405", "grey", "Bears"], "DET": ["#006DB0", "#C5C7CF", "black", "Lions"],
         "SF": ["#AF1E2C", " #E6BE8A", "black", "49ers"], "LAR": ["#13264B", "#C9AF74", "grey", "Rams"],
         "ARI": ["#9B2743", "#FFB612", "black", "Cardinals"], "SEA": ["#001433", "#4DFF00", "#245998", "Seahawks"],
         "CAR": ["#0085CA", "#101820", "#A5ACAF", "Panthers"], "ATL": ["#A6192D", "black", "grey", "Falcons"],
         "TB": [" #D60A0B", "#FF7900", "#89765F", "Buccaneers"], "NO": ["#D2B887", "black", "grey", "Saints"],
         "NE": ["#0D254C", "#C80815", "#D6D6D6", "Patriots"], "MIA": ["#008D97", "#F5811F", "grey", "Dolphins"],
         "BUF": ["#00338D", "#C60C30", "black", "Bills"], "NYJ": ["#0C371D", "grey", "black", "Jets"],
         "LAC": ["#0C2340", "#FFB81C", "#0072CE", "Chargers"], "DEN": ["#FC4C02", " #0C2340", "grey", "Broncos"],
         "KC": ["#C8102E", "#FFB81C", "grey", "Chiefs"], "OAK": ["black", "#C4C8CB", "#303030", "Raiders"],
         "PIT": ["#FFB81C", "#101820", "grey", "Steelers"], "BAL": ["#280353", "#D0B240", "black", "Ravens"],
         "CLE": ["#eb3300", "#301f10", "grey", "Browns"], "CIN": ["#FB4F14", "black", "grey", "Bengals"],
         "HOU": ["#02253A", "#B31B34", "grey", "Texans"], "IND": ["#003B7B", "black", "grey", "Colts"],
         "JAX": ["#006778", " #D7A22A", "black", "Jaguars"], "TEN": ["#648FCC", "#0D254C", "red", "Titans"]}
         # detroit switch to grey?
         # OAK tinker

cardinals = pd.read_csv("../ProcessedData/Teamified/ARI.csv")
year = list(cardinals["Year"])
oscore = list(cardinals["Oscore_Rank"])
dscore = list(cardinals["Dscore_Rank"])
stscore = list(cardinals["STscore_Rank"])

source = ColumnDataSource(
        data=dict(
            year=year,
            oscore=oscore,
            dscore=dscore,
            stscore=stscore
        )
    )
        
def callback(old, new, attr):
    print("updating....")
    print(old)
    print(new)
    team_data = pd.read_csv("../ProcessedData/Teamified/" + new.value + ".csv")
    source.data = {
        'year' : list(team_data["Year"]),
        'oscore' : list(team_data["Oscore_Rank"]),
        'dscore': list(team_data["Dscore_Rank"]),
        'stscore': list(team_data["STscore_Rank"]),
        }
         

hover = HoverTool(
        tooltips=[
            ("Year", "@year"),
            ("Offense Rank", "@oscore"),
            ("Defense Rank", "@dscore"),
            ("S/T Rank", "@stscore"),
        ],
        names=["Glyphs"]
    )
         
TOOLS = [BoxSelectTool(), hover]

p = figure(x_axis_label='Year', y_axis_label='Rank', title='Team Offense/Defense/Special Teams Rank by Year', tools=TOOLS)
p.y_range.start=35
p.y_range.end=0
p.x_range.start=min_year-1
p.x_range.end=max_year+1

p.line(x='year', y='oscore', color='blue', alpha=0.5, legend="Offense Rank", source=source)
p.circle(x='year', y='oscore', color='blue', line_color="yellow", legend="Offense Rank", size=15, source=source, name="Glyphs", hover_fill_color="pink", hover_line_color="#FF1493", hover_alpha=1.0)
p.line(x='year', y='dscore', color='brown', alpha=0.5, legend="Defense Rank", source=source)
p.diamond(x='year', y='dscore', color='brown', line_color="white", legend="Defense Rank", size=20, source=source, name="Glyphs", hover_fill_color="pink", hover_line_color="#FF1493", hover_alpha=1.0)
p.line(x='year', y='stscore', color='black', alpha=0.5, legend="S/T Rank", source=source)
p.asterisk(x='year', y='stscore', color='black', legend="S/T Rank", size=15, source=source, name="Glyphs", hover_fill_color="pink", hover_line_color="#FF1493", hover_alpha=1.0)
p.legend.location = "bottom_left"
p.legend.orientation="horizontal"
p.legend.background_fill_alpha = 0.8
p.legend.legend_margin = 0
p.legend.legend_padding=10
p.legend.border_line_color="Black"
p.xgrid.grid_line_color = "White"
p.ygrid.grid_line_color = "White"
p.background_fill_color = "green"
p.background_fill_alpha = 0.5
p.legend.background_fill_color = "yellow"
p.legend.background_fill_alpha = 0.5
select = Select(title="Team", options=sorted(list(team_colors.keys())), value='ARI')
select.on_change('select.value', callback)
layout = column(select, p)
curdoc().add_root(layout)
output_file("test.html")
show(layout)