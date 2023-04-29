#!/usr/bin/env python3
"""
Created on 2023-04-29 (Sat) 20:58:55

Collect basic information about 100 famouse restaurants (hyakumeiten).

@author: I.Azuma
"""
import time
import pandas as pd
from tqdm import tqdm
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BasicInfoCollection():
    def __init__(self,url):
        self.url = url
    
    def collect(self):
        # launch
        driver = webdriver.Chrome()
        driver.get(self.url)
        time.sleep(1)

        # collect each store data
        t = driver.find_elements_by_xpath("//a[contains(@href,'tabelog.com/tokyo/')]")

        N = []
        A = []
        S = []
        U = []
        DP = []
        LP = []

        for i in tqdm(range(len(t))):
            target = t[i].get_attribute("href")
            U.append(target)
            name,area,score,dinner_price,lunch_price = search(target)
            N.append(name)
            A.append(area)
            S.append(score)
            DP.append(dinner_price)
            LP.append(lunch_price)
        
        # summarize
        res_df = pd.DataFrame({'店舗名':N,'最寄り':A,'評価':S,'ランチ':LP,'ディナー':DP,'URL':U})

        # sort by score
        self.res_df = res_df.sort_values('評価',ascending=False)

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
    # price
    dinner_price = driver.find_elements_by_class_name('rdheader-budget__price-target')[0].text
    lunch_price = driver.find_elements_by_class_name('rdheader-budget__price-target')[1].text

    driver.close()
    return name,area,score,dinner_price,lunch_price