#!/usr/bin/env python3
"""
Created on 2023-04-27 (Thu) 23:35:20

Collect nationwide information

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
# Top 100 Tokyo Italian restaurants 2022
url = 'https://award.tabelog.com/hyakumeiten'

# launch
options = Options()
# FIXME: hide
# options.add_argument('--headless') 
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)

#%%
info = driver.find_elements_by_class_name('hyakumeiten-nav__item')

# 1. country-wide
cwide = driver.find_elements_by_xpath("//a[contains(@class,'hyakumeiten-nav__item-target js-sitecatalyst-link-track')]")
cwide_url = []
for t in cwide:
    cwide_url.append(t.get_attribute("href"))
time.sleep(3)

# 2. subdivision by region
sdiv_tokyo = driver.find_elements_by_xpath("//a[contains(@class,'hyakumeiten-nav__area-target js-sitecatalyst-link-track hyakumeiten-nav__area-target--tokyo')]")
# Tokyo
tokyo_url = []
for t in sdiv_tokyo:
    tokyo_url.append(t.get_attribute("href"))
time.sleep(3)
# East
sdiv_east = driver.find_elements_by_xpath("//a[contains(@class,'hyakumeiten-nav__area-target js-sitecatalyst-link-track hyakumeiten-nav__area-target--east')]")
east_url = []
for t in sdiv_east:
    east_url.append(t.get_attribute("href"))
time.sleep(3)
# West
sdiv_west = driver.find_elements_by_xpath("//a[contains(@class,'hyakumeiten-nav__area-target js-sitecatalyst-link-track hyakumeiten-nav__area-target--west')]")
west_url = []
for t in sdiv_west:
    west_url.append(t.get_attribute("href"))
time.sleep(3)

#%%
pd.to_pickle(cwide_url,'C:/github/tabelog_handling/famous_restaurants_collection/data/cwide_url_list.pkl')

