from datetime import datetime
import json
import requests
import time
import pymysql
from fake_useragent import UserAgent
import re

ua = UserAgent()


def get_city_code(*city_tuple):
    """
    从数据库获取城市的编号
    :param city_list:
    :return: 所查城市对应的编号列表
    """
    con = pymysql.connect(host='10.10.209.30', user='houkai_test', passwd='zjrqbm4dVG33Mb7oPFdSnTBG4yWD9g', port=3306, db='test')
    cursor = con.cursor()

    city_code = []
    # 插入的表需要提前在数据库中建好
    sql = 'SELECT adcode FROM city_code WHERE city in %s' % city_tuple

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            city_code.append(row[0])
    except Exception as e:
        print("查询数据异常", e)
        con.rollback()
    finally:
        con.close()
    return city_code


def get_starbucks_info_from_amap(city_code):
    # 获取星巴克的id 和 坐标，作为搜周边商户请求url的参数
    starbucks_info = []
    page = 0
    while True:
        page += 1
        url = 'https://www.amap.com/service/poiInfo'
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'guid=eabb-e594-efdc-43f4; UM_distinctid=166f1a82a60114-06e497025d43f4-44410a2e-1fa400-166f1a82a613dd; cna=ja5qFBrBtjQCAbSamTmUQrQ8; _uab_collina=154165317391165071948971; key=bfe31f4e0fb231d29e1d3ce951e2c780; x5sec=7b22617365727665723b32223a223465613038316165393433376233343666396338346634653165363232333038434b7a526c4e3846454a6a59304b2b573661325a7877453d227d; CNZZDATA1255626299=1388052370-1541648985-https%253A%252F%252Fwww.baidu.com%252F%7C1541741316; isg=BHl5GhuSBo3ra9odTClWzZjAiOWTLmF7yGzVdZuuzqAfIpm049ZxCOd0oGZxmgVw',
            'Host': 'www.amap.com',
            'Referer': 'https://www.amap.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        payload = {
            "query_type": "TQUERY",
            "pagesize": "20",
            "pagenum": page,
            "qii": "true",
            "cluster_state": "5",
            "need_utd": "true",
            "utd_sceneid": "1000",
            "div": "PC1000",
            "addr_poi_merge": "true",
            "is_classify": "true",
            "zoom": "12",
            "city": city_code,
            'geoobj': '121.445178|31.149618|121.609973|31.319589',
            "keywords": "星巴克",
        }

        html = requests.get(url, headers=headers, params=payload)
        # 返回的html是json格式
        obj = json.loads(html.text)
        if obj.get('data', '').get('poi_list', None):
            info_lists = obj['data']['poi_list']
            for per in info_lists:
                data = {
                    'amap_key': per.get('id', ''),
                    'name': per.get('name', ''),
                    'city': per.get('cityname', ''),
                    'longitude': per.get('longitude', ''),
                    'latitude': per.get('latitude', ''),
                    'address': per.get('address', ''),
                    'tel': per.get('tel', ''),
                }
                starbucks_info.append(data)
        else:
            break
    print('=' * 70)
    return starbucks_info


def insert_id(data):
    con = pymysql.connect(host='10.10.209.30', user='houkai_test', passwd='zjrqbm4dVG33Mb7oPFdSnTBG4yWD9g', port=3306,
                          db='test')
    cursor = con.cursor()
    sql = """insert into get_starbucks_id(id, name, address, tel, city_name) values(%s, %s, %s, %s, %s)"""
    try:
        cursor.executemany(sql, args=data)
        con.commit()
        print('*' * 50)
        print('插入完毕！！！')
    except Exception as e:
        print("插入数据报错！！！", e)
        con.rollback()
    finally:
        con.close()


