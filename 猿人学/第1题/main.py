import time

import requests
import execjs
data = {
    "page": "1"
}
class YRX1:
    def __init__(self):
        self.url = "https://www.python-spider.com/api/challenge1"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
            "safe": "",
        }
        self.cookies = {
            "sessionid": "n096lfi8ft9lrzioon334rjcj2u58fat"
        }
    def get_data(self, data):
        js_compile = execjs.compile(open("index.js", "r", encoding="utf-8").read())
        self.headers['safe'] = js_compile.call("get_data")
        self.headers['timestamp'] = str(int(time.time()))
        response = requests.post(self.url, headers=self.headers, cookies=self.cookies, data=data)
        return response.json()['data']

if __name__ == '__main__':
    y = YRX1()
    sum = 0
    for i in range(1, 101):
        data["page"] = str(i)
        dataList = y.get_data(data)
        for data in dataList:
            sum += int(data["value"])
        print('sum:::', sum, 'data:::', dataList, 'page:::', i)
