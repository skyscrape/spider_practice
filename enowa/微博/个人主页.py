import json
import re

import requests


class WeiboSpider:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }
        self.cookies = {
            "SUB": "_2AkMf2lVZf8NxqwFRmvkSzGPrbI13zAzEieKphqSCJRMxHRl-yj9xqkg-tRB6NFp7tjRN7Z7Z7T6iXbtzyUnIs5pGWIkr1g",
        }
    def create_sub(self):
        data = {
            'cb': 'visitor_gray_callback',
            'tid': '',
            'from': 'weibo',
        }
        response = requests.post('https://passport.weibo.com/visitor/genvisitor2', headers=self.headers, data=data)
        sub = json.loads(re.findall(r'({.*})', response.text)[0])['data']['sub']
        # print(f"生成新的sub : {sub}")
        return sub

    def get_content_dongtai(self, id, url):
        self.cookies['SUB'] = self.create_sub()
        self.headers['referer'] = url
        url = "https://weibo.com/ajax/statuses/show"
        params = {
            "id": id,
            "locale": "zh-CN",
            "isGetLongText": "true"
        }
        response = requests.get(url, headers=self.headers, cookies=self.cookies, params=params, timeout=10)
        print(response.text)
    def get_content_space(self, id):
        self.cookies['SUB'] = self.create_sub()
        self.headers['referer'] ="https://weibo.com/u/{id}".format(id=id)
        url = "https://weibo.com/ajax/statuses/mymblog"
        params = {
            "uid": str(id),
            "page": "1",
            "feature": "0"
        }
        response = requests.get(url, headers=self.headers, cookies=self.cookies, params=params, timeout=10)
        print(response.text)

    def get_content_article(self, url):
        self.cookies['SUB'] = self.create_sub()
        response = requests.get(url, headers=self.headers, cookies=self.cookies, timeout=10)

        print(response.text)

    def process_requests(self, urls):
        for url in urls:
            if re.search(r'/P[a-zA-Z0-9]{8,9}', url):
                print("✅ 动态正文链接:", url)
                id = re.search(r'P[a-zA-Z0-9]{8,9}', url).group()
                print(id)
                self.get_content_dongtai(id, url)
            elif re.search(r'/u/\d{10}', url):
                print("👤 用户主页:", url)
                id = re.search(r'\d{10}', url).group()
                self.get_content_space(id)

            elif re.search(r'/ttarticle/p/show', url):
                print("📰 文章页:", url)
                self.get_content_article(url)
            elif re.search(r'/p/\d+', url):
                print("📰 文章页:", url)
                self.get_content_article(url)
            else:
                print("其他链接", url)
                self.get_content_article(url)



if __name__ == '__main__':
    spider = WeiboSpider()


    urls = [
        "https://www.weibo.com/1911451427/PvSNw8bFF",
        "https://weibo.com/2512851283/PuWL4tihU?s=6cm7D0",
        "https://www.weibo.com/6213974274/PuSJaqcvR?s=6cm7D0",
        "https://www.weibo.com/2400966427/PvWkHaa6",
        "https://www.weibo.com/p/1001603724420437937644",
        "https://www.weibo.com/ttarticle/p/show?id=2309405191879360118969",
        "https://kefu.weibo.com/faqdetail?id=20020",
        "https://weibo.com/u/7989402868?refer_flag=1005050010_"
    ]
    spider.process_requests(urls)

