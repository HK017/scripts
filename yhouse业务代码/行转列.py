import pandas as pd
import numpy as np

data = pd.read_excel(r'C:\Users\yhouse\Desktop\icon点击统计.xlsx',sheet_name='Sheet2')
data = pd.DataFrame(data)
data = data.iloc[:,:3]
data_new = pd.pivot_table(data=data, index=['日期区间'], columns=['icon名称'], values=['点击去重用户数'])
dt = pd.DataFrame(data_new.reset_index())
dt.to_excel(r'C:\Users\yhouse\Desktop\icon点击统计1.xlsx')

