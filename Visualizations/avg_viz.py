from bokeh.plotting import show, output_file, curdoc
from bokeh.layouts import gridplot
#from bokeh.models import HoverTool, BoxSelectTool
from bokeh.charts import HeatMap
import bokeh.palettes as palette
import pandas as pd
from scipy.stats import percentileofscore
from copy import deepcopy

min_year = 1981
max_year = 2016

# Fmb, Y/Play, APYd, YppYprRatio, AllTD

avg_data = pd.read_csv("../ProcessedData/Teamified/AVG.csv")
years = list(avg_data["Year"])

# apply scipy.stats.percentileofscore to all values in all lists
PF = list(avg_data["PF"])
Plays = list(avg_data["Ply"])
TotalYds = list(avg_data["TotalYds"])
APyds = list(avg_data["APYd"])
RushAtt = list(avg_data["RushAtt"])
PassAtt = list(avg_data["PassAtt"])
RushYds = list(avg_data["RushYds"])
PassYds = list(avg_data["PassYds"])
PassTDs = list(avg_data["PassTD"])
RushTDs = list(avg_data["RushTD"])
AllTDs = list(avg_data["AllTD"])
ComplPrct = list(avg_data["Cmp%"])
QbRating = list(avg_data["QbRating"])
YdsPerPass = list(avg_data["Y/Apass"])
YdsPerCmp = list(avg_data["Y/C"])
YdsPerRush = list(avg_data["Y/Arun"])
YdsPerPlay = list(avg_data["Y/Play"])
YppYprRatio = list(avg_data["YppYprRatio"])
Pass1D = list(avg_data["1stDpass"])
Run1D = list(avg_data["1stDrun"])
RunPercent = list(avg_data["RunPercent"])
INT = list(avg_data["Int"])
Fmb = list(avg_data["Fmb"]) 
FL = list(avg_data["FL"])
TOV = list(avg_data["TO"])
Sacks = list(avg_data["Sk"])
DefensivePtsScored = list(avg_data["DefensivePtsScored"])
Penalties = list(avg_data["Pen"])
PenaltyYds = list(avg_data["PenYds"])
KrYds = list(avg_data["KrYds"])
PrYds = list(avg_data["PrYds"])
YdsPerKr = list(avg_data["Y/KR"])
YdsPerPr = list(avg_data["Y/PR"])
YdsPerPnt = list(avg_data["Y/Pnt"])
FgPrct = list(avg_data["FG%"])
Fgm50 = list(avg_data["FGM50Plus"])
XpPrct = list(avg_data["XP%"])

volumeStats = [PF, Plays, TotalYds, RushAtt, PassAtt, RushYds, PassYds, RushTDs, PassTDs, Pass1D, Run1D, INT, FL, TOV, Sacks,
               DefensivePtsScored, Penalties, PenaltyYds, KrYds, PrYds, Fgm50, Fmb, APyds, AllTDs]

# '82 and '87 adjust
index82 = 1982-min_year
index87 = 1987-min_year
for dataList in volumeStats:
    dataList[index82] *= 16/9
    dataList[index87] *= 16/15

listsForPercentile = [PF, Plays, TotalYds, APyds, RushAtt, PassAtt, RushYds, PassYds, RushTDs, PassTDs, ComplPrct, QbRating,
                      YdsPerPass,
                      YdsPerCmp, YdsPerRush, YdsPerPlay, YppYprRatio, Pass1D, Run1D, RunPercent, INT, Fmb, FL, TOV, Sacks,
                      DefensivePtsScored, Penalties, PenaltyYds,
                      KrYds, PrYds, YdsPerKr, YdsPerPr, YdsPerPnt, FgPrct, Fgm50, XpPrct]

for dataList in listsForPercentile:
    listCopy = deepcopy(dataList)
    for i in range(len(dataList)):
        dataList[i] = percentileofscore(listCopy, listCopy[i]) / 100.0

displayData_pass = pd.DataFrame({"Pass Attempts": PassAtt, "Pass Yds": PassYds, "Pass TDs": PassTDs,
                                  "Completion %": ComplPrct, "QB Rating": QbRating, "Yds/Pass": YdsPerPass,                     
                                  "Yds / Cmp": YdsPerCmp, "Pass 1D": Pass1D, "INT": INT,
                                  "Sacks": Sacks,}, index=years)
