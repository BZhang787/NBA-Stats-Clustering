import pandas as pd
from bs4 import BeautifulSoup
import lxml

df = []

for year in range(1997, 2024):
    with open('shooting_{}.html'.format(year), encoding='utf-8') as f:
        page = f.read()

    soup = BeautifulSoup(page, "html.parser")
    soup.find('tr', class_="thead").decompose()
    soup.find('tr', class_="over_header").decompose()
    shooting_table = soup.find(id="shooting_stats")
    player = pd.read_html(str(shooting_table))[0]
    player["Year"] = year
    df.append(player)

players = pd.concat(df)

players.to_csv("shooting_stats.csv")
