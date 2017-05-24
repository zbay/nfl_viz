import pandas as pd

teamDict = {"WAS": ["Washington Redskins"], "NYG": ["New York Giants"], "PHI": ["Philadelphia Eagles"],
"DAL": ["Dallas Cowboys"], "ATL": ["Atlanta Falcons"], "CAR": ["Carolina Panthers"], "TB": ["Tampa Bay Buccaneers"],
"NO": ["New Orleans Saints"], "LAR": ["St. Louis Rams", "Los Angeles Rams", "Cleveland Rams"], "SEA": ["Seattle Seahawks"],
"SF": ["San Francisco 49ers"], "ARI": ["Arizona Cardinals", "St. Louis Cardinals", "Phoenix Cardinals"], 
"GB": ["Green Bay Packers"], "DET": ["Detroit Lions"], "MIN": ["Minnesota Vikings"], "CHI": ["Chicago Bears"], 
"BAL": ["Baltimore Ravens"],
"CLE": ["Cleveland Browns"], "CIN": ["Cincinnati Bengals"], "PIT": ["Pittsburgh Steelers"], 
"IND": ["Indianapolis Colts", "Baltimore Colts"],
"JAX": ["Jacksonville Jaguars"], "HOU": ["Houston Texans"], "TEN": ["Tennessee Titans", "Tennessee Oilers", "Houston Oilers"],
"NE": ["New England Patriots"], "NYJ": ["New York Jets"], "BUF": ["Buffalo Bills"], "MIA": ["Miami Dolphins"], 
"KC": ["Kansas City Chiefs"],
"DEN": ["Denver Broncos"], "OAK": ["Oakland Raiders", "Los Angeles Raiders"], 
"LAC": ["San Diego Chargers", "Los Angeles Chargers"], "AVG": ["Avg Team"]}

# "AVG": ["Avg Team"]

#earliest years we are using data from
min_year = 1981

#latest year
max_year = 2016



def teamify():
    for team in teamDict:
        outputFile = "../ProcessedData/Teamified/" + team + ".csv"
        startFile = "../ProcessedData/Yearly_Ranked/ranked_1981.csv"
        start_csv = pd.read_csv(startFile)
        team_csv = pd.DataFrame(columns=start_csv.columns.values)
        for year in range(min_year, max_year+1):
            yearFile = "../ProcessedData/Yearly_Ranked/ranked_" + str(year) + ".csv"
            ranked_csv = pd.read_csv(yearFile)
            teams = ranked_csv["Tm"]
            for tm in teams:
                if tm in teamDict[team]:
                    # add row to teamDict where tm = ['Tm'] or whatever
                    team_row = ranked_csv[ranked_csv["Tm"] == tm]
                    team_row["Year"] = year
                    team_csv = team_csv.append(team_row)
            
        cols = team_csv.columns.values.tolist()
        cols.remove("Tm")
        cols.remove("Year")
        cols = ["Year"] + cols
            
        team_csv = team_csv[cols]
        team_csv.to_csv(outputFile, index=False)
             
teamify()