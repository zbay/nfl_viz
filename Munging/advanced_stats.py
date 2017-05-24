import pandas as pd

#for each year of offense and defense, compute advanced stats

#earliest years we are using data from
min_year = 1981

#latest year
max_year = 2016


def addedUnrankedStats(first_year, last_year):
    for year in range(first_year, last_year+1):
        fileLocation = "../IntermediateData/Merged/merged_" + str(year) + ".csv" 
        merged_csv = pd.read_csv(fileLocation)  
        merged_csv["RawPassYds"] = (merged_csv["PassYds"] + merged_csv["SkYds"])
        merged_csv["TO_Differential"] = (merged_csv["TO_Defense"] - merged_csv["TO"])
        merged_csv["PF_Differential"] = (merged_csv["PF"] - merged_csv["PF_Defense"])
        merged_csv["Yds_Differential"] = (merged_csv["TotalYds"] - merged_csv["TotalYds_Defense"])
        merged_csv['PassPercent'] = ((merged_csv['PassAtt'] + merged_csv['Sk']) / merged_csv['Ply'])
        merged_csv['RunPercent'] = (1.0 - merged_csv['PassPercent'])
        merged_csv['PassYdPercent'] = (merged_csv['PassYds'] / (merged_csv['TotalYds']))
        merged_csv['RunYdPercent'] = 1.0 - merged_csv['PassYdPercent']
        merged_csv['PassTdPercent'] = (merged_csv['PassTD'] / (merged_csv['PassTD'] + merged_csv['RushTD']))
        merged_csv['RunTdPercent'] = 1.0 - merged_csv['PassTdPercent']
        merged_csv['PassRun1dRatio'] = merged_csv['1stDpass'] / merged_csv["1stDrun"]
        merged_csv['RunPass1dRatio'] = merged_csv['1stDrun'] / merged_csv["1stDpass"]
        merged_csv['Penalty1dPercent'] = merged_csv['1stPy'] / merged_csv['1stD']
        merged_csv['YppYprRatio'] = merged_csv['Y/Apass'] / merged_csv['Y/Arun']
        merged_csv['PassPercent_Defense'] = (merged_csv['PassAtt_Defense'] + merged_csv['Sk_Defense']) / merged_csv['Ply_Defense']
        merged_csv['RunPercent_Defense'] = 1.0 - merged_csv['PassPercent_Defense']
        merged_csv['PassYdPercent_Defense'] = (merged_csv['PassYds_Defense'] / (merged_csv['TotalYds_Defense']))
        merged_csv['RunYdPercent_Defense'] = 1.0 - merged_csv['PassYdPercent_Defense']
        merged_csv['PassTdPercent_Defense'] = (merged_csv['PassTD_Defense'] / (merged_csv['PassTD_Defense'] + merged_csv['RushTD_Defense']))
        merged_csv['RunTdPercent_Defense'] = 1.0 - merged_csv['PassTdPercent_Defense']
        merged_csv['Penalty1dPercent_Defense'] = merged_csv['1stPy_Defense'] / merged_csv['1stD_Defense']
        merged_csv['YppYprRatio_Defense'] = merged_csv['Y/Apass_Defense'] / merged_csv['Y/Arun_Defense']
        merged_csv['FumbleLostPercent'] = merged_csv['FL'] / merged_csv['Fmb']
        merged_csv["DefensivePtsScored"] = 6*merged_csv["FmbTD"] + 6*merged_csv["IntTD"] + 6*merged_csv["OthTD"] + 2*merged_csv["Sfty"]
        merged_csv.to_csv(fileLocation, index=False)

def addedUnrankedDriveStats(first_year, last_year):
    for year in range(first_year, last_year+1):
        fileLocation = "../IntermediateData/Merged/merged_" + str(year) + ".csv" 
        merged_csv = pd.read_csv(fileLocation) 
        merged_csv['TimeOfPossession'] = (merged_csv['AvgDriveTime'] * merged_csv['#Dr'])
        merged_csv['TimeOfPossession_Defense'] = (merged_csv['AvgDriveTime_Defense'] * merged_csv['#Dr_Defense'])
        merged_csv['AvgFieldPositionDifferential'] = (merged_csv['AvgStartingPosition'] - merged_csv['AvgStartingPosition_Defense'])
        merged_csv.to_csv(fileLocation, index=False)
