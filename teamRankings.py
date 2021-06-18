import os, sys, stat

# checks and installs required libraries onto local computer
print("Installing libraries...")
os.system("pip install requests")
os.system("pip install beautifulsoup4")
os.system("pip install pandas")
os.system("pip install progressbar")

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

# list of the years 2015 through 2021
years = list(range(2015, 2022))

# creating a progress bar to display
pbar = ProgressBar()

# helper function for determining if a string is a number or not
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# list of the years 2015 through 2021
years = list(range(2015, 2022))

# creating the directory path for the file with the value of the key in teams so it is the full name
dirPath = "Python Projects/BasketballBetting/Team Ratings"

# if the directory is not made yet, make it (this should only execute the first time you run the program)
if (not os.path.isdir(dirPath)):
    os.makedirs(dirPath)

# output for user
print("Fetching team ratings...")

# loop through each year in the years list
for year in pbar(years):

    # creating the file path
    filePath = "Python Projects/BasketballBetting/Team Ratings/" + str(year) + ".txt"

    # opens designated file path
    with open(filePath, "w") as f:

        # writes the column headers to the file
        f.write("Team Name#Off Rtg#Def Rtg#Net Rtg" + "\n")

        # loops through every team in the dictionary
        for key in teams:

            # constructing the url from the key and year
            url = "https://www.basketball-reference.com/teams/{}/{}_games.html".format(key, year)
            # this is the HTML code from the given URL that we will be looking through
            html = urlopen(url)
            # i fucked up my soup
            soup = BeautifulSoup(html, features="html.parser")

            # string that we will append the ratings to with a # separator
            ratingsHashSeparated = ""
            # this is the list of all <p>"text"</p> in the html code
            summaryList = list(soup.findAll("p"))

            # loop through each <p>"text"</p> in the list and see if it is the one that contains the ratings
            for data in summaryList:
                text = data.getText()
                # if the <p>"text"</p> has the ratings in it
                if "Rtg" in text:
                    # split the text into a list
                    textList = text.split()
                    # if the string is a number, append it to the ratingsHashSeparated variable
                    for string in textList:
                        if is_number(string):
                            ratingsHashSeparated += string + "#"
            
            # writes the ratingsHashSeparated with the respective team to the file with the last "#" cut off
            f.write(teams[key] + "#" + ratingsHashSeparated.rstrip(ratingsHashSeparated[-1]) + "\n") 
