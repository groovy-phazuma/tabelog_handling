#!/usr/bin/env python3
"""
Created on 2023-05-24 (Wed) 23:34:02

Overwrite multi reviews

@author: I.Azuma
"""
#%%
import time
import pandas as pd
from tqdm import tqdm
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.support.select import Select
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
time.sleep(10)

#%%
info = driver.find_elements_by_class_name('mainnavi')
"""
トップ、メニュー・コース、写真、口コミ、地図
"""
info[3].click()
time.sleep(5)

#%%
target = "lunch"
target_list = ["all","dinner","lunch"]
# choose review range
lunch_review = driver.find_elements_by_class_name('rvwsort-change__tab')
lunch_review[target_list.index(target)].click()
time.sleep(3)

#%% review number
"""
select/optionタグで構成されるドロップダウン(プルダウン)リストを選択状態にしたり・値を取得する方法
"""
tmp = driver.find_elements_by_id('reload_list_change')[0]
select = Select(tmp)
select.select_by_value('2')

#%%
cur_url = driver.current_url

#%% expand (もっと見る)
for i in range(3):
    driver.get(cur_url)
    time.sleep(10)
    expand = driver.find_elements_by_xpath("//a [contains(@class, 'rvw-item__showall-trigger js-show-review-items')]")[i].click()
    time.sleep(5)

    tmp = driver.find_elements_by_class_name("rvw-item__review-contents-wrap")[0].text
    review = tmp.split('\n')

    with open('C:/github/tabelog_handling/review_analysis/dev/result/review.txt', mode = "a", encoding="utf_8") as f:
        f.write(tmp)