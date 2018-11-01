import json
import pymysql

file_path = r'C:\Users\yhouse\Desktop\city.json'

def get_info(file_path):
    """读取json文件并解析"""

    # 存放字段的列表
    CityLongName_CN_list = []
    CityName_CN_list = []
    CityLongName_list = []
    CityName_list = []
    CityCode_list = []
    CountryCode_list = []

    with open(file_path, 'r', encoding='utf-8') as f:
        file = json.load(f)

    lists = file['Success']['Cities']

    for temp in lists:
        CityLongName_CN_list.append(temp.get('CityLongName_CN',''))
        CityName_CN_list.append(temp.get('CityName_CN',''))
        CityLongName_list.append(temp.get('CityLongName',''))
        CityName_list.append(temp.get('CityName',''))
        CityCode_list.append(temp.get('CityCode',''))
        CountryCode_list.append(temp.get('CountryCode',''))

    return CityLongName_CN_list, CityName_CN_list ,CityLongName_list, CityName_list, CityCode_list, CountryCode_list


def db_conn(data_list):
    con = pymysql.connect(host='10.10.209.30', user='houkai_test', passwd='zjrqbm4dVG33Mb7oPFdSnTBG4yWD9g', port=3306, db='test')
    cursor = con.cursor()

    sql = """insert into json_parse(citylongname_cn, cityname_cn ,citylongname, cityname, citycode, countrycode) values (%s, %s, %s, %s, %s, %s)"""
    cursor.executemany(sql, args=data_list)

    con.commit()
    con.close()

if __name__ == '__main__':
    CityLongName_CN, CityName_CN, CityLongName, CityName, CityCode, CountryCode = get_info(file_path)
    data = list(zip(CityLongName_CN, CityName_CN, CityLongName, CityName, CityCode, CountryCode))
    db_conn(data)