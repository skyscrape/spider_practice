import pandas as pd
import requests
import execjs







def get_sign(page):
    execjs_obj = execjs.compile(open("index.js").read())
    m = execjs_obj.call("get_m",page)
    return m
def get_url_requests(page, m):
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer": "https://match.yuanrenxue.cn/match/12",
        "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    cookies = {
        "sessionid": "7yzilodu94rlst7d78ppe8sw0nn07s8r",
        "Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3": "1757577115",
        "HMACCOUNT": "9C5D5C4C24D2D864",
        "Hm_lpvt_434c501fe98c1a8ec74b813751d4e3e3": "1757577135"
    }
    url = "https://match.yuanrenxue.cn/api/match/12"
    params = {
        "page": page,
        "m": m
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    return response.json()['data']

if __name__ == '__main__':

    sum = 0
    for i in range(1, 6):
        m = get_sign(i)
        datalist = get_url_requests(i, m)
        for data in datalist:
            sum += data['value']
    print(sum)

