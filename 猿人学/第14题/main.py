import requests
import execjs

class YRX14:
    def __init__(self):
        self.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        }
        self.cookies = {
            "sessionid": "adkbveoxngd1m3omxhk3f5z0rnfrf8bo"
        }
        self.url = "https://www.python-spider.com/api/challenge14"
        self.data = {
            "page": "2",
            "uc": "5vCGTsFWoUvTKhvdK22PUA=="
        }
    def get_data(self):
        js_compile = execjs.compile(open("index.js", encoding="utf-8").read())
        sum = 0
        for i in range(1, 101):
            self.data["page"] = i
            uc = js_compile.call("get_data", self.data["page"])
            self.data["uc"] = uc
            response = requests.post(self.url, headers=self.headers, cookies=self.cookies, data=self.data).json()
            datalist = response["data"]
            for data in datalist:
                sum += int(data["value"])
            print('sum:::', sum, 'datalist:::', datalist, 'page:::', i)



if __name__ == '__main__':
    yrx14 = YRX14()
    print(yrx14.get_data())