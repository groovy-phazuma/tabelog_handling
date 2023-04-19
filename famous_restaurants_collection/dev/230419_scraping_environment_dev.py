#!/usr/bin/env python3
"""
Created on 2023-04-19 (Wed) 23:35:49

Scraping environment development.

@author: I.Azuma
"""
#%%
import chromedriver_binary
from selenium import webdriver

#%%
# Top 100 Tokyo ramen restaurants 2022
url = 'https://award.tabelog.com/hyakumeiten/ramen_tokyo'

# launch
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)