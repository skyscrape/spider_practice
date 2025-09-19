import subprocess

import requests
import re




def get_m():
    result = subprocess.run(
        ["node", "index.js"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()
def get_response(page, m):
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer": "https://match.yuanrenxue.cn/match/2",
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
        "m": m ,
    }
    url = "https://match.yuanrenxue.cn/api/match/2"
    params = {
        "page": page
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params).json()
    return response['data']

if __name__ == '__main__':
    sum = 0
    m = get_m()

    m = re.findall(r'mundefined=(.*?); path=/', m)[0]
    # print(m)
    for i in range(1, 6):

        datalist = get_response(i, m)
        print(datalist)
        for data in datalist:
            sum += data['value']
    print(sum)