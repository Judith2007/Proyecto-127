#from selenium import webdriver
#from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

#browser = webdriver.Chrome("chromedriver.exe")
#browser.get(START_URL)

page= requests.get(START_URL)
print(page)

soup = bs(page.text, 'html.parser')
star_table= soup.find('table')

time.sleep(10)

temp_list=[]

table_row= star_table.find_all('tr')
print(table_row)

for tr in table_row:
    td= tr.find_all('td')
    row=[i.text.rstrip() for i in td ]
    temp_list.append(row)
print(temp_list)
     
