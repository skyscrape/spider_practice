import re

import requests
import execjs
session = requests.session()
headers = {

    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
cookies = {
    "sessionid": "adkbveoxngd1m3omxhk3f5z0rnfrf8bo",
    "yuanrenxue34": "fWkTbQ28nj",
    "iloveu": "0b37577c85daf1ee35f1d82f30e9a47bd8ebe0ac"
}
url = "https://www.python-spider.com/challenge/34"
session.headers.clear()
session.headers.update(headers)

response = session.get(url, headers=headers, cookies=cookies)

yuanrenxue34_value = response.cookies.get('yuanrenxue34')

cookies['yuanrenxue34'] = yuanrenxue34_value

pattern = re.compile(
    r'<script[^>]*>\s*([^<]*rind\s*=.*?)(?:</script>|$)',
    re.DOTALL | re.IGNORECASE
)

matches = pattern.findall(response.text)[0]

with open("index.js", "r", encoding="utf-8") as f:
    js_code = f.read()
# 替换原来的
js_code = js_code.replace("js_data", matches)

# 写入临时 JS 文件
with open("temp.js", "w", encoding="utf-8") as f:
    f.write(js_code)

js_compile = execjs.compile(open("temp.js", "r", encoding="utf-8").read())
data = js_compile.call("sEnc")
data = re.match(r'iloveu=(.*?);', data).group(1)
# print( data)

cookies["iloveu"] = data
print( cookies)

response = session.get('https://www.python-spider.com/challenge/34', cookies=cookies, headers=headers)
print(response.text)