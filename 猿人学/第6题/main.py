from requests import session




class YRX6:
    def __init__(self):
        self.data = {
            "page": "1"
        }
        self.cookies = {
            "sessionid": "n096lfi8ft9lrzioon334rjcj2u58fat",
            "sign": "oahginvmzj"
        }
        self.url = "https://www.python-spider.com/api/challenge6"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        }
        self.s = session()
    def get_data(self):
        sum = 0
        # for i in range(1, 50):
        #     self.data["page"] = str(i)
        #     res = session().post(url=self.url, data=self.data, cookies=self.cookies, headers=self.headers).json()
        #     datalist = res["data"]
        #     for data in datalist:
        #         sum += int(data["value"])
        #     print('sum:::', sum, 'data:::', datalist, 'page:::', i)
        for i in range(50,51):
            self.s.headers.clear()
            self.s.headers.update(headers)
            self.data["page"] = str(i)
            res = session().post(url=self.url, data=self.data, cookies=self.cookies, headers=self.headers).json()
            datalist = res["data"]
            for data in datalist:
                sum += int(data["value"])
            print('sum:::', sum, 'data:::', datalist, 'page:::', i)



if __name__ == '__main__':
    YRX6().get_data()