# -*- coding: utf-8 -*-
import sys
import time

import requests
from pyquery import PyQuery

import ua


def get_city_map():
    city_url = 'http://www.dianping.com/citylist'

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.dianping.com',
        'Referer': 'http://www.dianping.com/shanghai/ch0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': ua.get_user_agent(),
    }
    resp = requests.get(city_url, headers=headers, timeout=6.3)
    if resp.status_code != 200:
        print('city list code:', resp.status_code)
        return None

    content = PyQuery(resp.text)
    cities = content('.main-citylist a')
    city_map = {city.text: PyQuery(city).attr('href').split('/')[-1] for city in cities}

    return city_map


def get_food_list(city, selector='', start_page=1, end_page=1):
    hosts = []

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Cache-Control': 'max-age=0',
        'Proxy-Connection': 'keep-alive',
        'Host': 'www.dianping.com',
        'Upgrade-Insecure-Requests': '1',
    }

    base_url = 'http://www.dianping.com/{city}/ch10/{selector}p{page}'
    for i in range(start_page, end_page + 1):
        list_url = base_url.format(city=city, selector=selector, page=i)
        headers['User-Agent'] = ua.get_user_agent()
        resp = requests.get(list_url, headers=headers, timeout=6.3)
        if resp.status_code != 200:
            print('host list', resp.status_code, list_url)
            continue
        if not resp.text:
            print('response is empty')
            continue

        content = PyQuery(resp.text)
        labels = content('#shop-all-list ul li div.txt')
        labels = [PyQuery(label) for label in labels]
        for label in labels:
            title = label('div.tit a:nth-child(1)').attr('title')
            host_url = label('div.tit a:nth-child(1)').attr('href')
            star = label('div.comment span').attr('title')
            mean_price = label('div.comment a.mean-price b').text().strip()
            district = label('div.tag-addr a:nth-child(3) span').text().strip()
            addr = label('div.tag-addr span.addr').text().strip()
            recommend = label('div.recommend a').text().strip()

            hosts.append((title, host_url, star, mean_price, district, addr, recommend))

        time.sleep(20)

    return hosts
