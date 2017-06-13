import pandas as pd
import os

directories = ["../ProcessedData/Coaches_Offense/", "../ProcessedData/Coaches_Defense/", "../ProcessedData/Coaches_Head/"]
outputs_mean = ["../ProcessedData/Coaches_Summary/Offense_Means.csv", "../ProcessedData/Coaches_Summary/Defense_Means.csv", "../ProcessedData/Coaches_Summary/HC_Means.csv"]
outputs_median = ["../ProcessedData/Coaches_Summary/Offense_Medians.csv", "../ProcessedData/Coaches_Summary/Defense_Medians.csv", "../ProcessedData/Coaches_Summary/HC_Medians.csv"]

o_coach_columns = list(pd.read_csv("../ProcessedData/Coaches_Offense/Kyle Shanahan.csv").columns) + ['Name', 'Experience']
d_coach_columns = list(pd.read_csv("../ProcessedData/Coaches_Defense/Mike Tomlin.csv").columns) + ['Name', 'Experience']
h_coach_columns = list(pd.read_csv("../ProcessedData/Coaches_Head/Sean Payton.csv").columns) + ['Name', 'Experience']

offenseEssentials = ["Name", "Exp", "Tm", "Oscore_Rank", "PF_High_Rank", "TotalYds_High_Rank", "Ply_High_Rank", "1stD_High_Rank",
"Y/Play_High_Rank", "TO_Low_Rank", "TO%_Low_Rank",
"Pen_Low_Rank", "Plays/Drive_High_Rank", "Yds/Drive_High_Rank", "AvgDriveTime_High_Rank", "Pts/Drive_High_Rank", "Sc%_High_Rank",
"PassAtt_High_Rank", "PassYds_High_Rank", "PassTD_High_Rank", "ANY/A_High_Rank", "Sk%_Low_Rank", "Int_Low_Rank", "Int%_Low_Rank",
"1stDpass_High_Rank", "Cmp%_High_Rank", "Y/C_High_Rank", "QbRating_High_Rank",
"RushAtt_High_Rank", "RushYds_High_Rank", "RushTD_High_Rank", "Y/Arun_High_Rank", "1stDrun_High_Rank", "FL_Low_Rank"]

defenseEssentials = ["Name", "Exp", "Tm", "Dscore_Rank", "PF_Defense_Low_Rank", "TotalYds_Defense_Low_Rank",
"Ply_Defense_Low_Rank", "1stD_Defense_Low_Rank", "Y/Play_Defense_Low_Rank",
"TO_Defense_High_Rank", "TO%_Defense_High_Rank", "Pen_Defense_Low_Rank",
"Plays/Drive_Defense_Low_Rank", "Yds/Drive_Defense_Low_Rank", "AvgDriveTime_Defense_Low_Rank", "Pts/Drive_Defense_Low_Rank",
"Sc%_Defense_Low_Rank",
"PassAtt_Defense_Low_Rank", "PassYds_Defense_Low_Rank",
"PassTD_Defense_Low_Rank", "ANY/A_Defense_Low_Rank", "Sk_Defense_High_Rank", "Sk%_Defense_High_Rank", 
"Int_Defense_High_Rank", "Int%_Defense_High_Rank",
"1stDpass_Defense_Low_Rank", "Cmp%_Defense_Low_Rank", "Y/C_Defense_Low_Rank", "QbRating_Defense_Low_Rank",
"RushAtt_Defense_Low_Rank", "RushYds_Defense_Low_Rank", "RushTD_Defense_Low_Rank", "Y/Arun_Defense_Low_Rank", 
"1stDrun_Defense_Low_Rank", "FL_Defense_High_Rank", "DefensivePtsScored_High_Rank"]

hcEssentials = ["Name", "Exp", "Tm",
                "Oscore_Rank", "Dscore_Rank", "STscore_Rank", "ThreePhaseScore_Rank",
                "PF_Differential_High_Rank", "Yds_Differential_High_Rank", "TO_Differential_High_Rank",
               "AvgStartingPosition_High_Rank",  "AvgStartingPosition_Defense_Low_Rank", "TimeOfPossession_High_Rank",
               "GameControlScore_Rank", "GameControlPlusBalance_Rank"]

currentCoaches = pd.read_csv("../RawData/CurrentCoaches.csv")

mean_dfs = [pd.DataFrame(columns=o_coach_columns), pd.DataFrame(columns=d_coach_columns), pd.DataFrame(columns=h_coach_columns)]
median_dfs = [pd.DataFrame(columns=o_coach_columns), pd.DataFrame(columns=d_coach_columns), pd.DataFrame(columns=h_coach_columns)]

def averageSeasonReports():
    for i in range(len(directories)):
        for filename in os.listdir(directories[i]):
            if filename.endswith(".csv"):
                end_name = filename.index(".csv")
                name = filename[0:end_name]
                coach = pd.read_csv(directories[i] + filename)
                coach_team = currentCoaches.loc[(currentCoaches["HC"] == name) | (currentCoaches["OC"] == name) | (currentCoaches["DC"] == name) | (currentCoaches["OC2"] == name), "Team"].iloc[0]
                median_row = coach.loc[coach['Year'] == 'Median year']
                mean_row = coach.loc[coach['Year'] == 'Mean year']
                median_row["Name"] = name
                mean_row["Name"] = name
                mean_row["Tm"] = coach_team
                median_row["Tm"] = coach_team
                mean_row["Exp"] = coach.shape[0]-2
                median_row["Exp"] = coach.shape[0]-2
                mean_dfs[i] = mean_dfs[i].append(mean_row)
                median_dfs[i] = median_dfs[i].append(median_row)
                del mean_dfs[i]["Year"]
                del median_dfs[i]["Year"]
        mean_dfs[i].to_csv(outputs_mean[i], index=False)
        median_dfs[i].to_csv(outputs_median[i], index=False)

def reorderColumns(phase):
    if phase == "HC":
        mean_cols = mean_dfs[2].columns.values.tolist()
        median_cols = median_dfs[2].columns.values.tolist()
        for col in hcEssentials:
            print(col)
            mean_cols.remove(col)
            median_cols.remove(col)
        mean_cols = hcEssentials + mean_cols
        median_cols = hcEssentials + median_cols
        mean_dfs[2].to_csv(outputs_mean[2], columns = mean_cols, index=False)
        median_dfs[2].to_csv(outputs_median[2], columns=median_cols, index=False)
    if phase == "OC":
        mean_cols = mean_dfs[0].columns.values.tolist()
        median_cols = median_dfs[0].columns.values.tolist()
        for col in offenseEssentials:
            print(col)
            mean_cols.remove(col)
            median_cols.remove(col)
        mean_cols = offenseEssentials + mean_cols
        median_cols = offenseEssentials + median_cols
        mean_dfs[0].to_csv(outputs_mean[0], columns = mean_cols, index=False)
        median_dfs[0].to_csv(outputs_median[0], columns=median_cols, index=False)
    if phase == "DC":
        mean_cols = mean_dfs[1].columns.values.tolist()
        median_cols = median_dfs[1].columns.values.tolist()
        for col in defenseEssentials:
            print(col)
            mean_cols.remove(col)
            median_cols.remove(col)
        mean_cols = defenseEssentials + mean_cols
        median_cols = defenseEssentials + median_cols
        mean_dfs[1].to_csv(outputs_mean[1], columns = mean_cols, index=False)
        median_dfs[1].to_csv(outputs_median[1], columns=median_cols, index=False)
    