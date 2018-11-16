from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.keys import Keys
import re
from lxml import etree
import pymysql
import time
import sys
import random

chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度

# 启动浏览器，获取网页源代码
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
wait = WebDriverWait(browser,10)





def get_cookie_isg():

    try:
        start_time = time.time()
        browser.get('https://www.amap.com/')
        cookie_list = browser.get_cookies()
        end_time = time.time()
        print('获取一个cookie的时间为{}s'.format(end_time - start_time))
        print(cookie_list)
        for item in cookie_list:
            if item["name"] == 'guid':
                guid = item["value"]
            if item["name"] == 'isg':
                isg = item["value"]
                break
        return guid, isg
    except  TimeoutException as e:
        print('获取cookie错误',e)

if __name__ == '__main__':
    guid, isg =  get_cookie_isg()
    print(guid, isg)
