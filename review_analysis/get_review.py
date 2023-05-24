#!/usr/bin/env python3
"""
Created on 2023-05-22 (Mon) 23:14:03

get comprehensive review

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

from logging import getLogger
logger = getLogger('get_review')

#%%
class GetReview():
    def __init__(self):
        self.url = None
    
    def set_url(self,url:str):
        self.url = url
        logger.info('URL: {}'.format(self.url))
    
    def launch(self):
        # launch
        options = Options()
        # FIXME: hide
        options.add_argument('--headless') 
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        time.sleep(10)

        info = self.driver.find_elements_by_class_name('mainnavi')
        """
        トップ、メニュー・コース、写真、口コミ、地図 in that order
        """
        info[3].click() # select review
        time.sleep(5)

    def get_review(self,target="lunch"):
        target_list = ["all","dinner","lunch"]
        # choose review range
        lunch_review = self.driver.find_elements_by_class_name('rvwsort-change__tab')
        lunch_review[target_list.index(target)].click()
        time.sleep(3)
        # expand the review range
        tmp = self.driver.find_elements_by_id('reload_list_change')[0]
        select = Select(tmp) # select/option tag
        select.select_by_value('2') # 20, 50, 100 in order
        logger.info('target: {}'.format(target))

        # open the hidden text
        expand = self.driver.find_elements_by_xpath("//a [contains(@class, 'rvw-item__showall-trigger js-show-review-items')]")[0].click()
        time.sleep(5)

        # collect info
        self.review = self.driver.find_elements_by_class_name("rvw-item__review-contents-wrap")[0].text
    
    def get_comprehensive(self,target="lunch",n=100,path='C:/github/tabelog_handling/review_analysis/dev/result/review2.txt'):
        target_list = ["all","dinner","lunch"]
        # choose review range
        lunch_review = self.driver.find_elements_by_class_name('rvwsort-change__tab')
        lunch_review[target_list.index(target)].click()
        time.sleep(3)
        # expand the review range
        tmp = self.driver.find_elements_by_id('reload_list_change')[0]
        select = Select(tmp) # select/option tag
        select.select_by_value('2') # 20, 50, 100 in order
        cur_url = self.driver.current_url
        logger.info('target: {}'.format(target))
        tmp = len(list(self.driver.find_elements_by_xpath("//a [contains(@class, 'rvw-item__showall-trigger js-show-review-items')]")))
        logger.info('review_size: {}'.format(tmp))

        for i in range(n):
            self.driver.get(cur_url)
            time.sleep(10)
            # open the hidden text
            expand = self.driver.find_elements_by_xpath("//a [contains(@class, 'rvw-item__showall-trigger js-show-review-items')]")[i].click()
            time.sleep(5)

            tmp = self.driver.find_elements_by_class_name("rvw-item__review-contents-wrap")[0].text
            review = tmp.split('\n')

            with open(path, mode="a", encoding="utf_8") as f:
                f.write(tmp)
    
    def save_review(self,path='C:/github/tabelog_handling/review_analysis/dev/result/review2.txt'):
        with open(path, mode = "w", encoding="utf_8") as f:
            f.write(self.review)

