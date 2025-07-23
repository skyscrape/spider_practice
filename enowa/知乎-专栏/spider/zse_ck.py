import requests

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'origin': 'https://zhuanlan.zhihu.com',
    'pragma': 'no-cache',
    'priority': 'u=1',
    'referer': 'https://zhuanlan.zhihu.com/p/252861467',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://static.zhihu.com/zse-ck/v4/24df2abbfcb1b98cd5ce1b519f02eeabea28c83ac9d9ec2778dc5b03a3b8b710.js',
    headers=headers,
    verify=False,
)
print(response.text)