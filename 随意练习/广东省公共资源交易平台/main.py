import requests
import json
import execjs
class GuangDongZiYuan(object):
    def __init__(self):
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": "https://ygp.gdzwfw.gov.cn",
            "Pragma": "no-cache",
            "Referer": "https://ygp.gdzwfw.gov.cn/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
            "X-Dgi-Req-App": "ggzy-portal",
            "X-Dgi-Req-Nonce": "iID84TzTzQEUTJoc",
            "X-Dgi-Req-Signature": "c1df35a9edd84a125c99df9be3b8056161d837c593697ec174e161a365635225",
            "X-Dgi-Req-Timestamp": "1754986387338",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\""
        }
        self.cookies = {
            "_horizon_sid": "66465cbf-21ab-4cc9-be75-c0da80feaef5",
            "_horizon_uid": "03934ed1-66ed-4b35-aa5f-2ba5e3a3cfd0"
        }
        self.url = "https://ygp.gdzwfw.gov.cn/ggzy-portal/search/v2/items"

        self.data = {
            "type": "trading-type",
            "openConvert": False,
            "keyword": "",
            "siteCode": "44",
            "secondType": "A",
            "tradingProcess": "",
            "thirdType": "[]",
            "projectType": "",
            "publishStartTime": "",
            "publishEndTime": "",
            "pageNo": 1,
            "pageSize": 10
        }

    def get_data(self):
        response = requests.post(self.url, headers=self.headers, cookies=self.cookies, data=self.data_str)
        return response.json()
    def get_list(self):
        js_compile = execjs.compile(open("index1.js", "r", encoding="utf-8").read())


        for i in range(1, 3):

            data = json.loads(js_compile.call("get_Data", i))

            # 修改字典
            self.data["pageNo"] = i

            # 每次循环都重新序列化，不覆盖原字典
            self.data_str = json.dumps(self.data, separators=(',', ':'))

            self.headers["X-Dgi-Req-Signature"] = data['Signature']
            self.headers["X-Dgi-Req-Timestamp"] = str(data['Timestamp'])
            self.headers["X-Dgi-Req-Nonce"] = data['Nonce']
            print(self.get_data())


if __name__ == "__main__":
    gdzzy = GuangDongZiYuan()
    data = gdzzy.get_list()
    # print(data)