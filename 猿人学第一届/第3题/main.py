# -*- coding: utf-8 -*-
import json
from collections import Counter

from requests import Session

session = Session()
session.headers = {
    'Content-Length': '0',
    'Accept': '*/*',
    'Referer': 'https://match.yuanrenxue.cn/match/3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cookie': "sessionid="
}

coll = []
for i in range(1, 6):
    url = f"https://match.yuanrenxue.com/api/match/3?page={i}"
    session.post('https://match.yuanrenxue.cn/jssm')
    resp = json.loads(session.get(url).text)
    items = resp['data']
    t = [x['value'] for x in items]
    coll += t
c = Counter(coll)
max_key = max(c, key=c.get)
print("出现频率最高的申请号：", max_key)
