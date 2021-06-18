import os, sys, stat
from urllib.request import urlopen
import random
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import os, sys, stat
from progressbar import ProgressBar

# constructing the url from the key and year
url = "https://www.basketball-reference.com/teams/UTA/2021.html"
# this is the HTML code from the given URL that we will be looking through
html = urlopen(url)
# i fucked up my soup
soup = BeautifulSoup(html, features="html.parser")

summaryList = list(soup.findAll("p"))
# print(summaryList)
for data in summaryList:
    text = data.getText()
    if "Rtg" in text:
        print(text)