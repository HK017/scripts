import pandas as pd
from datetime import timedelta

"""
# 先得到统计值
SELECT  
a.user_info_id,
DATE(a.pay_time),
COUNT(*)
FROM rd_book.rd_brand_equity_subscribe a 
JOIN rd_book.rd_brand_equity b on b.id = a.brand_equity_id AND b.equity_name LIKE '星巴克%'
WHERE a.`status` = 1 AND a.pay_time between '2018-12-1 00:00:00' AND '2018-12-31 23:59:59'
GROUP BY a.user_info_id,DATE(a.pay_time)
ORDER BY a.user_info_id,DATE(a.pay_time);
"""


data = pd.read_excel(r'C:\Users\yhouse\Desktop\demo.xlsx')
data['num'] = 1
data['dt'] = pd.to_datetime(data['dt'])


for index, dataframe in data.groupby('id'):
    if len(dataframe) == 1:
        continue
    else:
        for i in dataframe.index[:-1]:
            if (dataframe.ix[i+1,'dt'] - dataframe.ix[i,'dt']) == timedelta(1):
                data.ix[i + 1, 'num'] = data.ix[i, 'num'] + data.ix[i + 1, 'num']
            else:
                continue

result = data.groupby('id')['num'].max().reset_index()
result.to_csv(r'C:\Users\yhouse\Desktop\result.csv')