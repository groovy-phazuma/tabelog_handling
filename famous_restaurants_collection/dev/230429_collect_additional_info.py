#!/usr/bin/env python3
"""
Created on 2023-04-29 (Sat) 20:43:13

collect additional information

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
href = 'https://tabelog.com/tokyo/A1303/A130302/13229964/'

options = Options()
driver = webdriver.Chrome(options=options)
driver.get(href)
time.sleep(1)

# store name
name = driver.find_elements_by_class_name('display-name')[0].text
# nearest station
area = driver.find_elements_by_class_name('linktree__parent-target-text')[0].text
# score
score = driver.find_elements_by_class_name('rdheader-rating__score-val-dtl')[0].text

#%%
# price
dinner_price = driver.find_elements_by_class_name('rdheader-budget__price-target')[0].text
lunch_price = driver.find_elements_by_class_name('rdheader-budget__price-target')[1].text

# driver.close()
# %%
