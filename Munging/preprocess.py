import pandas as pd

# earliest year for which a relevant coach has data
min_year = 1981
# latest completed season
max_year = 2016

# indicate the columns to rename and delete from the raw tables
rename_offense = {"Yds": "TotalYds", "Y/P": "Y/Play", 
    "Att": "PassAtt", "Yds.1": "PassYds", "TD": "PassTD",
    "1stD.1": "1stDpass", "Att.1": "RushAtt", 
    "Yds.2": "RushYds", "TD.1": "RushTD", "Y/A": "Y/Arun",
    "1stD.2": "1stDrun", "Yds.3": "PenYds", 
    "EXP": "ExpectedPoints"}

delete_offense = ["Rk", "G"]

rename_pass_offense = {"TD%": "PassTD%",
    "Y/A": "Y/Apass", "Rate": "QbRating", 
    "Yds.1": "SkYds", "EXP": "ExpectedPointsPassing"}

delete_pass_offense = ["Rk", "G", "Cmp", "Att", "Yds",
    "TD", "Int", "Lng", "Y/G", "NY/A", "4QC", "GWD"]
    
rename_defense = rename_offense
    
delete_defense = delete_offense

rename_pass_defense = rename_pass_offense

delete_pass_defense = ["Rk", "G", "Cmp", "Att", "Yds",
    "TD", "Int", "Y/G", "NY/A"]

rename_returns = {"Ret": "PuntRet", "Yds": "PrYds",
    "TD": "PrTD", "Y/R": "Y/PR",
    "Rt": "KickRet", "Yds.1": "KrYds",
    "TD.1": "KrTD", "Y/Rt": "Y/KR"}
    
delete_returns = ["Rk", "G", "Lng", "Lng.1"]

rename_returns_against = {"Ret": "PntRet", "Yds": "PrYds",
    "TD": "PrTD", "Y/R": "Y/PR",
    "Rt": "KickRet", "Yds.1": "KrYds",
    "TD.1": "KrTD", "Y/Rt": "Y/KR"}
delete_returns_against = delete_offense

rename_kicking = {"FGA": "FGA019",
    "FGM": "FGM019", "FGA.1": "FGA2029",
    "FGM.1": "FGM2029", "FGA.2": "FGA3039",
    "FGM.2": "FGM3039", "FGA.3": "FGA4049",
    "FGM.3": "FGM4049", "FGA.4": "FGA50Plus",
    "FGM.4": "FGM50Plus", "FGA.5": "TFGA",
    "FGM.5": "TFGM", "Yds": "PntYds", "Y/P": "Y/Pnt", "Blck": "PntBlck"}

delete_kicking = ["G", "Rk", "Lng"]

rename_kicking_against = {"Yds": "PntYds", "FGA": "TFGA",
    "FGM": "TFGM", "Y/P": "Y/Pnt", "Blck": "PntBlck"}
delete_kicking_against = delete_offense

rename_rush_offense = {"EXP": "ExpectedPointsRunning"}

delete_rush_offense = ["G", "Rk", "Att", "Yds",
    "TD", "Lng", "Y/A", "Y/G"]

rename_rush_defense = rename_rush_offense

delete_rush_defense = ["G", "Rk", "Att", "Yds",
    "TD", "Y/A", "Y/G"]

rename_drives_offense = {"Plays.1": "Plays/Drive",
    "Yds": "Yds/Drive", "Start": "AvgStartingPosition",
    "Time": "AvgDriveTime", "Pts": "Pts/Drive"}

delete_drives_offense = ["Rk", "G", "Plays", "Sc%", "TO%"]

rename_drives_defense = rename_drives_offense

delete_drives_defense = delete_drives_offense

rename_scoring_offense = {"FblTD": "FmbTD"}

delete_scoring_offense = ["Rk", "G", "RshTD",
   "RecTD", "PR TD", "KR TD", "XPM", "XPA",
   "FGM", "FGA", "Pts", "Pts/G"]

rename_scoring_defense = rename_scoring_offense

delete_scoring_defense = ["Rk", "G", "RshTD",
   "RecTD", "PR TD", "KR TD", "XPM", "XPA",
   "FGM", "FGA", "Pts", "Pts/G", "AllTD"]

