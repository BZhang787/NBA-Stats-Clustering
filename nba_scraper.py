# Group Members : Diego Bobrow, Nicholas Tincani Ueki, Brandon Zhang

import time
from selenium import webdriver


shooting_stats_url = 'https://www.basketball-reference.com/leagues/NBA_{}_shooting.html'

driver = webdriver.Chrome(executable_path='C:/Users/brand/Downloads/chromedriver_win32/chromedriver')

for year in range(2001, 2023):
    url = shooting_stats_url.format(year)
    driver.get(url)
    driver.execute_script("window.scrollTo(1, 10000)")
    time.sleep(2)

    html = driver.page_source

    with open("shooting_{}.html".format(year), "w+", encoding='utf-8') as f:
        f.write(html)