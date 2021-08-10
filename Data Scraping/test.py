import os
import wget
import codecs
from bs4 import BeautifulSoup

url = "https://www.basketball-reference.com/teams/UTA/2016.html"
html = wget.download(url)
print("")
grossText = (codecs.open(html, "r", "utf-8")).read()

os.remove("2016.html")

loc = grossText.find("div_team_misc")
tempText = (grossText[loc:])

loc2 = tempText.find("<tbody>") + 7
loc3 = tempText.find("</table>")
text = (tempText[loc2:loc3])
# print(text)

soup = BeautifulSoup(text, "html.parser")
rows = soup.find_all("td")
for row in rows:
  if (len(row.contents) >= 1):
    print(row.contents[0])
  else:
    print("")