# 整体思路
# 1.从主页输入关键字进行查询,获取最大页数
# 2.清空输入框，输入页码，点击查询
# 3.解析网页，插入数据，停留几秒
# 4.翻页，跳转到第2步，直至最大页数
#总结
#判断当前页面下方的高亮的页码是否为我们请求的页码
#如果网页一直在原地加载，就是翻页出现问题,即next_page函数有问题,追查即可


#D:\Anaconda\lib\site-packages\pymysql\cursors.py:170: Warning: (1265,"Data truncated for column 'title' at row 5")
#  result = self._query(query)
# 字段类型有问题
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





def search(word):
    try:
        browser.get('http://www.taobao.com/')
        input = wait.until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="q"]'))
        )
        submit =wait.until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="J_TSearchForm"]/div[1]/button'))
        )
        input.send_keys(word)
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="mainsrp-pager"]/div/div/div/div[1]')))
        total = int(re.findall('\d+',total.text)[0])
        return total
    except  TimeoutException:
        return search(word)

def next_page(page_number):
    '''完成翻页'''
    try:
        #输入页码的框是否加载出现
        input = wait.until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="mainsrp-pager"]/div/div/div/div[2]/input'))
        )
        #确定按钮可以点击
        submit =wait.until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="mainsrp-pager"]/div/div/div/div[2]/span[3]'))
        )
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.XPATH,'//li[@class="item active"]/span'),str(page_number))
        )
    except TimeoutException:
        return next_page(page_number)

def paser_html():
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="mainsrp-itemlist"]')))
    html = browser.page_source
    title = etree.HTML(html).xpath('//img[@class="J_ItemPic img"]/@alt')
    print("title length =", len(title[0]))
    # title = []
    # for index in title_list:
    #     if index.strip() != '':
    #         title.append(index.strip())
    pay_num = etree.HTML(html).xpath('//div[@class="deal-cnt"]/text()')
    price1 = etree.HTML(html).xpath('//div[@class="price g_price g_price-highlight"]/span/text()')
    price2 = etree.HTML(html).xpath('//div[@class="price g_price g_price-highlight"]/strong/text()')
    price = []
    for x,y in zip(price1,price2):
        temp = x + y
        price.append(temp)
    data = []
    if len(title) == len(pay_num) == len(price):
        print('解析成功')
    else:
        print('解析失败')
        print(title,pay_num,price)
        sys.exit()
    for i in range(len(title)):
        temp = (title[i],pay_num[i],price[i])
        print(temp)
        data.append(temp)

    return data

def get_connection():
    return pymysql.connect(host ='10.10.209.30', user = 'houkai_test', passwd = 'zjrqbm4dVG33Mb7oPFdSnTBG4yWD9g', port = 3306, db = 'test')

def check_connect():
    global  conn
    try:
        conn.ping()
    except:
        conn = get_connection()
    # assert conn.ping() is None,'数据库已断开链接'

def write_to_sql(data):
    check_connect()
    cursor = conn.cursor()
    print('连接库连接正常')
    # 如果出现逐渐或者唯一键重复，则不插入该条记录
    sql = 'insert ignore into taobao_food(title,pay_num,price) values(%s,%s,%s)'
    cursor.executemany(sql,args = data)
    conn.commit()
    print('插入成功！')
    cursor.close()


def main(page_number):
    next_page(page_number)
    # print('第{}页'.format(page_number))
    data = paser_html()
    # print("=============================")
    # print(data)
    # print("=============================")
    print('第{}页解析完成'.format(page_number))
    write_to_sql(data)
    print('第{}页插入成功！'.format(page_number))


if __name__ == '__main__':
    try:
        word = input('请输入关键字：')
        total = search(word)
        print(type(total))
        conn = get_connection()
        for page_number in range(2,total+1):
            main(page_number)
            a = random.randint(1,6)
            time.sleep(a)
    finally:
        browser.close()
        conn.close()


