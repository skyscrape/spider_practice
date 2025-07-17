import requests
import execjs

js_compile  = execjs.compile(open("index.js", encoding="utf-8").read())

class shanbei:
    def __init__(self):
        self.headers = {

            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",

        }
        self.cookies = {
            "auth_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzA1NjY1NzUsImV4cCI6MTc2MDQxMjU0OCwiZXhwX3YyIjoxNzYwNDEyNTQ4LCJkZXZpY2UiOiIiLCJ1c2VybmFtZSI6ImV5ZXdpdG5lc3NmYXVsIiwiaXNfc3RhZmYiOjAsInNlc3Npb25faWQiOiI3MTQ1OWE3NDYwOTIxMWYwYTYwMjcyMDVkMTVkYzZjZSJ9.ZRv4jV35ogEaI3a3XokKlW2qspxYS9GgmwPmxFc2tTY"
        }
        self.url = "https://apiv3.shanbay.com/wordscollection/learning/words/unlearned_items"
        self.params = {
            "page": "56",
            "order": "DESC",
            "ipp": "10"
        }
    def get_data(self):
        response = requests.get(url=self.url, params=self.params, headers=self.headers, cookies=self.cookies)
        data = response.json()['data']
        data = self.parse_data(data)
        print(data)
    def parse_data(self, data):
        return js_compile.call("parse_data", data)

if __name__ == '__main__':
    shanbei().get_data()