import pandas as pd

#for each year of offense and defense, compute advanced stats

def addUnrankedStats(first_year, last_year):
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

def addUnrankedDriveStats(first_year, last_year):
    for year in range(first_year, last_year+1):
        fileLocation = "../IntermediateData/Merged/merged_" + str(year) + ".csv" 
        merged_csv = pd.read_csv(fileLocation) 
        merged_csv['TimeOfPossession'] = (merged_csv['AvgDriveTime'] * merged_csv['#Dr'])
        merged_csv['TimeOfPossession_Defense'] = (merged_csv['AvgDriveTime_Defense'] * merged_csv['#Dr_Defense'])
        merged_csv['AvgFieldPositionDifferential'] = (merged_csv['AvgStartingPosition'] - merged_csv['AvgStartingPosition_Defense'])
        merged_csv.to_csv(fileLocation, index=False)


#addUnrankedStats(min_year, max_year)
#addUnrankedDriveStats(1998, max_year)