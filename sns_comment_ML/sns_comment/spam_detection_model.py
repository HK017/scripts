import pandas as pd
import numpy as np
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from sqlalchemy import create_engine
import datetime
from datetime import date, timedelta
import jieba
import re
# cleaning the text
def textcleansing(col):
    mytext = col.str.lower()
    mytext = mytext.str.replace(r"#.+?#", "")
    mytext = mytext.str.replace('<[^>]+>', '')
    mytext = mytext.str.replace('[^\u4e00-\u9fa5a-zA-Z0-9 ]', '')
    return(mytext)

def textcleansing_str(mytext):
    mytext = mytext.lower()
    mytext = mytext.replace(r"#.+?#", "")
    mytext = mytext.replace('<[^>]+>', '')
    mytext = mytext.replace('[^\u4e00-\u9fa5a-zA-Z0-9 ]', '')
    return(mytext)

def jiebaparsing(col):
    """首先加载自定义词典，然后进行jieba分词，然后返回每一条评论的字典"""
    # 加载自定义词典 file_name为自定义词典的路径
    # 词典格式和dict.txt一样，一个词占一行；每一行分三部分，一部分为词语，另一部分为词频，最后为词性（可省略），用空格隔开
    # jieba.load_userdict("/opt/sns_comment/jieba_dict_new.txt")
    newtext = []
    for doc in textcleansing(col):
        doc = jieba.cut(str(doc), cut_all=False, HMM = True)
        newtext.append(" ".join(doc))
    newtext =  [re.sub("\s+", " ", string) for string in list(map(str.strip, newtext))]
    return(newtext)
    
def rmstopwords(col):
    # with open("/opt/sns_comment/Stopword_cn_new.txt", encoding= 'utf8') as f:
    #     stopwords = set([re.sub("\n", "", string) for string in f.readlines()])
    stopwords = ''
    newtext_stop = []
    for sublist in [[word for word in document.lower().split() if word not in stopwords] for document in jiebaparsing(col)]:
        newtext_stop.append(" ".join(sublist))
    return(newtext_stop)

def rmstopwords_str(mytext):
    # with open("/opt/sns_comment/Stopword_cn_new.txt", encoding= 'utf8') as f:
    #     stopwords = set([re.sub("\n", "", string) for string in f.readlines()])
    stopwords = ''
    mytext_seg = " ".join(jieba.cut(textcleansing_str(mytext), cut_all=False, HMM = True))
    newtext_stop = []
    for sublist in [[word for word in document.lower().split() if word not in stopwords] for document in mytext_seg]:
        newtext_stop.append(" ".join(sublist))
    newtext = (' '.join(newtext_stop)).replace(" ", "")
    newtext_seg = " ".join(jieba.cut(newtext, cut_all=False, HMM = True))
    return([newtext_seg])
    
#engine_sns = create_engine('mysql+mysqldb://sns_data:mulQMh6CwSL6lKw2@localhost:3309/sns', connect_args={'charset':'utf8'})
engine_sns = create_engine('mysql+mysqldb://sns_data:mulQMh6CwSL6lKw2@10.10.38.201:3306/sns', connect_args={'charset':'utf8'})


sns_comment =  pd.read_sql_query("""select content, status is_spam from sns_user_share_comment 
where length(content) >10
and operator in (0, 1)
and date(create_time) <= %(ystday)s """, engine_sns, params = {"ystday": (date.today()-timedelta(1)).strftime("%Y-%m-%d")})

train_text = rmstopwords(sns_comment.content)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB())])
print(train_text)
_ = text_clf.fit(train_text, sns_comment.is_spam.tolist())

# a = CountVectorizer()
a = TfidfTransformer()
b = a.fit_transform(["dog cat fish","dog cat cat","fish bird", 'bird'])
# print(type(a.vocabulary_))
# print(a.vocabulary_)

print(type(b))
print(b.todense())
print(b.toarray())

from sklearn.externals import joblib
# joblib.dump(text_clf, "/opt/sns_comment/spam.pkl")

print("model has been succesfully built at {day}".format(day = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))