import  numpy as np

data = np.load(r'E:\yhouse_repo\sns_comment_ML\sns_comment\spam.pkl_07.npy')
print(type(data))
print(data)

from sklearn.externals import joblib
# text_clf = joblib.load(r"E:\yhouse_repo\sns_comment_ML\sns_comment\spam.pkl")
# print(text_clf)