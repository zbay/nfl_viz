import pandas as pd

highGood = ["PF", "TotalYds", "Ply", "Y/Play", "1stD",
                   "Cmp", "PassAtt", "PassYds", "PassTD",
                   "NY/A", "1stDpass", "RushAtt",
                   "RushYds", "RushTD", "Y/Arun", "1stPy",
                   "Sc%", "1stDpass", "1stDrun",
                   "Cmp%", "PassTD%", "Y/Apass", 
                   "AY/A", "Y/C", "QbRating", "ANY/A",
                   "TO_Defense", "FL_Defense", "Int_Defense",
                   "Sk_Defense", "SkYds_Defense", "Sk%_Defense", 
                   "Int%_Defense",
                   "PuntRet", "PrYds", "PrTD", "Y/PR", "KickRet",
                   "KrYds", "KrTD", "Y/KR", "APYd",
                   "TFGA", "TFGM", "FG%", "XPA", "XPM",
                   "XP%", "Pnt", "PntYds", "Y/Pnt",
                   "TO%_Defense",
                   "RawPassYds", "TO_Differential",
                   "Yds_Differential", "PF_Differential", "DefensivePtsScored"]

highGoodExp = ["ExpectedPoints", "ExpectedPointsPassing",
                   "ExpectedPoints_Defense",
                   "ExpectedPointsPassing_Defense",
                   "ExpectedPointsRunning",
                   "ExpectedPointsRunning_Defense"]
    
highGoodDrive = ["#Dr", "Plays/Drive",
                   "Yds/Drive", "AvgStartingPosition",
                   "AvgDriveTime", "Pts/Drive",
                   "TimeOfPossession", "AvgFieldPositionDifferential"]

#Neither high or low values are necessarily good for these. We'll treat them like "highGood" though
neutralGood = ["PassPercent", "RunPercent", 
                   "PassYdPercent", "RunYdPercent",
                   "PassTdPercent", "RunTdPercent",
                   "Penalty1dPercent", "YppYprRatio",
                   "PassPercent_Defense",                   
                   "RunPercent_Defense", 
                  "PassYdPercent_Defense",
                  "RunYdPercent_Defense",
                  "PassTdPercent_Defense", "RunTdPercent_Defense",
                  "Penalty1dPercent_Defense", "YppYprRatio_Defense",
                  'PassRun1dRatio', 'RunPass1dRatio'] 
                   
lowGood = ["TO", "FL", "Int", "Pen", "PenYds", "TO%",
                  "Sk", "SkYds", "Sk%", "Int%",
                  "PF_Defense", "TotalYds_Defense",
                  "Ply_Defense", "Y/Play_Defense",
                  "1stD_Defense",
                  "Cmp_Defense", "PassAtt_Defense",
                  "PassYds_Defense", "PassTD_Defense",
                  "NY/A_Defense", "1stDpass_Defense",
                  "RushAtt_Defense",
                  "RushYds_Defense", "RushTD_Defense",
                  "Y/Arun_Defense", "1stPy_Defense",
                  "Sc%_Defense", "1stDrun_Defense",
                  "Cmp%_Defense", "PassTD%_Defense",
                  "Y/Apass_Defense",
                  "AY/A_Defense", "Y/C_Defense",
                  "QbRating_Defense", "ANY/A_Defense",
                  "ANY/A_Defense",
                  "Pen_Defense", "PenYds_Defense",
                  "PntRet_Defense", "PrYds_Defense",
                  "PrTD_Defense", "Y/PR_Defense",
                  "KickRet_Defense",
                  "KrYds_Defense", "KrTD_Defense",
                  "Y/KR_Defense", 
                  "TFGA_Defense", "TFGM_Defense", "FG%_Defense",
                  "XPA_Defense", "XPM_Defense", 
                  "XP%_Defense", "Pnt_Defense", "PntYds_Defense",
                  "PntBlck_Defense", "Y/Pnt_Defense",
                  "PntBlck",
                  "FumbleLostPercent"]
    
lowGoodDrive = ["#Dr_Defense",
                  "Plays/Drive_Defense", 
                  "Yds/Drive_Defense", 
                  "AvgStartingPosition_Defense",
                  "Pts/Drive_Defense"]

min_year = 1981

#latest year
max_year = 2016


def rankAllYears(first_year, last_year):
    for year in range(first_year, last_year+1):
        fileLocation = "../IntermediateData/Merged/merged_" + str(year) + ".csv"
        outputLocation = "../ProcessedData/Yearly_Ranked/ranked_" + str(year) + ".csv"
        merged_csv = pd.read_csv(fileLocation)  
        realTeams = merged_csv[(merged_csv["Tm"] != "Avg Team")]
        avgTeam = merged_csv[merged_csv["Tm"] == 'Avg Team']
        for criterion in highGood:
            realTeams[criterion + "_High_Rank"] = realTeams[criterion].rank(ascending=False)
            avgTeam[criterion + "_High_Rank"] = (realTeams.shape[0]+1)/2
        for criterion in lowGood:
            realTeams[criterion + "_Low_Rank"] = realTeams[criterion].rank(ascending=True)  
            avgTeam[criterion + "_Low_Rank"] = (realTeams.shape[0]+1)/2
        for criterion in neutralGood:
            realTeams[criterion + "_High_Rank"] = realTeams[criterion].rank(ascending=False)
            avgTeam[criterion + "_High_Rank"] = (realTeams.shape[0]+1)/2
        if year >= 2000:
            for criterion in highGoodExp:
                realTeams[criterion + "_High_Rank"] = realTeams[criterion].rank(ascending=False)
                avgTeam[criterion + "_High_Rank"] = (realTeams.shape[0]+1)/2
        if year >= 1998:
            for criterion in highGoodDrive:
                realTeams[criterion + "_High_Rank"] = realTeams[criterion].rank(ascending=False)
                avgTeam[criterion + "_High_Rank"] = (realTeams.shape[0]+1)/2
            for criterion in lowGoodDrive:
                realTeams[criterion + "_Low_Rank"] = realTeams[criterion].rank(ascending=True)
                avgTeam[criterion + "_Low_Rank"] = (realTeams.shape[0]+1)/2
        
            
        realTeams = realTeams.append(avgTeam)
        realTeams.to_csv(outputLocation, index=False)

rankAllYears(min_year, max_year)