import json
import pymysql

file_path = r'C:\Users\yhouse\Desktop\starbucks.json'

def get_info(file_path):
    """读取json文件并解析"""

    # 存放字段的列表
    city = []
    name = []
    id = []
    postalCode = []
    streetAddressLine1 = []
    streetAddressLine2 = []
    streetAddressLine3 = []
    latitude = []
    longitude = []

    with open(file_path, 'r', encoding='utf-8') as f:
        file = json.load(f)

    lists = file['data']

    for temp in lists:
        id.append(temp.get('id', ''))
        name.append(temp.get('name', ''))
        city.append(temp['address'].get('city',''))
        streetAddressLine1.append(temp['address'].get('streetAddressLine1',''))
        streetAddressLine2.append(temp['address'].get('streetAddressLine2',''))
        streetAddressLine3.append(temp['address'].get('streetAddressLine3',''))
        postalCode.append(temp['address'].get('postalCode',''))
        latitude.append(temp['coordinates'].get('latitude', ''))
        longitude.append(temp['coordinates'].get('longitude', ''))



    return id, name ,city, postalCode, streetAddressLine1, streetAddressLine2, streetAddressLine3, latitude, longitude


def db_conn(data_list):
    con = pymysql.connect(host='10.10.209.30', user='houkai_test', passwd='zjrqbm4dVG33Mb7oPFdSnTBG4yWD9g', port=3306, db='test')
    cursor = con.cursor()

    sql = """insert into parse_starbucks(id, name ,city, postalCode, streetAddressLine1, streetAddressLine2, streetAddressLine3, latitude, longitude) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.executemany(sql, args=data_list)

    con.commit()
    con.close()

if __name__ == '__main__':
    id, name, city, postalCode, streetAddressLine1, streetAddressLine2, streetAddressLine3, latitude, longitude = get_info(file_path)
    data = list(zip(id, name ,city, postalCode, streetAddressLine1, streetAddressLine2, streetAddressLine3, latitude, longitude))
    db_conn(data)