displayData_rush = pd.DataFrame({"Fum Lost": FL,  "Fum": Fmb, "Run 1D": Run1D, "Run %": RunPercent,
                                 "Rush Att": RushAtt, "Rush TDs": RushTDs, "Rush Yds": RushYds,
                                 "Yds / Rush": YdsPerRush}, index=years)
displayData_st = pd.DataFrame({"FG %": FgPrct, "FGM 50+": Fgm50, "KR Yds": KrYds, "PR Yds": PrYds,
                               "XP %": XpPrct, "Yds / KR": YdsPerKr,
                               "Yds/Pnt": YdsPerPnt,
                               "Yds/PR": YdsPerPr}, index=years)
displayData_ovrl = pd.DataFrame({"AP Yds": APyds, "DTD + Safety Pts": DefensivePtsScored, 'Total Pts': PF,
                                 "Penalties": Penalties, "Pen Yds": PenaltyYds, "Plays": Plays,
                                 "Turnovers": TOV, "Offensive Yds": TotalYds,
                                 "Yds / Play": YdsPerPlay, "Pass / Run Efficiency": YppYprRatio
                                 }, index=years)

percentiles = []
for x in displayData_pass.apply(tuple):
  percentiles.extend(x)

dataColumns = list(displayData_pass.columns)
displayColumns = []
for i in range(len(dataColumns)):
    for j in range(len(years)):
        displayColumns.append(dataColumns[i])
  
data_pass=pd.DataFrame(dict(statistics=displayColumns,
                       percentiles=percentiles,
                       years=years*displayData_pass.shape[1]
                       ))


hm_pass = HeatMap(data_pass, x="years", y='statistics', values='percentiles', title='NFL Passing Stat Percentiles By Year', stat=None, palette=palette.Blues9, legend=False)
hm_pass.background_fill_color = "grey"

percentiles = []
for x in displayData_rush.apply(tuple):
  percentiles.extend(x)

dataColumns = list(displayData_rush.columns)
displayColumns = []
for i in range(len(dataColumns)):
    for j in range(len(years)):
        displayColumns.append(dataColumns[i])
        
data_rush=pd.DataFrame(dict(statistics=displayColumns,
                       percentiles=percentiles,
                       years=years*displayData_rush.shape[1]
                       ))

hm_rush = HeatMap(data_rush, x="years", y='statistics', values='percentiles', title='NFL Rushing Stat Percentiles By Year', stat=None, palette=palette.Greens9, legend=False)
hm_rush.background_fill_color = "grey"

percentiles = []
for x in displayData_st.apply(tuple):
  percentiles.extend(x)

dataColumns = list(displayData_st.columns)
displayColumns = []
for i in range(len(dataColumns)):
    for j in range(len(years)):
        displayColumns.append(dataColumns[i])
        
data_st=pd.DataFrame(dict(statistics=displayColumns,
                       percentiles=percentiles,
                       years=years*displayData_st.shape[1]
                       ))

hm_st = HeatMap(data_st, x="years", y='statistics', values='percentiles', title='NFL Special Teams Stat Percentiles By Year', stat=None, palette=palette.Oranges9, legend=False)
hm_st.background_fill_color = "grey"

percentiles = []
for x in displayData_ovrl.apply(tuple):
  percentiles.extend(x)

dataColumns = list(displayData_ovrl.columns)
displayColumns = []
for i in range(len(dataColumns)):
    for j in range(len(years)):
        displayColumns.append(dataColumns[i])

data_ovrl=pd.DataFrame(dict(statistics=displayColumns,
                       percentiles=percentiles,
                       years=years*displayData_ovrl.shape[1]
                       ))

hm_ovrl = HeatMap(data_ovrl, x="years", y='statistics', values='percentiles', title='NFL Overall Percentiles By Year', stat=None, palette=palette.Purples9, legend=False)
hm_ovrl.background_fill_color = "grey"
layout=gridplot([hm_pass, hm_rush], [hm_st, hm_ovrl])
curdoc().add_root(layout)
output_file("test.html")
show(layout)