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
        f.write("Team1#Team2#PointDifferential#eFGDif#TOVDif#ORBDiff#FT/FGADiff" + "\n")

        # loops through every team in the dictionary
        for key in teams:
            for teamYear in years:
                filePath2 = "Python Projects/BasketballBetting/Team Schedules/" + str(teams(key)) + "/" + str(teamYear)
                with open(filePath2, "r") as g:
                    filePath3 = 
                    lines = g.readlines()
                    for line in lines:
                        list = line.split("#")
                        f.write(str(teams)) + "#" + list[3] + "#" + abs(list[4] - list[5]) + "#" +
                g.close()
    # closes file
    f.close()

# output for user
print("Complete!")