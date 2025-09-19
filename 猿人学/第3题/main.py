import subprocess
import re
import requests




class YRX3:
    def __init__(self):
        self.cookies = {
            "sessionid": "n096lfi8ft9lrzioon334rjcj2u58fat",
            "m": "",
        }
        self.url = "https://www.python-spider.com/api/challenge3"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        }
        self.data = {
            "page": "1"
        }
    def get_cookies(self):
        result = subprocess.run(
            ["node", "source.js"],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    def get_data(self):
        sum = 0
        for i in range(1, 101):
            self.data["page"] = str(i)
            result = self.get_cookies()
            m = re.findall(r"mundefined=(.*?);", result)[0]
            self.cookies["m"] = m
            response = requests.post(url=self.url, headers=self.headers, cookies=self.cookies, data=self.data).json()
            dataList = response["data"]
            for data in dataList:
                sum += int(data["value"])
            print('sum:::', sum, 'datalist:::', dataList, 'page:::', i)



if __name__ == '__main__':
    y = YRX3()
    y.get_data()
