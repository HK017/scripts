import json
import pandas as pd
import numpy as np
import time
import datetime
from datetime import date, timedelta
import jieba
import re
from kafka import KafkaClient, KafkaProducer, KafkaConsumer
from sklearn.externals import joblib


def textcleansing_str(mytext):
    mytext = mytext.lower()
    mytext = mytext.replace(r"#.+?#", "")
    mytext = mytext.replace('<[^>]+>', '')
    mytext = mytext.replace('[^\u4e00-\u9fa5a-zA-Z0-9 ]', '')
    return (mytext)


def rmstopwords_str(mytext):
    with open("/opt/sns_comment/Stopword_cn.txt", encoding='utf8') as f:
        stopwords = set([re.sub("\n", "", string) for string in f.readlines()])
    mytext_seg = " ".join(jieba.cut(textcleansing_str(mytext), cut_all=False, HMM=True))
    newtext_stop = []
    for sublist in [[word for word in document.lower().split() if word not in stopwords] for document in mytext_seg]:
        newtext_stop.append(" ".join(sublist))
    newtext = (' '.join(newtext_stop)).replace(" ", "")
    newtext_seg = " ".join(jieba.cut(newtext, cut_all=False, HMM=True))
    return ([newtext_seg])


consumer = KafkaConsumer("sns_data_comment_topic", group_id='data_group',
                         bootstrap_servers="10.10.233.2:2181,10.10.213.218:2181,10.10.238.166:2181,10.10.233.2:9092,10.10.213.218:9092,10.10.238.166:9092",
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
for message in consumer:
    text_clf = joblib.load("/opt/sns_comment/spam.pkl")
    try:
        # load the msg outter layer
        full_msg = json.loads(json.dumps(message[6], ensure_ascii=False))
        # load the msg inner layer
        sub_msg = json.loads(full_msg['content'])
        # load the text and pass to the model
        text = json.loads(full_msg['content'])['content']
        # spam_status = int(text_clf.predict(rmstopwords_str(text)))
        spam_status = 0 if len(text.encode("utf-8")) <= 10 else int(text_clf.predict(rmstopwords_str(text)))

        # create json inner layer
        new_s_content = {}
        new_s_content["id"], new_s_content["userId"], new_s_content["shareId"], new_s_content["shareType"], \
        new_s_content["parentId"], new_s_content["content"], new_s_content["status"] \
            = sub_msg["id"], sub_msg["userId"], sub_msg["shareId"], sub_msg["shareType"],\
              sub_msg["parentId"], sub_msg["content"], spam_status
        # new_s_content = json.dumps({"id": "{s_id}", "userId": "{s_userId}", "shareId": "{shareId}", "parentId": "{parentId}", "content": "{s_content}", "status": "{spam_status}"}).format(s_id, s_userId, shareId, parentId, s_content, spam_status)
        new_s_content = json.dumps(new_s_content, ensure_ascii=False)

        # create json outter layer
        new_f_content = {}
        new_f_content["msgUID"] = full_msg["msgUID"].split("_", 1)[0] + "_" + str(int(time.mktime(datetime.datetime.now().timetuple())))
        new_f_content["id"], new_f_content["transactionId"], new_f_content["topic"] = full_msg["id"], full_msg["transactionId"], 'sns_user_comment_topic'
        new_f_content["status"], new_f_content["opr"] = full_msg["status"], full_msg["opr"]
        new_f_content["type"], new_f_content["addTime"], new_f_content["from"] = full_msg["type"], str(int(time.mktime(datetime.datetime.now().timetuple()))), '社区评论广告数据'
        new_f_content["content"] = new_s_content
        new_f_content = json.dumps(new_f_content, ensure_ascii=False)
        print("Success @ {today}".format(today=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")), flush=True)
        print(full_msg, flush=True)
        producer = KafkaProducer(bootstrap_servers="10.10.233.2:2181,10.10.213.218:2181,10.10.238.166:2181,10.10.233.2:9092,10.10.213.218:9092,10.10.238.166:9092")
        producer.send("sns_user_comment_topic", bytes(new_f_content, encoding='utf-8'))
    except:
        print("Error @ {today}".format(today=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")), flush=True)
        print(full_msg, flush=True)
        # print(sub_msg)
        # print(new_s_content)