import pandas as pd

teams = ["WAS", "NYG", "PHI", "DAL", "ATL", "CAR", "NO", "TB", "GB", "DET", "MIN", "CHI", "SF", "ARI", "LAR", "SEA",
         "BAL", "CLE", "CIN", "PIT", "IND", "JAX", "HOU", "TEN", "NE", "MIA", "NYJ", "BUF", "LAC", "DEN", "KC", "OAK"]

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
def rankFusionStats(first_year, last_year):
    for year in range(first_year, last_year+1):
        fileLocation = "../ProcessedData/Yearly_Ranked/ranked_" + str(year) + ".csv"
        year_csv = pd.read_csv(fileLocation)
        avg_csv = year_csv.loc[year_csv["Tm"] == "Avg Team"]
        year_csv = year_csv.loc[year_csv["Tm"] != "Avg Team"]
        
        year_csv["Oscore"] = ((year_csv["PF_High_Rank"]) + (year_csv["TotalYds_High_Rank"]) + (year_csv["1stD_High_Rank"])
            + (year_csv["TO_Low_Rank"])
            + (year_csv["Y/Arun_High_Rank"]) + (year_csv["NY/A_High_Rank"])) / 6.0
        year_csv["Dscore"] = ((year_csv["PF_Defense_Low_Rank"]) + (year_csv["TotalYds_Defense_Low_Rank"]) + 
            (year_csv["1stD_Defense_Low_Rank"])
            + (year_csv["TO_Defense_High_Rank"]) +
            (year_csv["Y/Arun_Defense_Low_Rank"]) + (year_csv["NY/A_Defense_Low_Rank"])) / 6.0
        year_csv["STscore"] = (((year_csv["Y/PR_High_Rank"]) + (year_csv["Y/KR_High_Rank"]) 
            + (year_csv["Y/Pnt_High_Rank"]) + (year_csv["FG%_High_Rank"]) + 
            ((year_csv['TFGM_High_Rank'] + year_csv['PrYds_High_Rank'] + year_csv['KrYds_High_Rank'] 
              + year_csv['KrYds_Defense_Low_Rank'] + year_csv['PrYds_Defense_Low_Rank']) / 5.0) +
            (year_csv["Y/PR_Defense_Low_Rank"]) + (year_csv["Y/KR_Defense_Low_Rank"]) + 
            (year_csv["Y/Pnt_Defense_Low_Rank"]) + (0.1 * (year_csv["FG%_Defense_Low_Rank"])))) / 8.1
        year_csv["ThreePhaseScore"] = (((year_csv["Oscore"]) + (year_csv["Dscore"]) + (0.75* (year_csv["STscore"])))) / 2.75
        year_csv["FantasyPassScore"] = ((year_csv["Cmp_High_Rank"]) + (year_csv["PassYds_High_Rank"] * 2.0) +
            (year_csv["PassTD_High_Rank"] * 2.0) + (year_csv["Int%_Low_Rank"])
            + (year_csv["1stDpass_High_Rank"]) + (year_csv["Y/Apass_High_Rank"]) + year_csv["Int_Low_Rank"]) / 10.0
        year_csv["FantasyRushScore"] = ((year_csv["RushAtt_High_Rank"]) + (year_csv["RushYds_High_Rank"] * 2.0) +
            (year_csv["Y/Arun_High_Rank"]) +
            (year_csv["RushTD_High_Rank"] * 2.0) + (year_csv["1stDrun_High_Rank"]) + (year_csv["FL_Low_Rank"])) / 8.0
        year_csv["FantasyOffenseScore"] = ((year_csv["FantasyPassScore"]) + (year_csv["FantasyRushScore"])) / 2.0
        year_csv["FantasyDstScore"] = ((((year_csv["PrYds_High_Rank"]) + (year_csv["KrYds_High_Rank"])) / 2) +
            (year_csv["PF_Defense_Low_Rank"]) + (year_csv["TotalYds_Defense_Low_Rank"]) + (year_csv["Sk_Defense_High_Rank"])
            + (year_csv["TO_Defense_High_Rank"]) + (year_csv['DefensivePtsScored_High_Rank'])) / 6.0
        if year >= 1998:
            year_csv["GameControlScore"] = ( (year_csv["TimeOfPossession_High_Rank"]) + (year_csv["AvgFieldPositionDifferential_High_Rank"])
                + (year_csv["Yds_Differential_High_Rank"]) + (year_csv["PF_Differential_High_Rank"]) +  (year_csv["TO_Differential_High_Rank"]) ) / 5.0
            year_csv["GameControlPlusBalance"] = ((year_csv["GameControlScore"] + year_csv["ThreePhaseScore"]) / 2.0)
            year_csv["GameControlScore_Rank"] = year_csv["GameControlScore"].rank(ascending=True)
            year_csv["GameControlPlusBalance_Rank"] = year_csv["GameControlPlusBalance"].rank(ascending=True)
            
        year_csv["Oscore_Rank"] = year_csv["Oscore"].rank(ascending=True)
        year_csv["Dscore_Rank"] = year_csv["Dscore"].rank(ascending=True)
        year_csv["STscore_Rank"] = year_csv["STscore"].rank(ascending=True)
        year_csv["ThreePhaseScore_Rank"] = year_csv["ThreePhaseScore"].rank(ascending=True)
        year_csv["FantasyPassScore_Rank"] = year_csv["FantasyPassScore"].rank(ascending=True)
        year_csv["FantasyRushScore_Rank"] = year_csv["FantasyRushScore"].rank(ascending=True)
        year_csv["FantasyOffenseScore_Rank"] = year_csv["FantasyOffenseScore"].rank(ascending=True)
        year_csv["FantasyDstScore_Rank"] = year_csv["FantasyDstScore"].rank(ascending=True)
        
        num_teams = year_csv.shape[0]
        avg_csv["Oscore"] = (num_teams + 1)/2
        avg_csv["Dscore"] = (num_teams + 1)/2
        avg_csv["STscore"] = (num_teams + 1)/2
        avg_csv["ThreePhaseScore"] = (num_teams + 1)/2
        avg_csv["FantasyPassScore"] = (num_teams + 1)/2
        avg_csv["FantasyRushScore"] = (num_teams + 1)/2
        avg_csv["FantasyOffenseScore"] = (num_teams + 1)/2
        avg_csv["FantasyDstScore"] = (num_teams + 1)/2
        avg_csv["GameControlScore"] = (num_teams + 1)/2
        avg_csv["GameControlPlusBalance"] = (num_teams + 1)/2
        avg_csv["Oscore_Rank"] = (num_teams + 1)/2
        avg_csv["Dscore_Rank"] = (num_teams + 1)/2
        avg_csv["STscore_Rank"] = (num_teams + 1)/2
        avg_csv["ThreePhaseScore_Rank"] = (num_teams + 1)/2
        avg_csv["FantasyPassScore_Rank"] = (num_teams + 1)/2
        avg_csv["FantasyRushScore_Rank"] = (num_teams + 1)/2
        avg_csv["FantasyOffenseScore_Rank"] = (num_teams + 1)/2
        avg_csv["FantasyRushScore_Rank"] = (num_teams + 1)/2
        avg_csv["FantasyDstScore_Rank"] = (num_teams + 1)/2
        avg_csv["GameControlScore_Rank"] = (num_teams + 1)/2
        avg_csv["GameControlPlusBalance_Rank"] = (num_teams + 1)/2
        
        year_csv = year_csv.append(avg_csv)
        year_csv.to_csv(fileLocation, index=False)
        
rankFusionStats(1981, 2016)