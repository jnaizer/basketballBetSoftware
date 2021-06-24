import os, sys, stat

# checks and installs required libraries onto local computer
print("Installing libraries...")
os.system("pip install requests")
os.system("pip install beautifulsoup4")
os.system("pip install pandas")
os.system("pip install progressbar")

from datetime import date
from urllib.request import urlopen
import random
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import os, sys, stat
from progressbar import ProgressBar

# dictionary that stores the abbreviation as the key and the full name as the value
teams = {"MIL" : "Milwaukee Bucks", "BRK" : "Brooklyn Nets", "WAS" : "Washington Wizards", "UTA" : "Utah Jazz", "POR" : "Portland Trail Blazers",
 "IND" : "Indiana Pacers", "PHO" : "Phoenix Suns", "DEN" : "Denver Nuggets", "ATL" : "Atlanta Hawks", "BOS" : "Boston Celtics", "CHO" : "Charlotte Hornets",
 "HOU" : "Houston Rockets", "DAL" : "Dallas Mavericks", "LAC" : "Los Angeles Clippers", "NOP" : "New Orleans Pelicans", "SAS" : "San Antonio Spurs",
 "LAL" : "Los Angeles Lakers", "MIN" : "Minnesota Timberwolves", "TOR" : "Toronto Raptors", "MEM" : "Memphis Grizzlies", "MIA" : "Miami Heat",
 "PHI" : "Philadelphia 76ers", "OKC" : "Oklahoma City Thunder", "SAC" : "Sacramento Kings", "ORL" : "Orlando Magic", "DET" : "Detroit Pistons",
 "CLE" : "Cleveland Cavaliers", "CHI" : "Chicago Bulls", "GSW" : "Golden State Warriors", "NYK" : "New York Knicks"}

currentDate = date.today()
# list of the years we want data from
years = list(range(2015, currentDate.year + 1))

# creating a progress bar
pbar = ProgressBar()

# creating directory path
dirPath = "Python Projects/BasketballBetting/Misc Team Stats"

# if directory does not exist, create it
if (not os.path.isdir(dirPath)):
    os.makedirs(dirPath)

# output for user
print("Fetching team stats...")

# looping through each year we want data from
for year in pbar(years):

    # creating file path for files to exist in
    filePath = "Python Projects/BasketballBetting/Misc Team Stats/" + str(year) + ".txt"

    # open filePath
    with open(filePath, "w") as file:

        # writing headers for the text file
        file.write("Team Name#ORtg#DRtg#FTr#3PAr#eFT%#TOV%#ORB%#FT/FGA#opp eFG%#opp TOV%#opp DRB%#opp FT/FGA" + "\n")

        # looping through each team
        for team in teams:

            # constructing url from team and year
            url = "https://www.basketball-reference.com/teams/{}/{}.html".format(team, year)
            # openning html code from the given url
            html = urlopen(url)
            # soup
            soup = BeautifulSoup(html, features="html.parser")

            # getting the desired data table
            table = soup.find('div', class_='table_wrapper', id="all_team_misc")
            tbody = table.find('tbody')
            print(tbody)



