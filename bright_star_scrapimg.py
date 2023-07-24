from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("C:/Users/Brajesh/Downloads/chromedriver_win32 (1)/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scraped_data = []

# Define Exoplanet Data Scrapping Method
def scrape():
    
     soup = BeautifulSoup(browser.page_source, "html.parser")
     
     bright_star_table = soup.find("table", attrs={"class", "wikitable"})
     
     table_body = bright_star_table.find('tbody')
     
     table_rows = table_body.find_all('tr')
     
     for row in table_rows:
          table_cols = row.find_all('td')
          print(table_cols)
          
          tem_list = []
          
          for col_data in table_cols:
               print(col_data.text)
               
               data = col_data.text.strip()
               print(data)
               
               tem_list.append(data)

            # Append data to star_data list
               scraped_data.append(tem_list)
               
               
               
scrape() 


star_data = []


for i in range(0,len(scraped_data)):
    
    Star_names = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lum = scraped_data[i][7]

    data2 = [Star_names, Distance, Mass, Radius, Lum]
    star_data.append(data2)

print(star_data)

headers = ['Star_name','Distance','Mass','Radius','Luminosity']  
 
star_df_1 = pd.DataFrame(star_data, columns=headers)

star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")              
     