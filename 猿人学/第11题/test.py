import re

import execjs
import requests
from bs4 import BeautifulSoup



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
res = requests.get("https://www.python-spider.com/challenge/11", headers=headers, cookies=cookies, timeout=10)
# print(res.status_code, res.text)
script_js = "function get_vm(){" + res.text[8:-9].replace('eval', 'script_js_2=') + "return script_js_2}"
vm_js = execjs.compile(script_js).call('get_vm')
cookie_js = "function get_cookie(){ var document={'createElement':createElement};function createElement(){return{'innerHTML':'','firstChild':{'href':'http://xxxxxxx/'}}};" + re.search(r"cookie=.*\(\)\+", vm_js).group().rstrip('+') + ";return cookie}"
jsl_cookie = execjs.compile(cookie_js).call('get_cookie')
# print(jsl_cookie)
pro_jsl = re.findall(r"__jsl_clearance=(.*)", jsl_cookie)[0]
print(pro_jsl)
cookies['__jsl_clearance'] = pro_jsl
res = requests.get("https://www.python-spider.com/challenge/11", headers=headers, cookies=cookies, timeout=10)
soup = BeautifulSoup(res.text, "lxml")
s = sum([int(td.get_text().strip()) for td in soup.select(".odd td")])
print(s)
