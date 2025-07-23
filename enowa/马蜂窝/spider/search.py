import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.get_cookie import get_w_tsfp_cookie
import subprocess
import time
import requests
import os
import signal
from lxml import etree


w_tsfp_value = get_w_tsfp_cookie()

headers = {
    "Host": "www.mafengwo.cn",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "priority": "u=0, i"
}

cookies = {
    "w_tsfp": w_tsfp_value  # 替换进来
}

url = "https://www.mafengwo.cn/search/q.php"
params = {
    "q": "北京",
    "t": "questions",
    "seid": "159F2F76-E41F-4535-AE07-9D8ABD9DBF39"
}

print("正在发起请求...")
response = requests.get(url, headers=headers, cookies=cookies, params=params, verify=False)
html = etree.HTML(response.text)


results = []
blocks = html.xpath('//div[@class="ct-text closeto"]')
for block in blocks:
    title = block.xpath('.//h3/a/text()')
    link = block.xpath('.//h3/a/@href')
    desc = block.xpath('.//p[@class="seg-desc"]/text()')
    place = block.xpath('.//ul[@class="seg-info-list clearfix"]/li[1]/a/text()')
    stats = block.xpath('.//ul[@class="seg-info-list clearfix"]/li[2]/text()')

    results.append({
        'title': title[0].strip() if title else '',
        'link': link[0] if link else '',
        'desc': desc[0].strip() if desc else '',
        'place': place[0].strip() if place else '',
        'stats': stats[0].strip() if stats else ''
    })

print("抓取结果：")
for r in results:
    print(r)
