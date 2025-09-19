import requests
import execjs

js_compile = execjs.compile(open("index.js", encoding="utf-8").read())

import requests


headers = {
    "Accept": "*/*",
    "Accept-EncKey": "36mnb37hmTGeFzyHYVS4MA==",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://webapi.cninfo.com.cn",
    "Pragma": "no-cache",
    "Referer": "https://webapi.cninfo.com.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
headers["Accept-EncKey"] = js_compile.call("getResCode")
# print(headers)
cookies = {
    # "Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b": "1756086463",
    # "HMACCOUNT": "A86953C510CDFDC7",
    # "MALLSSID": "696170774567396A62743044596E4269584342443166613945777A434B445341324B56356D46714E4C4977554442356A396C767A39397671666C3752304C704C",
    # "Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b": "1756345785"
}
url = "https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007"
data = {
    "tdate": "2025-08-26",
    "market": "DCE"
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)