# rename columns
def renamify(first_year, last_year, phase):
    renamer = rename_offense
    if phase == "Pass_Offense":
        renamer = rename_pass_offense
    elif phase == "Defense":
        renamer = rename_defense
    elif phase == "Pass_Defense":
        renamer = rename_pass_defense
    elif phase == "Returns":
        renamer = rename_returns
    elif phase == "Returns_Against":
        renamer = rename_returns_against
    elif phase == "Kicking_Punting":
        renamer = rename_kicking
    elif phase == "Kicking_Punting_Against":
        renamer = rename_kicking_against
    elif phase == "Rush_Offense":
        renamer = rename_rush_offense
    elif phase == "Rush_Defense":
        renamer = rename_rush_defense
    elif phase == "Drives":
        renamer = rename_drives_offense
    elif phase == "Drives_Against":
        renamer = rename_drives_defense
    elif phase == "Scoring_Offense":
        renamer = rename_scoring_offense
    elif phase == "Scoring_Defense":
        renamer = rename_scoring_defense
        
    for year in range(first_year, last_year+1):
        inputFile = "../IntermediateData/" + phase + "/" + phase.lower() + "_" + str(year) + ".csv"
        data_csv = pd.read_csv(inputFile)  
        output_file = "../IntermediateData/" + phase + "/" + phase.lower() + "_" + str(year) + ".csv"
        data_csv = data_csv.rename(columns=renamer)
        data_csv.to_csv(output_file, index=False)       

# delete unwanted or redundant columns
def deleteCols(first_year, last_year, phase):
    deleter = delete_offense
    if phase == "Pass_Offense":
        deleter = delete_pass_offense
    elif phase == "Defense":
        deleter = delete_defense
    elif phase == "Pass_Defense":
        deleter = delete_pass_defense
    elif phase == "Returns":
        deleter = delete_returns
    elif phase == "Returns_Against":
        deleter = delete_returns_against
    elif phase == "Kicking_Punting":
        deleter = delete_kicking
    elif phase == "Kicking_Punting_Against":
        deleter = delete_kicking_against
    elif phase == "Rush_Offense":
        deleter = delete_rush_offense
    elif phase == "Rush_Defense":
        deleter = delete_rush_defense
    elif phase == "Drives":
        deleter = delete_drives_offense
    elif phase == "Drives_Against":
        deleter = delete_drives_defense
    elif phase == "Scoring_Offense":
        deleter = delete_scoring_offense
    elif phase == "Scoring_Defense":
        deleter = delete_scoring_defense
    for year in range(first_year, last_year+1):
        file = "../IntermediateData/" + phase + "/" + phase.lower() + "_" + str(year) + ".csv"
        data_csv = pd.read_csv(file)  
        for column in deleter:
            data_csv = data_csv.drop(column, 1)
        data_csv.to_csv(file, index=False)

#delete last two rows "League Total" and Avg Tm/G
def deleteRows(first_year, last_year, phase):
    for year in range(first_year, last_year+1):
        file = "../RawData/" + phase + "/" + phase.lower() + "_" + str(year) + ".csv"
        outputFile = "../IntermediateData/" + phase + "/" + phase.lower() + "_" + str(year) + ".csv"
        data_csv = pd.read_csv(file) 
        data_csv = data_csv[(data_csv["Tm"] != "League Total") & (data_csv["Tm"] != "Avg Tm/G")]
        data_csv.to_csv(outputFile, index=False)

# used in percentToDecimal()
def p2f(x):
    return float(x.strip('%'))

# used in fixDrives()
def removeOwnHelper(x):
    return float(x.strip('Own '))

# used in fixDrives()
def driveTimeHelper(x):
    minutes = x[0]
    seconds = x[2:]
    return ((float(minutes) * 60) + (float(seconds)))

# remove percent from FG% and XP%
def percentToDecimal(first_year, last_year, phase):
    for year in range(first_year, last_year+1):
        file = "../IntermediateData/" + phase + "/" + phase.lower() + "_" + str(year) + ".csv"
        data_csv = pd.read_csv(file, converters={"FG%": p2f, "XP%": p2f, "FG%_Against": p2f, "XP%_Against": p2f})
        data_csv.to_csv(file, index=False)

# convert drive stats into simple numbers
def fixDrives(first_year, last_year, phase):
        for year in range(first_year, last_year+1):
            file = "../IntermediateData/" + phase + "/" + phase.lower() + "_" + str(year) + ".csv"
            data_csv = pd.read_csv(file, converters={"AvgStartingPosition": removeOwnHelper, "AvgDriveTime": driveTimeHelper}) 
            data_csv.to_csv(file, index=False)

