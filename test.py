# -*- coding: utf-8 -*-
from ltp_model import *
import pymysql
import time
from pyltp import SentenceSplitter
LTP_DATA_DIR = '/Users/sivber/Desktop/NLP_DATA/ltp_data'
segmentor = get_segmentor(LTP_DATA_DIR)
postagger = get_postagger(LTP_DATA_DIR)
recognizer = get_recognizer(LTP_DATA_DIR)
parser = get_parser(LTP_DATA_DIR)
labeller = get_labeller(LTP_DATA_DIR)


def get_ltp_model(text):
    return LTPModel(text,
                     segmentor,
                     postagger,
                     recognizer,
                     parser,
                     labeller
                     )

conn = pymysql.connect(user='root', passwd='!@#$%^', host='localhost', db='news_dataset', charset="utf8")
cur = conn.cursor()
index = 0
models = []

while True:
    cur.execute("select title from tencent "
                # "where create_time between '2017-7-28 00:00:00' and '2017-7-31 00:00:00' "
                "ORDER BY 'create_time' DESC "
                "LIMIT %d,1" % index
                )
    data = cur.fetchone()
    index += 1
    for t in data:
        if len(t.strip()) > 0:
            models.append(get_ltp_model(t.strip()))
    time.sleep(60)
cur.close()
conn.close()
