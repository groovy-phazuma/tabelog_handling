# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 16:00:46 2020

target data : 2020 Tokyo rahmen 100 famouse restaurants

@author: I.Azuma
"""
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import chromedriver_binary
from tqdm import tqdm
import pandas as pd
import time

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

#-----------------------------------------------------------------------------#
# 2020 Tokyo
url = 'https://award.tabelog.com/hyakumeiten/ramen_tokyo'

# launch
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)

# sort by score ranking
driver.find_elements_by_class_name('js-search-trigger')[1].click()

driver.find_elements_by_xpath("//a[contains(@href,'sort=ranking')]")[0].click()
time.sleep(1)

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

R = [i+1 for i in range(100)]

df = pd.DataFrame({'ランキング':R,'店舗名':N,'最寄り':A,'評価':S,'URL':U})
df.to_csv('C:/github/tabelog_handling/famous_restaurants_collection/legacy/results/2021_tokyo_rahmen_100_famous_store.csv',index=False,encoding='utf_8_sig')
