#!/usr/bin/env python3
"""
Created on 2023-04-19 (Wed) 23:35:49

Scraping environment development.

@author: I.Azuma
"""
#%%
import time
import pandas as pd
from tqdm import tqdm
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#%%
# Top 100 Tokyo ramen restaurants 2022
url = 'https://award.tabelog.com/hyakumeiten/ramen_tokyo/2022?pref=tokyo'

# launch
options = Options()
# FIXME: hide
# options.add_argument('--headless') 
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)

#%%
def search(href):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(href)
    time.sleep(1)
    
    # store name
    name = driver.find_elements_by_class_name('display-name')[0].text

    # nearest station
    area = driver.find_elements_by_class_name('linktree__parent-target-text')[0].text

    # score
    score = driver.find_elements_by_class_name('rdheader-rating__score-val-dtl')[0].text
    
    driver.close()
    
    return name,area,score

#%%
# store names
name_obj = driver.find_elements_by_class_name('hyakumeiten-shop__name')
name_list = [t.text for t in list(name_obj)]

# collect each store data
t = driver.find_elements_by_xpath("//a[contains(@href,'tabelog.com/tokyo/')]")

N = []
A = []
S = []
U = []

for i in tqdm(range(len(t))):
    target = t[i].get_attribute("href")
    U.append(target)
    name, area, score = search(target)
    N.append(name)
    A.append(area)
    S.append(score)

df = pd.DataFrame({'店舗名':N,'最寄り':A,'評価':S,'URL':U})

# sort by score
df = df.sort_values('評価',ascending=False)
df.to_csv('C:/github/tabelog_handling/famous_restaurants_collection/results/2022_Tokyo_ramen_top_100.csv',index=False,encoding='utf_8_sig')

#%% output
import datetime
dt_now = datetime.datetime.now()
print(dt_now.isoformat())
"""
2023-04-24T22:45:38.370781
"""