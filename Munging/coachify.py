#todo:
# compute means and medians in each report, and then make a way to compile those ranks

import pandas as pd

currentCoaches = pd.read_csv("../RawData/CurrentCoaches.csv")
coachHistory = pd.read_csv("../RawData/CoachHistories.csv")

latestYear = 2016

offensiveColumns = ["Year", "Tm", "PF", "TotalYds", "Ply", "Y/Play",
    "TO", "#Dr", "Plays/Drive", "Yds/Drive", "AvgStartingPosition",
    "AvgDriveTime", "Pts/Drive", "TimeOfPossession",
    "Fmb", "FL", "FumbleLostPercent",
    "1stD", "Cmp", "PassAtt", "PassYds", "PassTD",
    "Int", "NY/A", "1stDpass", "RushAtt", "RushYds", "RushTD", "Y/Arun",
    "1stDrun", "Pen", "PenYds", "1stPy", "Sc%", "TO%", "ExpectedPoints",
    "Cmp%", "PassTD%", "Int%", "Y/Apass", "AY/A", "Y/C", "QbRating", "Sk",
    "SkYds", "ANY/A", "Sk%", "ExpectedPointsPassing", "ExpectedPointsRunning",
    "TFGA", "TFGM",
    "FGA50Plus", "FGM50Plus", "FG%", "XP%", "2PA", "2PM", "Sfty",
    "TO_Differential", "PF_Differential", "Yds_Differential",
    "PassPercent", "RunPercent", "PassYdPercent", "RunYdPercent",
    "PassTdPercent", "RunTdPercent", "PassTdPercent" "RunYdPercent",
    "PassRun1dRatio", "RunPass1dRatio", "Penalty1dPercent", 
    "YppYprRatio", 
    "PF_High_Rank", "TotalYds_High_Rank", "Ply_High_Rank", "Y/Play_High_Rank",
    "TO_Low_Rank", "#Dr", "Plays/Drive", "Yds/Drive", "AvgStartingPosition",
    "AvgDriveTime", "Pts/Drive", "TimeOfPossession",
    "Fmb", "FL", "FumbleLostPercent",
    "1stD_High_Rank", "Cmp_High_Rank", "PassAtt_High_Rank", "PassYds_High_Rank", "PassTD_High_Rank",
    "Int_Low_Rank", "NY/A_High_Rank", "1stDpass_High_Rank", "RushAtt_High_Rank", "RushYds_High_Rank", "RushTD_High_Rank", "Y/Arun_High_Rank",
    "1stDrun_High_Rank", "Pen_Low_Rank", "PenYds_Low_Rank", "1stPy_High_Rank", "Sc%_High_Rank", "TO%_Low_Rank", "ExpectedPoints_High_Rank",
    "Cmp%_High_Rank", "PassTD%_High_Rank", "Int%_Low_Rank", "Y/Apass_High_Rank", "AY/A_High_Rank", "Y/C_High_Rank", "QbRating_High_Rank", "Sk_Low_Rank",
    "SkYds_Low_Rank", "ANY/A_High_Rank", "Sk%_Low_Rank", "ExpectedPointsPassing_High_Rank", "ExpectedPointsRushing_High_Rank",
    "TFGA_High_Rank", "TFGM_High_Rank", "FG%_High_Rank", "XP%_High_Rank",
    "TO_Differential_High_Rank", "PF_Differential_High_Rank", "Yds_Differential_High_Rank",
    "PassPercent_High_Rank", "RunPercent_High_Rank", "PassYdPercent_High_Rank", "RunYdPercent_High_Rank",
    "PassTdPercent_High_Rank", "RunTdPercent_High_Rank", "PassTdPercent_High_Rank", "RunYdPercent_High_Rank",
    "PassRun1dRatio_High_Rank", "RunPass1dRatio_High_Rank", "Penalty1dPercent_High_Rank", 
    "YppYprRatio_High_Rank", "Oscore", "FantasyPassScore", "FantasyRushScore",
    "FantasyOffenseScore", "GameControlScore", "GameControlPlusBalance", "Oscore_Rank", "FantasyPassScore_Rank",
    "FantasyRushScore_Rank", "FantasyOffenseScore_Rank", "GameControlScore_Rank", "GameControlPlusBalance_Rank"]
    
