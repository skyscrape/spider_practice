import requests


headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://www.python-spider.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.python-spider.com/challenge/5",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "sessionid": "8ibovcuvtnpgzowio43cvmdnala1jcv2",
    "m": "pua"
}
url = "https://www.python-spider.com/api/challenge5"
params = {
    "m": "4UrkgIwjsrchfAKOC2qRltb4jx0ieHyhXvZItorSg8hL5lGtjcIt_woJEPyvWewABEIiJjuvPYIOUv86BABZmAn1OFEQ8mCPoofwLfSgUFEQ8mZs6AMZAZqSry.LIVreKhdhizu0AT3GqdKDFtueaV3JyaEZCld7mwIfgQbH1UNSVS9rKAbrjanG9V9Zh1osedYhOtnxoSfyqf33oUznhFQJeGxU4y2.cWAVU.P5Mx6KjTiXBybQBggAXLSI9Hixl0ergazd2nl5_nOITRsMoHqxv"
}
data = {
    "page": "3"
}
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data, verify=False)

print(response.text)
print(response)