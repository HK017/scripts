# encoding=utf-8
from datetime import datetime
import json
import requests
import time
import pymysql
import re
from math import radians, cos, sin, asin, sqrt
from get_cookies_by_selenium import get_cookie_isg
# ua = UserAgent()

MYSQL_SETTINGS = {
    'host': '10.10.209.30',
    'port': 3306,
    'user': 'houkai_test',
    'password': 'zjrqbm4dVG33Mb7oPFdSnTBG4yWD9g',
    'database': 'test',
}

COOKIE = 'guid={}; UM_distinctid=166f1a82a60114-06e497025d43f4-44410a2e-1fa400-166f1a82a613dd; cna=ja5qFBrBtjQCAbSamTmUQrQ8; _uab_collina=154165317391165071948971; key=bfe31f4e0fb231d29e1d3ce951e2c780; CNZZDATA1255626299=1388052370-1541648985-https%253A%252F%252Fwww.baidu.com%252F%7C1541752120; x5sec=7b22617365727665723b32223a223332663732613466643936326661383735333333393062303737373265363463435033416c643846454f6a2b734a574c765966523267453d227d; isg=%s'.format(get_cookie_isg()[0], get_cookie_isg()[1])

keyword_list = [
    '西餐',
    '日料',
    '川菜',
    '韩国料理',
    '本帮菜',
    '意大利菜',
    '火锅',
    '海鲜',
    '自助餐',
    '酒吧',
    '创意菜',
    '融合菜',
    '粤菜',
    '咖啡厅'
]

cities = {
    '上海': ('310000', '121.105093|31.05873|122.271264|31.426729'),
    '北京': ('110000', '116.295415|39.609909|116.954608|40.219779'),
    '广州': ('440100', '113.170767|22.771717|113.82996|23.5029'),
    '深圳': ('440300', '113.976077|22.192045|114.63527|22.926343'),
    '西安': ('610100', '108.838154|33.945335|109.497347|34.602401'),
    '成都': ('510100', '103.995462|30.522917|104.325067|30.864798'),
    '天津': ('120000', '117.131299|38.925722|117.460904|39.234349'),
    '杭州': ('330100', '120.162909|30.159115|120.492514|30.502275'),
    '南京': ('320100', '118.657543|31.715599|119.316736|32.389528'),
    '石家庄': ('130100', '114.392591|37.742568|115.051784|38.368669'),
    '沈阳': ('210100', '123.319226|41.50997|123.978419|42.102668'),
    '大连': ('210200', '121.508752|38.615302|122.167945|39.233898'),
    '武汉': ('420100', '114.188702|30.253352|114.847895|30.937793'),
    '重庆': ('500000', '106.395092|29.198637|107.054285|29.890386'),
    '苏州': ('320500', '120.509715|30.970831|121.168908|31.650169')
}


def request_amap_poi_info(payload, referer):
    url = 'https://www.amap.com/service/poiInfo'

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': COOKIE,
        'Host': 'www.amap.com',
        'Referer': referer,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    resp = requests.get(url, headers=headers, params=payload)
    if resp.status_code != 200:
        return None

    try:
        data = json.loads(resp.text)
        poi_list = data.get('data').get('poi_list')
    except Exception as e:
        print(e)
        return None
    return poi_list


def get_starbucks_info(city_info):
    """ get starbucks info from amap by city."""
    print('=='*100)
    print(city_info[0] + '的星巴克店开始爬取')

    starbucks_data = []

    payload = {
        "query_type": "TQUERY",
        "pagesize": "20",
        "qii": "true",
        "cluster_state": "5",
        "need_utd": "true",
        "utd_sceneid": "1000",
        "div": "PC1000",
        "addr_poi_merge": "true",
        "is_classify": "true",
        "zoom": "12",
        "city": city_info[1][0],
        "geoobj": city_info[1][1],
        "keywords": "星巴克",
    }

    for page_num in range(1, 100):
        payload['pagenum'] = page_num
        poi_list = request_amap_poi_info(payload, 'https://www.amap.com/')

        if not poi_list:
            print('request starbucks list exit with %s' % page_num)
            break

        for poi in poi_list:
            data = {
                'amap_key': poi.get('id'),
                'name': poi.get('name'),
                'city': poi.get('cityname'),
                'longitude': poi.get('longitude'),
                'latitude': poi.get('latitude'),
                'address': poi.get('address'),
                'tel': poi.get('tel'),
            }
            starbucks_data.append(data)
        print('【%s】的星巴克列表的第【%s】页已爬取完毕'% (city_info[0], page_num))
    print('【%s】的星巴克全部爬取完毕' % city_info[0])
    print('==' * 100)
    return starbucks_data


