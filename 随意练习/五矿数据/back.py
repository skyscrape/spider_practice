import requests


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "Origin": "https://ec.minmetals.com.cn",
    "Pragma": "no-cache",
    "Referer": "https://ec.minmetals.com.cn/open/home/purchase-info?tabIndex=0",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    # "__jsluid_s": "616c4aabe725eac4a09c06cc8f79ae42",
    # "SUNWAY-ESCM-COOKIE": "f07685c4-56cc-4745-9d4e-31308d421b5a",
    # "JSESSIONID": "9FBC7A3A94BA41F46098D85042E8D8B9"
}
url = "https://ec.minmetals.com.cn/open/homepage/public"
response = requests.post(url, headers=headers, cookies=cookies)

print(response.text)
print(response)