defensiveColumns = ["Year", "Tm", "PF_Defense", "TotalYds_Defense", "Ply_Defense", "Y/Play_Defense",
    "TO_Defense", "#Dr_Defense", "Plays/Drive_Defense", "Yds/Drive_Defense", "AvgStartingPosition_Defense",
    "AvgDriveTime_Defense", "Pts/Drive_Defense", "TimeOfPossession_Defense",
    "FL_Defense",
    "1stD_Defense", "Cmp_Defense", "PassAtt_Defense", "PassYds_Defense", "PassTD_Defense",
    "Int_Defense", "NY/A_Defense", "1stDpass_Defense", "RushAtt_Defense", "RushYds_Defense", "RushTD_Defense", "Y/Arun_Defense",
    "1stDrun_Defense", "Pen_Defense", "PenYds_Defense", "1stPy_Defense", "Sc%_Defense", "TO%_Defense", "ExpectedPoints_Defense",
    "Cmp%_Defense", "PassTD%_Defense", "Int%_Defense", "Y/Apass_Defense", "AY/A_Defense", "Y/C_Defense", "QbRating_Defense", "Sk_Defense",
    "SkYds_Defense", "ANY/A_Defense", "Sk%_Defense", "ExpectedPointsPassing_Defense", "ExpectedPointsRunning_Defense",
    "TFGA_Defense", "TFGM_Defense",
    "FG%_Defense", "XP%_Defense", "2PA_Defense", "2PM_Defense", "Sfty_Defense",
    "TO_Differential", "PF_Differential", "Yds_Differential",
    "PassPercent_Defense", "RunPercent_Defense", "PassYdPercent_Defense", "RunYdPercent_Defense",
    "PassTdPercent_Defense", "RunTdPercent_Defense", "PassTdPercent_Defense", "RunYdPercent_Defense",
    "Penalty1dPercent_Defense", 
    "YppYprRatio_Defense", 
    "PF_Defense_Low_Rank", "TotalYds_Defense_Low_Rank", "Ply_Defense_Low_Rank", "Y/Play_Defense_Low_Rank",
    "TO_Defense_High_Rank", "#Dr_Defense", "Plays/Drive_Defense", "Yds/Drive_Defense", "AvgStartingPosition_Defense",
    "AvgDriveTime_Defense", "Pts/Drive_Defense", "TimeOfPossession_Defense",
    "FL_Defense",
    "1stD_Defense_Low_Rank", "Cmp_Defense_Low_Rank", "PassAtt_Defense_Low_Rank", "PassYds_Defense_Low_Rank",
    "PassTD_Defense_Low_Rank",
    "Int_Defense_High_Rank", "NY/A_Defense_Low_Rank", "1stDpass_Defense_Low_Rank", "RushAtt_Defense_Low_Rank", "RushYds_Defense_Low_Rank", "RushTD_Defense_Low_Rank", "Y/Arun_Defense_Low_Rank",
    "1stDrun_Defense_Low_Rank", "Pen_Defense_Low_Rank", "PenYds_Defense_Low_Rank", "1stPy_Defense_Low_Rank", "Sc%_Defense_Low_Rank", "TO%_Defense_High_Rank", "ExpectedPoints_Defense_High_Rank",
    "Cmp%_High_Rank", "PassTD%_High_Rank", "Int%_Low_Rank", "Y/Apass_High_Rank", "AY/A_High_Rank", "Y/C_High_Rank", "QbRating_High_Rank", "Sk_Defense_High_Rank",
    "SkYds_Defense_High_Rank", "ANY/A_Defense_Low_Rank", "Sk%_Defense_High_Rank", "ExpectedPointsPassing_Defense_High_Rank", "ExpectedPointsRunning_Defense_High_Rank",
    "TFGA_Defense_Low_Rank", "TFGM_Defense_Low_Rank", "FG%_Defense_Low_Rank", "XP%_Defense_Low_Rank",
    "TO_Differential_High_Rank", "PF_Differential_High_Rank", "Yds_Differential_High_Rank",
    "PassPercent_Defense_High_Rank", "RunPercent_Defense_High_Rank", "PassYdPercent_Defense_High_Rank", "RunYdPercent_Defense_High_Rank",
    "PassTdPercent_Defense_High_Rank", "RunTdPercent_Defense_High_Rank", "PassTdPercent_Defense_High_Rank", "RunYdPercent_Defense_High_Rank",
    "Penalty1dPercent_Defense_High_Rank", 
    "YppYprRatio_Defense_High_Rank", "Dscore","FantasyDstScore", "GameControlScore", "GameControlPlusBalance", "Dscore_Rank",
    "FantasyDstScore_Rank", "GameControlScore_Rank", "GameControlPlusBalance_Rank"]

