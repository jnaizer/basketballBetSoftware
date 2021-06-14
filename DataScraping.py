from bs4 import BeautifulSoup
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import requests
import random
from urllib.request import urlopen

# NBA season we will be analyzing
year = 2019
team = "UTA"
# URL page we will scraping (see image above)
url = "https://www.basketball-reference.com/teams/{}/2021_games.html".format(team)
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
stats = pd.DataFrame(player_stats, columns = headers)
stats.head(10)
print(stats)