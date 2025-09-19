import execjs
import requests

class caiZhaoNet :
    def __init__(self):
        self.headers = {
            "accept": "text/plain, */*; q=0.01",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://search.bidcenter.com.cn",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://search.bidcenter.com.cn/",
            "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
        }
        self.url = "https://interface.bidcenter.com.cn/search/GetSearchProHandler.ashx"
        self.data = {
            "from": "6137",
            "guid": "ed500ccb-0a9e-42bd-90c3-6699de853da2",
            "location": "6138",
            "token": "",
            "next_token": "",
            "keywords": "%E8%B6%85%E5%A3%B0%E5%88%80",
            "mod": "0"
        }
        self.index_obj = execjs.compile(open("index.js").read())
    def get_data(self):
        response = requests.post(self.url, headers=self.headers, data=self.data)
        res = response.text
        real_data = self.index_obj.call("get_data", res)
        print(real_data)


if __name__ == '__main__':
    cz = caiZhaoNet()
    cz.get_data()