# for each coach with a given job, get all their team's data from that year
def coachifyData(job):
    yearlyStart = "../ProcessedData/Teamified/WAS.csv" #get an arbitrary team's columns
    yearly_csv = pd.read_csv(yearlyStart)
    yearly_columns = yearly_csv.columns
    for coach in currentCoaches[job]:
        if coach != "Vacant":
            coach_csv = pd.DataFrame(columns=yearly_columns)
            relevantTenures = coachHistory[(coachHistory["Coach"] == coach)]
            for i, tenure in relevantTenures.iterrows():
                team = tenure.Team
                team_csv = pd.read_csv("../ProcessedData/Teamified/" + team + ".csv")
                firstYear = tenure.StartYr
                lastYear = latestYear
                if tenure.EndYr > 1950:
                    lastYear = int(tenure.EndYr)
                if firstYear <= lastYear:
                    for year in range(firstYear, lastYear+1):
                        year_row = team_csv[team_csv["Year"] == year]
                        year_row['Tm'] = tenure.Team
                        year_row['Job'] = tenure.Job
                        coach_csv = coach_csv.append(year_row)
                    cols = coach_csv.columns.values.tolist()
                    cols.remove("Year")
                    cols = ["Year"] + cols     
                    coach_csv = coach_csv[cols]
                    coach_csv.to_csv("../ProcessedData/Coaches_Full/" + coach + ".csv", index=False)

# Generate Offensive, Defensive, and Head Coach reports for each coach
def coachifyReports(job):
    #Coach history is: the file for the current coach
    for coach in currentCoaches[job]:
        try:
            currentCoach = pd.read_csv("../ProcessedData/Coaches_Full/" + coach + ".csv")
            if coach != "Vacant":
                if job == "HC":
                    offensiveReports(coach, currentCoach[currentCoach["Job"] != "DC"])
                    defensiveReports(coach, currentCoach[currentCoach["Job"] != "OC"])
                    hcReports(coach, currentCoach[currentCoach["Job"] == "HC"])
                elif job == "OC" or job == "OC2":
                    offensiveReports(coach, currentCoach[currentCoach["Job"] != "DC"])
                elif job == "DC": 
                    defensiveReports(coach, currentCoach[currentCoach["Job"] != "OC"])
        except (OSError) :
            do = "nothing"
                
def offensiveReports(coach, tenures):
    outputLoc = "../ProcessedData/Coaches_Offense/" + coach + ".csv"
    meanRow = tenures.mean()
    medianRow = tenures.median()
    meanRow['Year'] = "Mean year"
    medianRow['Year'] = "Median year"
    tenures = tenures.append(meanRow, ignore_index=True).append(medianRow, ignore_index=True)
    tenures.to_csv(outputLoc, columns=offensiveColumns, index=False)
        
def defensiveReports(coach, tenures):
    outputLoc = "../ProcessedData/Coaches_Defense/" + coach + ".csv"
    meanRow = tenures.mean()
    medianRow = tenures.median()
    meanRow['Year'] = "Mean year"
    medianRow['Year'] = "Median year"
    tenures = tenures.append(meanRow, ignore_index=True).append(medianRow, ignore_index=True)
    tenures.to_csv(outputLoc, columns=defensiveColumns, index=False)

def hcReports(coach, tenures):
    outputLoc = "../ProcessedData/Coaches_Head/" + coach + ".csv"
    meanRow = tenures.mean()
    medianRow = tenures.median()
    meanRow['Year'] = "Mean year"
    medianRow['Year'] = "Median year"
    tenures = tenures.append(meanRow, ignore_index=True).append(medianRow, ignore_index=True)
    tenures.to_csv(outputLoc, index=False)
    

def coachifyAll():
    coachifyData("HC")
    coachifyData("OC")
    coachifyData("DC")
    coachifyData("OC2")
    
    coachifyReports("HC")
    coachifyReports("OC")
    coachifyReports("DC")
    coachifyReports("OC2")
    
    

coachifyAll()