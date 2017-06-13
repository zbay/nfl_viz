from preprocess import preprocess
from merge_tables import merge_all
from advanced_stats import addUnrankedStats, addUnrankedDriveStats
from rankify import rankAllYears
from rank_fusion_stats import rankFusionStats
from teamify import teamify
from coachify import coachifyAll
from coach_averages import averageSeasonReports, reorderColumns
#from coach_averages import 
# pipeline: preprocess, merge_tables, advanced_stats, rankify, rank_fusion_stats, teamify, coachify, average coach data
min_year = 1981
min_year_drive = 1998
max_year = 2016

'''
preprocess(min_year, max_year)
merge_all(min_year, max_year)
addUnrankedStats(min_year, max_year)
addUnrankedDriveStats(min_year_drive, max_year)
rankAllYears(min_year, max_year)
rankFusionStats(min_year, max_year)
teamify(min_year, max_year)
coachifyAll()
'''
averageSeasonReports()
reorderColumns("HC")
reorderColumns("OC")
reorderColumns("DC")