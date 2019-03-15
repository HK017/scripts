from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_log_error,mean_squared_error
import pandas as pd
import pymysql
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import GradientBoostingRegressor

db = pymysql.connect(host='10.10.206.32', port=3306, user='rigdev', db='tmp_data_yhouse',password='rJ2gWooHqz2B9E@U4KYKJtQ7gB8AfP')
sql = "select * from model_data"
data = pd.read_sql(sql=sql, con=db)


# 处理
data.replace(np.nan, '-1', inplace=True)

label_code = LabelEncoder()
data.ix[:,'first_hexiao_name'] = label_code.fit_transform(data.ix[:,'first_hexiao_name'])
data.ix[:,'first_buy_card_name'] = label_code.fit_transform(data.ix[:,'first_buy_card_name'])

x = data.iloc[:,1:-1]
y = data.iloc[:,-1]
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.3, random_state=0)

model1 = RandomForestRegressor(n_estimators=50, random_state=0, min_samples_leaf=10, min_samples_split=20, verbose=True)
model1.fit(train_x, train_y)
model2 = GradientBoostingRegressor(random_state=0)
model2.fit(train_x, train_y)
# print(model.oob_score_)
pred_test1 = model1.predict(test_x)
pred_train1 = model1.predict(train_x)
pred_train2 = model2.predict(train_x)
pred_test2 = model2.predict(test_x)
# pred1 = [np.floor(i) for i in pred]
# pd.DataFrame(pred_test).to_csv('pred_test.csv')
# pd.DataFrame(test_y).to_csv('test_y.csv')
print(mean_squared_error(test_y, pred_test1))
print(mean_squared_error(train_y, pred_train1))
print(mean_squared_error(test_y, pred_test2))
print(mean_squared_error(train_y, pred_train2))