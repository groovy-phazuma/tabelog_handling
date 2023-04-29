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