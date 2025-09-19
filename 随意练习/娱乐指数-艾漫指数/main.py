import execjs
import requests

class AiMan:
    def __init__(self):
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://www.chinaindex.net/ranklist/4",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "UUID": "1342ec2e-a5be-5256-8016-3bd83081a63d",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
            "funcID": "undefined",
            "incognitoMode": "0",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\""
        }
        self.cookies = {
            # "mobile_iindex_uuid": "1342ec2e-a5be-5256-8016-3bd83081a63d",
        }
        self.url = "https://www.chinaindex.net/iIndexMobileServer/mobile/movie/objectFansRank"

        self.params = {
            "channel": "movielist",
            "sign": "5f3cce6a40c09a221b21104cc98436a3"
        }
    def get_data(self):
        js_compile = execjs.compile(open("index.js", "r", encoding="utf-8").read())
        data = js_compile.call("getSign", str(self.params['channel']))
        self.params['sign'] = data
        response = requests.get(self.url, headers=self.headers, cookies=self.cookies, params=self.params)
        print(response.json())

    def parse_data(self, data):
        pass


if __name__ == '__main__':
    ai = AiMan()
    ai.get_data()