import pandas as pd
import requests


import execjs


def get_m():
    execjs_obj = execjs.compile(open("index.js").read())
    m = execjs_obj.call("get_sign")
    return m


def requests_url(page, m):
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer": "https://match.yuanrenxue.cn/match/1",
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
        "sessionid": "",
    }
    url = "https://match.yuanrenxue.cn/api/match/1"
    params = {
        "page": page,
        "m": m
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    print(response.json()['data'])
    return response.json()['data']


if __name__ == '__main__':
    m = get_m()
    df = pd.DataFrame()
    for i in range(1, 6):
        res = requests_url(i, m)
        df = pd.concat([df, pd.DataFrame(res)], ignore_index=True)
    print(df.values.mean())

