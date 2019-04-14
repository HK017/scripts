import requests
from lxml import etree
import time
import pymysql
from fake_useragent import UserAgent
ua = UserAgent()

def get_list_page_info(sub_type):
    # 不同的类之间页面的解析可能不一样，程序会报错
    """获取大众点评美食列表页的信息 商家名称，推荐菜，城市"""
    city_name = []
    special_cuisine = []
    host_name = []
    # 抓取的城市列表,注意 city获取的是拼音，如果要处理的话手动改一下就行
    city_list = ['shanghai','beijing']

    for city in city_list:

        page_num = 1       # 可以修改爬取的页数
        for page in range(0, page_num):

            headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Host': 'www.dianping.com',
                'Origin': 'http://www.dianping.com',
                'Referer': 'http://www.dianping.com/{0}/ch10/{1}p{2}'.format(city, sub_type, page),  # 美食 ch10
                'User-Agent': ua.random
            }
            url = 'http://www.dianping.com/{0}/ch10/{1}p{2}'.format(city, sub_type, page)  # 美食 ch10
            print(url)
            html = requests.get(url, headers = headers)
            if html.status_code != 200:
                print('请求返回code不等于200，程序退出')
                exit()

            host_name_temp = etree.HTML(html.text).xpath('//div[@class="tit"]/a[@data-click-name="shop_title_click"]/h4/text()')
            for host in host_name_temp:
                host_name.append(host)
            special_cuisine = []
            str1 = etree.HTML(html.text).xpath('//div[@class="recommend"]/a[1]/text()')
            str2 = etree.HTML(html.text).xpath('//div[@class="recommend"]/a[2]/text()')
            str3 = etree.HTML(html.text).xpath('//div[@class="recommend"]/a[3]/text()')
            for item in zip(str1,str2,str3):
                special_cuisine.append(item)
            city_name.append(city*len(special_cuisine))

            # 一页爬取完毕后停留8-10秒
            print('{0} 的 第[{1}]页爬取完毕！'.format(city, page + 1))
            time.sleep(10)

    return city_name, host_name, special_cuisine


def insert_to_sql(data):
    """参数data是一个列表每一个元素都是一个元组，表示moyan_info表的一行记录"""
    con = pymysql.connect(host='10.10.209.30', user='houkai_test', passwd='zjrqbm4dVG33Mb7oPFdSnTBG4yWD9g', port=3306, db='test')
    cursor = con.cursor()

    # 插入的表需要提前在数据库中建好
    sql = """insert into moyan_info(city_name, host_name, special_cuisine) values(%s, %s, %s)"""
    try:
        cursor.executemany(sql, args = data)
        con.commit()
    except:
        print("插入数据报错！！！")
        con.rollback()
    finally:
        con.close()


if __name__ == '__main__':
    # 抓取的 美食子分类列表（需自己添加，自己重新改代码写循环，和城市一样的循环） 其中 西餐 g116
    sub_type_list = ['g116','g110']
    for sub_type in sub_type_list:
        city_name, host_name, special_cuisine = get_list_page_info(sub_type)
        data = list(zip(city_name, host_name, special_cuisine))
        insert_to_sql(data)