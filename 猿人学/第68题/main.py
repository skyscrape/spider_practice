import requests
import execjs






class YRX68:
    def __init__(self):
        self.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        }
        self.cookies = {
            "sessionid": "n096lfi8ft9lrzioon334rjcj2u58fat"
        }
        self.url = "https://www.python-spider.com/api/challenge68"


    def get_data(self, data, page):
        data['page'] = str(page)
        response = requests.post(self.url, headers=self.headers, cookies=self.cookies, data=data)
        return response.json()['data']

    def get_predata(self, page):
        response = requests.post(self.url, headers=self.headers, cookies=self.cookies)
        data = response.json()
        js_compile = execjs.compile(open('index.js').read())
        data_a = js_compile.call('get_a', data['r'], data['c'])
        data['a'] = data_a
        return self.get_data(data, page)

    def get_list(self):
        sum = 0
        for i in range(1, 101):
            dataList = self.get_predata(i)
            for data in dataList:
                # print(dataList)
                sum += int(data['value'])
            print( 'sum:::', sum, 'datal;ist:::', dataList, 'page:::', i)



if __name__ == '__main__':
    yrx68 = YRX68()
    yrx68.get_list()