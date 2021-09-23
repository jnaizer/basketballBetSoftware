#####################################
# Change the start year to different years to make the program run faster.
# Valid values are from 2015 to current year
startYear = 2015
#####################################

import os, sys, stat

# checks and installs required libraries onto local computer
print("Installing libraries...")
os.system("pip install requests")
os.system("pip install progressbar")

from datetime import date
from urllib.request import urlopen
from progressbar import ProgressBar

# dictionary that stores the abbreviation as the key and the full name as the value
teams = {"MIL": "Milwaukee Bucks", "BRK": "Brooklyn Nets", "WAS": "Washington Wizards", "UTA": "Utah Jazz",
         "POR": "Portland Trail Blazers",
         "IND": "Indiana Pacers", "PHO": "Phoenix Suns", "DEN": "Denver Nuggets", "ATL": "Atlanta Hawks",
         "BOS": "Boston Celtics", "CHO": "Charlotte Hornets",
         "HOU": "Houston Rockets", "DAL": "Dallas Mavericks", "LAC": "Los Angeles Clippers",
         "NOP": "New Orleans Pelicans", "SAS": "San Antonio Spurs",
         "LAL": "Los Angeles Lakers", "MIN": "Minnesota Timberwolves", "TOR": "Toronto Raptors",
         "MEM": "Memphis Grizzlies", "MIA": "Miami Heat",
         "PHI": "Philadelphia 76ers", "OKC": "Oklahoma City Thunder", "SAC": "Sacramento Kings", "ORL": "Orlando Magic",
         "DET": "Detroit Pistons",
         "CLE": "Cleveland Cavaliers", "CHI": "Chicago Bulls", "GSW": "Golden State Warriors", "NYK": "New York Knicks"}

# list of the years startYear through endYear
currentDate = date.today()
years = list(range(startYear, currentDate.year + 1))

# creating a progress bar to display
pbar = ProgressBar()

# creating the directory path for the file with the value of the key in teams so it is the full name
dirPath = "Python Projects/BasketballBetting/OrganizedData"

# if the directory is not made yet, make it (this should only execute the first time you run the program)
if (not os.path.isdir(dirPath)):
    os.makedirs(dirPath)

# output for user
print("\nFetching data...")

# loop through each year in the years list
for year in pbar(years):

    # creating the file path
    filePath = "Python Projects/BasketballBetting/OrganizedData/" + str(year) + ".txt"

    # opens designated file path
    with open(filePath, "w") as f:

        # writes the column headers to the file
        f.write("Team1#Team2#PointDifferential#Off eFG Diff#Off TOV Diff#Off ORB Diff#Off FT/FGA Diff#Def eFG Diff#Def TOV Diff#Def DRB Diff#Def FT/FGA Diff" + "\n")

        # loops through every team in the dictionary
        for key in teams:
            for teamYear in years:
                filePath2 = "Python Projects/BasketballBetting/Team Schedules/" + str(teams[key]) + "/" + str(teamYear) + ".txt"
                with open(filePath2, "r") as g:
                    lines = g.readlines()
                    skipHeader = True
                    for line in lines:
                        if not skipHeader:
                            list = line.split("#")
                            teamStats = []
                            oppTeamStats = []
                            gameData = str(teams[key]) + "#" + str(list[3]) + "#" + str(abs(float(list[6]) - float(list[5]))) + "#"
                            filePath3 = "Python Projects/BasketballBetting/Team Miscellaneous/" + str(teamYear) + ".txt"
                            with open (filePath3, "r") as h:
                                lines2 = h.readlines()
                                skipHeader2 = True
                                for line2 in lines2:
                                    if not skipHeader2:
                                        list2 = line2.split("#")
                                        if (str(list2[0]) == str(teams[key])):
                                            teamStats = list2
                                        if (str(list2[0]) == str(list[3])):
                                            oppTeamStats = list2
                                    skipHeader2 = False
                            gameData += str(round(abs(float(teamStats[13]) - float(oppTeamStats[13])), 3)) + "#" + str(round(abs(float(teamStats[14]) - float(oppTeamStats[14])), 3)) + "#" + str(round(abs(float(teamStats[15]) - float(oppTeamStats[15])), 3)) + "#" + str(round(abs(float(teamStats[16]) - float(oppTeamStats[16])), 3)) + "#" + str(round(abs(float(teamStats[17]) - float(oppTeamStats[17])), 3)) + "#" + str(round(abs(float(teamStats[18]) - float(oppTeamStats[18])), 3)) + "#" + str(round(abs(float(teamStats[19]) - float(oppTeamStats[19])), 3)) + "#" + str(round(abs(float(teamStats[20]) - float(oppTeamStats[20])), 3)) + "#" + "\n"
                            f.write(gameData)
                            h.close()
                        skipHeader = False
                g.close()
    # closes file
    f.close()

# output for user
print("Complete!")