from urllib.request import urlopen
import random
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import os, sys, stat

# dictionary that stores the abbreviation as the key and the full name as the value
teams = {"MIL" : "Milwaukee Bucks", "BRK" : "Brooklyn Nets", "WAS" : "Washington Wizards", "UTA" : "Utah Jazz", "POR" : "Portland Trail Blazers",
 "IND" : "Indiana Pacers", "PHO" : "Phoenix Suns", "DEN" : "Denver Nuggets", "ATL" : "Atlanta Hawks", "BOS" : "Boston Celtics", "CHO" : "Charlotte Hornets",
 "HOU" : "Houston Rockets", "DAL" : "Dallas Mavericks", "LAC" : "Los Angeles Clippers", "NOP" : "New Orleans Pelicans", "SAS" : "San Antonio Spurs",
 "LAL" : "Los Angeles Lakers", "MIN" : "Minnesota Timberwolves", "TOR" : "Toronto Raptors", "MEM" : "Memphis Grizzlies", "MIA" : "Miami Heat",
 "PHI" : "Philadelphia 76ers", "OKC" : "Oklahoma City Thunder", "SAC" : "Sacramento Kings", "ORL" : "Orlando Magic", "DET" : "Detroit Pistons",
 "CLE" : "Cleveland Cavaliers", "CHI" : "Chicago Bulls", "GSW" : "Golden State Warriors", "NYK" : "New York Knicks"}

# list of the years 2015 through 2021
years = list(range(2015, 2022))

# loop through each key (abbreviation) in the teams dictionary
for key in teams:

    # loop through each year in the years list
    for year in years:

        # constructing the url from the key and year
        url = "https://www.basketball-reference.com/teams/{}/{}_games.html".format(key, year)
        # this is the HTML code from the given URL that we will be looking through
        html = urlopen(url)
        # i fucked up my soup
        soup = BeautifulSoup(html)
        # use findALL() to get the column headers
        soup.findAll('tr', limit=2)
        # use getText() to extract the text we need into a list
        headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
        # exclude the first column because we dont care about the ranking order
        headers = headers[1:]
        # avoid the first header row
        rows = soup.findAll('tr')[1:]
        player_stats = [[td.getText() for td in rows[i].findAll('td')]
                        for i in range(len(rows))]
        # create the dataframe
        stats = pd.DataFrame(player_stats, columns=headers)
        stats.head(10)
        
        # creating the directory path for the file with the value of the key in teams so it is the full name
        dirPath = "Python Projects/BasketballBetting/" + str(teams[key])

        # creating the file path
        filePath = "Python Projects/BasketballBetting/" + str(teams[key]) + "/" + str(year)

        # if the directory is not made yet, ,make it (this should only execute the first time you run the program)
        if (not os.path.isdir(dirPath)):
            os.makedirs(dirPath)
        
        # this gives the python program permission to edit the file
        # os.chmod(dirPath, stat.S_IRWXU)

        # converts the stats dataframe into a # separated file and stores it at file location
        stats.to_csv(filePath, sep="#", index=False)

        # boolean used for editing only the first row (changing header names)
        first = True

        #opens file into read mode
        with open(filePath, "r") as f:
            # stores all the lines of the file into the variable 'lines'
            lines = f.readlines()
        # opens the same file into write mode
        with open(filePath, "w") as f:
            # iterating through each line in lines
            for line in lines:
                # skipping the weird lines that looked like "#############"
                if (line.__contains__("######")):
                    continue
                # splits the lines we want into a list
                list = line.split("#")
                #if its the first row (header row)
                if (first):
                    # change the fourth column title to Location
                    list[4] = "Location"
                    #change the sixth column title to Outcome
                    list[6] = "Outcome"
                    # changes first to false because we dont want to change the next lines since they are not header rows
                    first = False
                else:
                    # changing the @ symbol to Away
                    if (list[4] == "@"):
                        list[4] = "Away"
                    else:
                        # else change it to home
                        list[4] = "Home"
                # the next four lines are deleting the unnecessary empty columns
                del list[2]
                del list[2]
                del list[5]
                del list[10]
                # join the edited list back into a # separated string
                result = "#".join(list)
                # write the edited string back to the same file
                f.write(result + "\n")
        
        # Assures user the program is still running
        print(teams[key] + " " + str(year))

# notifies user that the program is finished
print("Complete!")