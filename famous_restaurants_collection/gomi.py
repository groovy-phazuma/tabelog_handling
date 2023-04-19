from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import csv
import time
import random
import chromedriver_binary

#enter the information
key = '3136383157@utac.u-tokyo.ac.jp'
pw = '********'
location = '薬学系総合研究棟'

# log in
driver = webdriver.Chrome()
driver.get('https://login.microsoftonline.com/common/oauth2/authorize?response_mode=form_post&response_type=id_token+code&scope=openid&msafed=0&nonce=ce7a0248-7d9f-4caa-98d6-bad3cb051127.637355170218564132&state=https%3a%2f%2fforms.office.com%2fPages%2fResponsePage.aspx%3fid%3dT6978HAr10eaAgh1yvlMhF__kSldrNpNvIWhwdsjjRJURUZEVjlIWjM1VjhXMlVaRVJaWVpEVjJZVCQlQCN0PWcu&client_id=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&redirect_uri=https%3a%2f%2fforms.office.com%2fauth%2fsignin')
driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]").send_keys(key)
driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/input").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/div/form/div[2]/div[2]/input").send_keys(pw)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/div/form/div[2]/div[4]/span").click()
driver.find_element_by_xpath("/html/body/div/form/div[1]/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input").click()
time.sleep(3)

# send information
driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[3]/div/div[1]/div/label/input").click()
driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[3]/div/div[1]/div/label/input").click()
driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div[1]/div[3]/div[2]/div[3]/div[2]/div[3]/div/div/div/input").send_keys(location)
driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div[1]/div[3]/div[2]/div[4]/div[2]/div[3]/div/div[1]/div/label/input").click()
driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div[1]/div[3]/div[2]/div[5]/div[2]/div[3]/div/div[2]/div/label/input").click()

# end
driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div[1]/div[3]/div[3]/div/div/button/div").click()
