import re
import json
import time
import queue
import requests
import pandas as pd
from selenium import webdriver
from lxml import etree

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Host': 'music.163.com',
    # 'Cookie': 
    'Origin': 'https://music.163.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

def get_user_home(driver, user_id):
    home = 'https://music.163.com/#/user/follows?id=%d'
    user_home = home % user_id
    # r = requests.get(user_home, headers=headers)
    driver.set_page_load_timeout(5)
    start = time.time()
    try:
        driver.get(user_home)
    except Exception:
        pass
    end = time.time()
    frame = driver.find_element_by_xpath('//*[@id="g_iframe"]')
    driver.switch_to.frame(frame)
    user_name = driver.find_element_by_xpath('//*[@id="j-name-wrap"]/span[1]')
    user_level = driver.find_element_by_xpath('//*[@id="j-name-wrap"]/span[3]')
    user_sex = driver.find_element_by_xpath('//*[@id="j-name-wrap"]/i').get_attribute('class')
    if user_sex[-1] == 1:
        user_sex = '男'
    else:
        user_sex = '女'
    user_introduce = driver.find_element_by_xpath('//*[@id="head-box"]/dd/div[2]')
    user_location = driver.find_element_by_xpath('//*[@id="head-box"]/dd/div[3]/span[1]')
    user_age = driver.find_element_by_xpath('//*[@id="age"]/span')
    following_num = driver.find_element_by_xpath('//*[@id="follow_count"]')
    followed_num = driver.find_element_by_xpath('//*[@id="fan_count"]')
    print(end-start)
    return following_num


def get_follows(driver, user_id, following_num=0):
    follow = 'https://music.163.com/#/user/follows?id=%d'
    follow_url = follow % user_id
    follow_ids = {}
    driver.set_page_load_timeout(5)
    start = time.time()
    try:
        driver.get(follow_url)
    except Exception:
        pass
    end = time.time()
    frame = driver.find_element_by_xpath('//*[@id="g_iframe"]')
    driver.switch_to.frame(frame)
    print(end - start)
    following_user = driver.find_elements_by_xpath('//*[@id="main-box"]/li/a')
    pattern = re.compile(r"(?<==)\d+")
    for i in following_user:
        follow_ids += int(pattern.findall(i.get_attribute('href'))[0])
    return follow_ids
user_id = 266097214
driver = webdriver.PhantomJS('D://tools//phantomjs-2.1.1-windows//bin//phantomjs.exe')
# following_num=get_user_home(driver, 266097214)
user_ids = get_follows(driver, user_id)
print(user_ids)