# compute missing things in each spreadsheet
def computeMissing(first_year, last_year, phase):
    # Avg Team "Pen" and "PenYds", SC%, TO%, ExpectedPoints in offense/defense
    # AllTD average in scoring offense
    for year in range(first_year, last_year+1):
        file = "../IntermediateData/" + phase + "/" + phase.lower() + "_" + str(year) + ".csv"
        data_csv = pd.read_csv(file) 
        all_but_avg = data_csv.loc[data_csv["Tm"] != "Avg Team"]
        if phase == "Offense" or phase == "Defense":
            #set these values with .ix
            data_csv.loc[data_csv["Tm"] == "Avg Team", "Pen"] = all_but_avg["Pen"].mean()
            data_csv.loc[data_csv["Tm"] == "Avg Team", "PenYds"] = all_but_avg["PenYds"].mean()
            data_csv.loc[data_csv["Tm"] == "Avg Team", "Sc%"] = all_but_avg["Sc%"].mean()
            data_csv.loc[data_csv["Tm"] == "Avg Team", "TO%"] = all_but_avg["TO%"].mean()
            if year >= 2000:
                data_csv.loc[data_csv["Tm"] == "Avg Team", "ExpectedPoints"] = all_but_avg["ExpectedPoints"].mean()
        if phase == "Pass_Offense" or phase == "Pass_Defense":
            if year >= 2000:
                data_csv.loc[data_csv["Tm"] == "Avg Team", "ExpectedPointsPassing"] = all_but_avg["ExpectedPointsPassing"].mean()
        if phase == "Drives" or phase == "Drives_Against":
            data_csv = data_csv.append({'Tm':'Avg Team', '#Dr': all_but_avg["#Dr"].mean(),
                'Plays/Drive': all_but_avg["Plays/Drive"].mean(),
                'Yds/Drive': all_but_avg["Yds/Drive"].mean(), 'AvgStartingPosition': all_but_avg["AvgStartingPosition"].mean(),
                'AvgDriveTime': all_but_avg["AvgDriveTime"].mean(),
                'Pts/Drive': all_but_avg["Pts/Drive"].mean()}, ignore_index=True)
        if phase == "Scoring_Offense":
            data_csv.loc[data_csv['Tm'] == "Avg Team", "AllTD"] = all_but_avg["AllTD"].mean()
        data_csv.to_csv(file, index=False)

# for defenive stats, add "Against" to the column names
def appendDefense(first_year, last_year, phase):
    for year in range(first_year, last_year+1):
        file = "../IntermediateData/" + phase + "/" + phase.lower() + "_" + str(year) + ".csv"
        against_csv = pd.read_csv(file) 
        against_dict = {}
        for column in against_csv:
            if column != "Tm":
                against_dict[column] = column + "_Defense"
            against_csv = against_csv.rename(columns=against_dict)
            against_csv.to_csv(file, index=False)

# if a cell is empty, fill it with 0
def zeroify(first_year, last_year, phase):
    for year in range(first_year, last_year+1):
        file = "../IntermediateData/" + phase + "/" + phase.lower() + "_" + str(year) + ".csv"
        data_csv = pd.read_csv(file) 
        for column in data_csv:
            data_csv.loc[pd.isnull(data_csv[column]), column] = 0
        data_csv.to_csv(file, index=False)

# apply all the other functions in this file to the raw data. Drive data only exists since 1998, which is why drive data is treated differently
def preprocess(first_year, last_year):
    phases = ["Offense", "Pass_Offense", "Defense", "Pass_Defense", "Returns", "Returns_Against", "Kicking_Punting",
              "Kicking_Punting_Against", "Drives", "Drives_Against", "Scoring_Offense", "Scoring_Defense",
              "Rush_Offense", "Rush_Defense"]
    for phase in phases:
        if phase == "Drives" or phase == "Drives_Against":
            deleteRows(1998, last_year, phase)
            renamify(1998, last_year, phase)
            deleteCols(1998, last_year, phase)
            fixDrives(1998, last_year, phase)
            zeroify(1998, last_year, phase)
            computeMissing(1998, last_year, phase)
        else:
            deleteRows(first_year, last_year, phase)
            renamify(first_year, last_year, phase)
            deleteCols(first_year, last_year, phase)
            zeroify(first_year, last_year, phase)
            
    percentToDecimal(first_year, last_year, "Kicking_Punting")
    percentToDecimal(first_year, last_year, "Kicking_Punting_Against")

    computeMissing(first_year, last_year, "Offense")
    computeMissing(first_year, last_year, "Defense")
    computeMissing(first_year, last_year, "Pass_Offense")
    computeMissing(first_year, last_year, "Pass_Defense")
    computeMissing(first_year, last_year, "Scoring_Offense")
    
    appendDefense(first_year, last_year, "Defense")
    appendDefense(first_year, last_year, "Pass_Defense")
    appendDefense(first_year, last_year, "Returns_Against")
    appendDefense(first_year, last_year, "Kicking_Punting_Against")
    appendDefense(first_year, last_year, "Rush_Defense")
    appendDefense(first_year, last_year, "Scoring_Defense")
    appendDefense(1998, last_year, "Drives_Against")


    
preprocess(min_year, max_year)