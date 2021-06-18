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
# soup object for searching through html code
soup = BeautifulSoup(html, features="html.parser")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

ratingsHashSeparated = ""
summaryList = list(soup.findAll("p"))
# print(summaryList)
for data in summaryList:
    text = data.getText()
    if "Rtg" in text:
        textList = text.split()
        for str in textList:
            if is_number(str):
                ratingsHashSeparated += str + "#"
print(ratingsHashSeparated.rstrip(ratingsHashSeparated[-1]))
        