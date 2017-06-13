import pandas as pd

#merge, rankify, coachify, then advanced stats
min_year = 1981

#latest year
max_year = 2016

def merge_all(first_year, last_year):
    
    renamer = {"Pts": "Pts/Drive", "Pts_Defense": "Pts/Drive_Defense"}
    
    startFile = "../IntermediateData/Offense/offense_"
    fileLocations = ["../IntermediateData/Pass_Offense/pass_offense_", "../IntermediateData/Returns/returns_",
                     "../IntermediateData/Kicking_Punting/kicking_punting_", "../IntermediateData/Defense/defense_", "../IntermediateData/Pass_Defense/pass_defense_",
                     "../IntermediateData/Returns_Against/returns_against_", "../IntermediateData/Kicking_Punting_Against/kicking_punting_against_",
                     "../IntermediateData/Rush_Offense/rush_offense_", "../IntermediateData/Rush_Defense/rush_defense_", 
                     "../IntermediateData/Drives/drives_", "../IntermediateData/Drives_Against/drives_against_",
                     "../IntermediateData/Scoring_Offense/scoring_offense_", "../IntermediateData/Scoring_Defense/scoring_defense_"]
    for year in range(first_year, last_year+1):
        mainFile = startFile + str(year) + ".csv"
        start_csv = pd.read_csv(mainFile)
        for file in fileLocations:
            if year >= 1998 or (file != "../IntermediateData/Drives/drives_" and file != "../IntermediateData/Drives_Against/drives_against_"):
                otherFile = file + str(year) + ".csv"
                merge_csv = pd.read_csv(otherFile)
                start_csv = start_csv.merge(merge_csv, how="inner", on="Tm")
        start_csv = start_csv.rename(columns=renamer)
        start_csv = start_csv.to_csv("../IntermediateData/Merged/merged_" + str(year) + ".csv", index=False)
        
#merge_all(min_year, max_year)