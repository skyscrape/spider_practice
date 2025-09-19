import requests
import execjs

class ScrapyMovie6:
    def __init__(self):
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://spa6.scrape.center/page/2",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\""
        }
        self.url = "https://spa6.scrape.center/api/movie/"
        self.params = {
            "limit": "10",
            "offset": "20",
            "token": "YTYyOGMyYTJlZmUzODFmYzc2NmJmNjY0YmE2OTdmZjAwMGNhMDkyMiwxNzU2MDkwODc3"
        }
        self.execjs_obj = execjs.compile(open("index.js", encoding="utf-8").read())

    def getData(self):
        token = self.execjs_obj.call("getToken")
        self.params["token"] = token
        response = requests.get(self.url, headers=self.headers, params=self.params)
        return response.json()


if __name__ == '__main__':
    movie = ScrapyMovie6()
    data = movie.getData()
    print(data)
