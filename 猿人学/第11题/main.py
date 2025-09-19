import subprocess

import requests
import re

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://www.python-spider.com/challenge/11",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
cookies = {
    "sessionid": "adkbveoxngd1m3omxhk3f5z0rnfrf8bo",
    "__jsl_clearance": "1753707318.872|0|clD4VpfqhdaLBWywKWy%2FZyfi6d_cf266c677c23cbbcf31764de74001e0f3D"
}
url = "https://www.python-spider.com/challenge/11"
response = requests.get(url, headers=headers, cookies=cookies)
print(response.text)

# result = re.findall(r'<script>(.*)</script>', response.text)[0]
#
# with open("source.js", "w", encoding="utf-8") as f:
#     f.write(result)
#
# result = subprocess.run(
#     ["node", "index.js"],
#     capture_output=True,
#     text=True
# )
# print(result.stdout.strip())