import pandas as pd
import os
from datetime import timedelta

os.chdir(r'C:\Users\yhouse\Desktop')
data = pd.read_csv('model.csv', encoding='utf8')
data['num'] = 1
m = len(data)
data['dt'] = pd.to_datetime(data['dt'])

for _, sub_dataframe in data.groupby(['user_info_id']):
    sub_m = len(sub_dataframe)
    if sub_m == 1:
        continue
    else:
        for j in sub_dataframe.index.tolist()[1:]:
            if data.ix[j, 'dt'] - data.ix[j - 1, 'dt'] == timedelta(days=1):
                data.ix[j, 'num'] += data.ix[j-1, 'num']

d = data.groupby(['user_info_id'])['num'].agg(['max', 'count'])


d.to_excel('model1111111.xlsx')