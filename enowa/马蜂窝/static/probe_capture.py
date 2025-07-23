import requests


headers = {
    "Host": "www.mafengwo.cn",
    "sec-ch-ua-platform": "\"macOS\"",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "accept": "*/*",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-dest": "script",
    "referer": "https://www.mafengwo.cn/wenda/detail-18342660.html",
    "accept-language": "zh-CN,zh;q=0.9",
    "priority": "u=1"
}
cookies = {
    "x-waf-captcha-referer": ""
}
url = "https://www.mafengwo.cn/C2WF946J0/probe.js"
params = {
    "v": "vc1jasc"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params, verify=False)

print(response.text)
print(response)