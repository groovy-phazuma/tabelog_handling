#!/usr/bin/env python3
"""
Created on 2023-05-07 (Sun) 23:13:40

Review preprocessing

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
ramen_df = pd.read_csv('C:/github/tabelog_handling/famous_restaurants_collection/results/2022_Tokyo_ramen_top_100.csv',index_col=0)
url = ramen_df['URL'].tolist()[0]

#%%
# launch
options = Options()
# FIXME: hide
# options.add_argument('--headless') 
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)

#%%
info = driver.find_elements_by_class_name('mainnavi')
"""
トップ、メニュー・コース、写真、口コミ、地図
"""
info[3].click()
time.sleep(3)

#%%
target = "lunch"
target_list = ["all","dinner","lunch"]
# choose review range
lunch_review = driver.find_elements_by_class_name('rvwsort-change__tab')
lunch_review[target_list.index(target)].click()
time.sleep(3)