#####################################
# Change the start year to different years to make the program run faster.
# Valid values are from 2015 to current year
startYear = 2015
#####################################

import os, sys, stat

# checks and installs required libraries onto local computer
print("Installing libraries...")
os.system("pip install requests")
os.system("pip install beautifulsoup4")
os.system("pip install pandas")
os.system("pip install wget")
os.system("pip install progressbar")

from datetime import date
from urllib.request import urlopen
import random
import requests
import wget
import codecs
import time
from contextlib import contextmanager
from bs4 import BeautifulSoup
import pandas as pd
pd.set_option('display.max_colwidth', 500)
from progressbar import ProgressBar

# dictionary that stores the abbreviation as the key and the full name as the value
teams = {"MIL" : "Milwaukee Bucks", "BRK" : "Brooklyn Nets", "WAS" : "Washington Wizards", "UTA" : "Utah Jazz", "POR" : "Portland Trail Blazers",
 "IND" : "Indiana Pacers", "PHO" : "Phoenix Suns", "DEN" : "Denver Nuggets", "ATL" : "Atlanta Hawks", "BOS" : "Boston Celtics", "CHO" : "Charlotte Hornets",
 "HOU" : "Houston Rockets", "DAL" : "Dallas Mavericks", "LAC" : "Los Angeles Clippers", "NOP" : "New Orleans Pelicans", "SAS" : "San Antonio Spurs",
 "LAL" : "Los Angeles Lakers", "MIN" : "Minnesota Timberwolves", "TOR" : "Toronto Raptors", "MEM" : "Memphis Grizzlies", "MIA" : "Miami Heat",
 "PHI" : "Philadelphia 76ers", "OKC" : "Oklahoma City Thunder", "SAC" : "Sacramento Kings", "ORL" : "Orlando Magic", "DET" : "Detroit Pistons",
 "CLE" : "Cleveland Cavaliers", "CHI" : "Chicago Bulls", "GSW" : "Golden State Warriors", "NYK" : "New York Knicks"}

# list of the years startYear through endYear
currentDate = date.today()
years = list(range(startYear, currentDate.year + 1))

# helper function used to suppress trivial terminal output when executing "wget.download(url)"
@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

# creating a progress bar to display
pbar = ProgressBar()

# creating the directory path for the file with the value of the key in teams so it is the full name
dirPath = "Python Projects/BasketballBetting/Team Miscellaneous"

# if the directory is not made yet, make it (this should only execute the first time you run the program)
if (not os.path.isdir(dirPath)):
    os.makedirs(dirPath)

# output for user
print("\nFetching team miscellaneous...")

# loop through each year in the years list
for year in pbar(years):

    # creating the file path
    filePath = "Python Projects/BasketballBetting/Team Miscellaneous/" + str(year) + ".txt"

    # opens designated file path
    with open(filePath, "w") as f:

        # writes the column headers to the file
        f.write("Team Name#W#L#PW#PL#MOV#SOS#SRS#ORtg#DRtg#Pace#FTr#3PAr#eFG%#TOV%#ORB%#FT/FGA#eFG%#TOV%#DRB%#FT/FGA#Arena#Attendance" + "\n")

        # loops through every team in the dictionary
        for key in teams:

            # constructing the url from the key and year
            url = "https://www.basketball-reference.com/teams/{}/{}.html".format(key, year)
            
            # suppresses the trivial terminal output
            with suppress_stdout():
             
                # this is the HTML code from the given URL that we will be looking through
                html = wget.download(url)

            # complete html text
            grossText = (codecs.open(html, "r", "utf-8")).read()

            # removes the html file that was downloaded (for cleanup purposes)
            fileToRemove = str(year) + ".html"
            os.remove(fileToRemove)

            # finding where the team misc table is in the text
            loc = grossText.find("div_team_misc")
            tempText = (grossText[loc:])

            # cutting off the text before and after the misc table text to isolate it
            loc2 = tempText.find("<tbody>") + 7
            loc3 = tempText.find("</table>")
            text = (tempText[loc2:loc3])

            # string used for appending the data
            teamMiscHashSeparated = ""

            # keeps track of how many rows we have read so far
            num = 0

            # beautifulsoup
            soup = BeautifulSoup(text, "html.parser")

            # creates a list of all the rows in the table
            columns = soup.find_all("td")

            # iterates through each column and appends the data to teamMiscHashSeparated string
            for col in columns:
              # if the col contents exists ( >= 1 ) and it is in the first row ( num < 22 )
              if (len(col.contents) >= 1) and (num < 22):
                teamMiscHashSeparated += col.contents[0] + "#"
                num += 1
            
            # writes the hash separated strings to the file with the last "#" cut off
            f.write(teams[key] + "#" + teamMiscHashSeparated.rstrip(teamMiscHashSeparated[-1]) + "\n")

    # closes file
    f.close()

# output for user
print("Complete!")
