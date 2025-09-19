import requests
import json
import execjs


class XiniuData:
    def __init__(self):

        self.headers = {
            "accept": "application/json",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "origin": "https://www.xiniudata.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://www.xiniudata.com/industry/newest?from=data",
            "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
        }
        self.cookies = {
            # "username": "skyscrape2",

        }

        self.url = "https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort"

        self.data = {
            "payload": "LBc3V0I6ZGB5bXsxTCQnPRBuBAQVcDhbICcmb2x3AjI=",
            "sig": "CE704F132C4E47B31E91773020275904",
            "v": 1
        }
        # self.data = json.dumps(self.data, separators=(',', ':'))
        self.js_compile = execjs.compile(open("index.js", "r", encoding="utf-8").read())

    def get_data(self):

        process_data = json.loads(self.js_compile.call("get_data", 40))
        # print(process_data)
        self.data["payload"] = process_data["payload"]
        self.data["sig"] = process_data["sign"]
        str_data = json.dumps(self.data, separators=(',', ':'))
        # print(self.data)
        response = requests.post(url=self.url, data=str_data, headers=self.headers, cookies=self.cookies)
        print(self.parse_data(response.json()['d']))

    def parse_data(self, data):
        final_data = self.js_compile.call("d1", data)
        return final_data

if __name__ == '__main__':
    xiniu = XiniuData()
    xiniu.get_data()