def get_host_info(search_keyword, starbucks_data, city_info):
    """ get host info nearby starbucks from amap by searching keyword."""
    host_data = []

    payload = {
        "query_type": "RQBXY",
        "pagesize": "20",
        "pagenum": '',
        "qii": "true",
        "cluster_state": "5",
        "need_utd": "true",
        "utd_sceneid": "1000",
        "div": "PC1000",
        "addr_poi_merge": "true",
        "is_classify": "true",
        "zoom": "14",
        "longitude": starbucks_data['longitude'],
        "latitude": starbucks_data['latitude'],
        "range": "1000",
        "city": city_info[1][0],
        "keywords": search_keyword,
    }

    for page_num in range(1, 3):
        payload['pagenum'] = page_num
        poi_list = request_amap_poi_info(payload, 'https://www.amap.com/place/' + starbucks_data['amap_key'])

        if not poi_list:
            print('request host list fail with %s' % page_num)
            continue

        for poi in poi_list:
            if not (poi.get('longitude', '') or poi.get('latitude', '') or starbucks_data['longitude'] or starbucks_data['latitude']):
                distance = None
            else:
                distance = geo_distance(poi.get('longitude', ''), poi.get('latitude', ''),starbucks_data['longitude'], starbucks_data['latitude'])

            data = {
                'starbucks_key': starbucks_data['amap_key'],
                'keyword': search_keyword,
                'city': poi.get('cityname'),
                'name': poi.get('name'),
                'longitude': poi.get('longitude'),
                'latitude': poi.get('latitude'),
                'address': poi.get('address'),
                'tel': poi.get('tel'),
                'mean_price': '',
                'distance': distance
            }
            domain_list = poi.get('domain_list')
            for domain in domain_list:
                if domain.get('name', '') == 'price':
                    price_raw = domain.get('value', '')
                    # price_raw = "<font color='#90969a'>人均:</font><font color='#f84b57'>￥</font><font color='#f84b57'>114</font>"
                    try:
                        data['mean_price'] = re.findall('<.*>人均:<.*>￥<.*>([0-9]+)</font>', price_raw)[0]
                    except:
                        data['mean_price'] = None
                    break
            host_data.append(data)

        print('【%s】的【%s】的周边的【%s】菜系,第【%d】页爬取完毕' % (city_info[1], starbucks_data['name'], search_keyword, page_num))
    return host_data


def save2mysql(table_name, data_list):
    query_base = "insert into %s" % table_name
    conn = pymysql.Connect(**MYSQL_SETTINGS)
    with conn.cursor() as cur:
        for data in data_list:
            column = '(' + ','.join(data.keys()) + ')'
            value = 'values (' + ','.join(['%(' + k + ')s' for k in data.keys()]) + ')'
            query = ' '.join([query_base, column, value])
            cur.execute(query, data)
    conn.commit()
    conn.close()


def geo_distance(lng1, lat1, lng2, lat2):
    # 计算两点间距离-m
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    dis = round(2 * asin(sqrt(a)) * 6371 * 1000)
    return dis


def main():
    for city in cities.items():
        starbucks_info_list = get_starbucks_info(city)
        save2mysql('starbucks_amap_info', starbucks_info_list)
        print('【%s】的星巴克店铺信息全部插入完毕！！！' % city[0])
        for starbucks_info in starbucks_info_list:
            for keyword in keyword_list:
                host_info_list = get_host_info(keyword, starbucks_info, city)
                save2mysql('starbucks_host_info', host_info_list)
            print('【%s】的【%s】所有菜系爬取完毕' % (starbucks_info['city'], starbucks_info['name']))


if __name__ == '__main__':
    main()
