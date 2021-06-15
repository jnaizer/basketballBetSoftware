from urllib.request import urlopen
import random
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
pd.set_option('display.max_colwidth', 500)

# NBA season we will be analyzing
year = 2019
team = "UTA"
# URL page we will scraping (see image above)
url = "https://www.basketball-reference.com/teams/{}/{}_games.html".format(
    team, year)
# this is the HTML from the given URL
html = urlopen(url)
soup = BeautifulSoup(html)

# use findALL() to get the column headers
soup.findAll('tr', limit=2)
# use getText()to extract the text we need into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
# exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
headers = headers[1:]
print(headers)

# avoid the first header row
rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]
stats = pd.DataFrame(player_stats, columns=headers)
stats.head(10)
print(stats)

stats.to_csv(r"Python Projects\BasketballBetting\file1", sep="#", index=False)
# file1 = open(r"Python Projects\BasketballBetting\file1", "r")
# file2 = open(r"Python Projects\BasketballBetting\file2", "w")

first = True

with open(r"Python Projects\BasketballBetting\file1", "r") as f:
    lines = f.readlines()
with open(r"Python Projects\BasketballBetting\file1", "w") as f:
    for line in lines:
        if (line.__contains__("######")):
            continue
        list = line.split("#")
        if (first):
            list[4] = "Location"
            list[6] = "Outcome"
            first = False
        else:
            if (list[4] == "@"):
                list[4] = "Away"
            else:
                list[4] = "Home"
        del list[2]
        del list[2]
        del list[5]
        del list[10]
        result = "#".join(list)
        f.write(result + "\n")