#for each team, for each year, compute adv stats and add them to the dataframe and save back to csv
#Oscore = (PFRank + YdsRank + 1stDRank + TORank + Y/ArunRank + NY/ARank) / 6
#Dscore = (PF_DefenseRank + Yds_DefenseRank + 1stD_DefenseRank + TO_DefenseRank + Y/Arun_DefenseRank + NY/A_DefenseRank) / 6
#STscore = (Y/PRRank + Y/KRRank + Y/PntRank + FG%Rank + Y/PR_DefenseRank + Y/KR_DefenseRank + Y/Pnt_DefenseRank + FG%_DefenseRank) / 8
#ThreePhaseScore - (Oscore + Dscore + STscore) / 3
#FantasyPassScore = (PassCmpRank + PassYdsRank + PassTDRank + PassIntRank + Pass1DRank + Y/ApassRank) / 6
#FantasyRushScore = (RushAttRank + RushYdsRank + RushTDRank + Rush1DRank + FLRank) / 5
#FantasyOffenseScore = (FantasyPassScore + FantasyRushScore) / 2
#FantasyDstScore = (((PrYdsRank + KrYdsRank) / 2) + PF_DefenseRank + Yds_DefenseRank + Sk_DefenseRank + TO_DefenseRank + DefensivePtsScored_Rank) / 6
#GameControlScore = (TimeOfPossession_High_Rank + AvgFieldPositionDifferential_High_Rank + YdsDifferential_High_Rank + PF_Differential_High_Rank + TO_Differential_Low_Rank) / 5.0

teams = ["WAS", "NYG", "PHI", "DAL", "ATL", "CAR", "NO", "TB", "GB", "DET", "MIN", "CHI", "SF", "ARI", "LAR", "SEA",
         "BAL", "CLE", "CIN", "PIT", "IND", "JAX", "HOU", "TEN", "NE", "MIA", "NYJ", "BUF", "LAC", "DEN", "KC", "OAK"]

def rankFusionStats(first_year, last_year):
    for year in range(first_year, last_year+1):
        fileLocation = "../YearlyRanked/ranked_" + str(year) + ".csv"
        year_csv = pd.read_csv(fileLocation)
        year_csv["Oscore"] = ((year_csv["PF_High_Rank"]) + (year_csv["TotalYds_High_Rank"]) + (year_csv["1stD_High_Rank"])
            + (year_csv["TO_Low_Rank"])
            + (year_csv["Y/Arun_High_Rank"]) + (year_csv["NY/A_High_Rank"])) / 6.0
        year_csv["Dscore"] = ((year_csv["PF_Defense_Low_Rank"]) + (year_csv["TotalYds_Defense_Low_Rank"]) + 
            (year_csv["1stD_Defense_Low_Rank"])
            + (year_csv["TO_Defense_High_Rank"]) +
            (year_csv["Y/Arun_Defense_Low_Rank"]) + (year_csv["NY/A_Defense_Low_Rank"])) / 6.0
        year_csv["STscore"] = (((year_csv["Y/PR_High_Rank"]) + (year_csv["Y/KR_High_Rank"]) 
            + (year_csv["Y/Pnt_High_Rank"]) + (year_csv["FG%_High_Rank"]) +
            (year_csv["Y/PR_Defense_Low_Rank"]) + (year_csv["Y/KR_Defense_Low_Rank"]) + 
            (year_csv["Y/Pnt_Defense_Low_Rank"]) + (0.5 * (year_csv["FG%_Defense_Low_Rank"])))) / 7.5
        year_csv["ThreePhaseScore"] = (((year_csv["Oscore"]) + (year_csv["Dscore"]) + (0.75* (year_csv["STscore"])))) / 2.75
        year_csv["FantasyPassScore"] = ((year_csv["Cmp_High_Rank"]) + (year_csv["PassYds_High_Rank"]) +
            (year_csv["PassTD_High_Rank"]) + (year_csv["Int%_Low_Rank"])
            + (year_csv["1stDpass_High_Rank"]) + (year_csv["Y/Apass_High_Rank"]) + year_csv["Int_Low_Rank"]) / 8.0
        year_csv["FantasyRushScore"] = ((year_csv["RushAtt_High_Rank"]) + (year_csv["RushYds_High_Rank"]) +
            (year_csv["Y/Arun_High_Rank"]) +
            (year_csv["RushTD_High_Rank"]) + (year_csv["1stDrun_High_Rank"]) + (year_csv["FL_Low_Rank"])) / 6.0
        year_csv["FantasyOffenseScore"] = ((year_csv["FantasyPassScore"]) + (year_csv["FantasyRushScore"])) / 2.0
        year_csv["FantasyDstScore"] = ((((year_csv["PrYds_High_Rank"]) + (year_csv["KrYds_High_Rank"])) / 2) +
            (year_csv["PF_Defense_Low_Rank"]) + (year_csv["TotalYds_Defense_Low_Rank"]) + (year_csv["Sk_Defense_High_Rank"])
            + (year_csv["TO_Defense_High_Rank"]) + (year_csv['DefensivePtsScored_High_Rank'])) / 6.0
        if year >= 1998:
            year_csv["GameControlScore"] = ( (year_csv["TimeOfPossession_High_Rank"]) + (year_csv["AvgFieldPositionDifferential_High_Rank"])
                + (year_csv["Yds_Differential_High_Rank"]) + (year_csv["PF_Differential_High_Rank"]) +  (year_csv["TO_Differential_High_Rank"]) ) / 5.0
            year_csv["GameControlPlusVersatility"] = ((year_csv["GameControlScore"] + year_csv["ThreePhaseScore"]) / 2.0)
        year_csv.to_csv(fileLocation, index=False)

addedUnrankedStats(min_year, max_year)
addedUnrankedDriveStats(1998, max_year)