def get_host_info(keyword, starbucks_key, longitude, latitude):
    host_info = []
    for page in range(1, 3):
        url = 'https://www.amap.com/service/poiInfo'
        parameters = {
            "query_type": "RQBXY",
            "pagesize": "20",
            "pagenum": "1",
            "qii": "true",
            "cluster_state": "5",
            "need_utd": "true",
            "utd_sceneid": "1000",
            "div": "PC1000",
            "addr_poi_merge": "true",
            "is_classify": "true",
            "zoom": "14",
            "longitude": longitude,
            "latitude": latitude,
            "range": "1000",
            "city": "310000",
            "keywords": keyword,
        }

        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'guid=eabb-e594-efdc-43f4; UM_distinctid=166f1a82a60114-06e497025d43f4-44410a2e-1fa400-166f1a82a613dd; cna=ja5qFBrBtjQCAbSamTmUQrQ8; _uab_collina=154165317391165071948971; key=bfe31f4e0fb231d29e1d3ce951e2c780; x5sec=7b22617365727665723b32223a223465613038316165393433376233343666396338346634653165363232333038434b7a526c4e3846454a6a59304b2b573661325a7877453d227d; CNZZDATA1255626299=1388052370-1541648985-https%253A%252F%252Fwww.baidu.com%252F%7C1541741316; isg=BHl5GhuSBo3ra9odTClWzZjAiOWTLmF7yGzVdZuuzqAfIpm049ZxCOd0oGZxmgVw',
            'Host': 'www.amap.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://www.amap.com/place/' + str(starbucks_key),

        }

        html = requests.get(url, headers=headers, params=parameters)
        if html.status_code != 200:
            print('请求返回code不等于200，程序退出')
            print('=' * 70)
            continue

        print(html.text)
        json_data = json.loads(html.text)
        if json_data.get('data', '').get('poi_list', None):
            dict_data = json_data['data']['poi_list']

            for per in dict_data:
                data = {
                    'starbucks_key': starbucks_key,
                    'keyword': keyword,
                    'city': per.get('cityname', ''),
                    'name': per.get('name', ''),
                    'longitude': per.get('longitude', ''),
                    'latitude': per.get('latitude', ''),
                    'address': per.get('address', ''),
                    'tel': per.get('tel', ''),
                    'distance': calculate_distance_by_gps((per.get('longitude', ''), per.get('latitude', '')),(longitude, latitude))
                }
                temp = per.get('domain_list', '')
                for x in temp:
                    if x.get('name', '') == 'price':
                        # TODO:正则取价格
                        # 获取到数据类似 "<font color='#90969a'>人均:</font><font color='#f84b57'>￥</font><font color='#f84b57'>114</font>"
                        price_raw = x.get('value', '')
                        reg = re.compile(r'<font.*?</font><font.*?>￥</font><font color=.*?>(.*?)</font>')
                        data['mean_price'] = re.findall(reg, price_raw)[0]
                        break
                host_info.append(data)
        # 每一类每一页爬取完毕用时10s
        time.sleep(5)

    print('=' * 70)
    return host_info


def insert_host_info(host_info):
    """参数data是一个列表每一个元素都是一个元组，表示moyan_info表的一行记录"""
    con = pymysql.connect(host='10.10.209.30', user='houkai_test', passwd='zjrqbm4dVG33Mb7oPFdSnTBG4yWD9g', port=3306, db='test')
    cursor = con.cursor()

    # 插入的表需要提前在数据库中建好
    sql = """insert into starbucks_host_info(starbucks_key, keyword, city, name, mean_price, latitude, longitude, distance) values(%s, %s, %s, %s, %s, %s, %s, %s)"""
    try:
        cursor.executemany(sql, args=host_info)
        con.commit()
    except Exception as e:
        print("插入数据报错！！！", e)
        con.rollback()
    finally:
        con.close()


def insert_starbucks_info(starbucks_info):
    con = pymysql.connect(host='10.10.209.30', user='houkai_test', passwd='zjrqbm4dVG33Mb7oPFdSnTBG4yWD9g', port=3306, db='test')
    cursor = con.cursor()

    amap_key = starbucks_info.get('id', '')
    name = starbucks_info.get('name', '')
    city = starbucks_info.get('cityname', '')
    longitude = starbucks_info.get('longitude', '')
    latitude = starbucks_info.get('latitude', '')
    address = starbucks_info.get('address', '')
    tel = starbucks_info.get('tel', '')

    sql = """insert into starbucks_amap_info(amap_key, name, city, latitude, longitude, tel, address) values(%s, %s, %s, %s, %s, %s, %s)"""
    try:
        cursor.executemany(sql, args=(amap_key, name, city, latitude, longitude, tel, address))
        con.commit()
    except Exception as e:
        print("插入数据报错！！！", e)
        con.rollback()
    finally:
        con.close()


def insert_into_mysql():
    pass


def calculate_distance_by_gps(host_gps, starbuck_gps):
    """
    :param host_gps: type is a tuple (lon, lat)
    :param starbuck_gps: type is a tuple (lon, lat)
    :return: int value and value's is mile
    """
    host_gps[0]


if __name__ == '__main__':
    city_tuple = ('北京市','上海市','广州市','深圳市','西安市','成都市','天津市','杭州市','南京市','石家庄市','沈阳市','大连市','武汉市','重庆市','苏州市')
    city_list = get_city_code(city_tuple)

    keyword_list = ['西餐', '日料', '川菜', '韩国料理', '本帮菜', '意大利菜', '火锅', '海鲜', '自助餐', '酒吧', '创意菜', '融合菜', '粤菜', '咖啡厅']

    for city_code in city_list:
        starbucks_info_list = get_starbucks_info_from_amap(city_code)
        # starbucks_info_list 是一个元组，每个元素是一个字典（即一个星巴克信息）即starbucks_info是一个字典
        for starbucks_info in starbucks_info_list:
            insert_starbucks_info(starbucks_info)

            for keyword in keyword_list:
                # print('开始爬取,星巴克id=【{}】,名称为【{}】,地址为【{}】,其经纬度为【{},{}】,类型为【{}】,'.format(id, name, addresss, longitude,latitude, type))
                host_info_list = get_host_info(keyword, starbucks_info['amap_key'], starbucks_info['longitude'], starbucks_info['latitude'])
                for host_info in host_info_list:
                    insert_host_info(host_info)