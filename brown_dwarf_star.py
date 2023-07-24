from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv
import time
import requests
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome("C:/Users/Brajesh/Downloads/chromedriver_win32 (1)/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

# Get Page
page = requests.get(START_URL)

# Parse Page
soup = BeautifulSoup(page.text,"html.parser")

# Get <table> with class = 'wikitable sortable'
star_table = soup.find_all("table", {"class":"wikitable sortable"})

total_table = len(star_table)


tem_list= []

table_rows = star_table[1].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    tem_list.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]

print(tem_list)

for i in range(1,len(tem_list)):
    
    Star_names.append(tem_list[i][0])
    Distance.append(tem_list[i][5])
    Mass.append(tem_list[i][7])
    Radius.append(tem_list[i][8])

headers = ['Star_name','Distance','Mass','Radius']  
df_2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df_2)

df_2.to_csv('dwarf_star.csv', index=True, index_label="id")
