import requests


headers = {
    "Host": "aiqicha.baidu.com",
    "sec-ch-ua-platform": "\"macOS\"",
    "Zx-Open-Url": "https://aiqicha.baidu.com/company_detail_46470666527506?tab=basic",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://aiqicha.baidu.com/company_detail_46470666527506?tab=basic",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
cookies = {
    "BAIDUID": "8EAF7B47BC1B07845667F5C48BB807BC:FG=1",

}
url = "https://aiqicha.baidu.com/detail/basicAllDataAjax"
params = {
    "pid": "46470666527506"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params, verify= False)

# 保留原始 JSON 字符串（可选）
print("原始响应内容：")
print(response.text)

# ✅ 转译 unicode 为可读中文
decoded_text = response.text.encode('utf-8').decode('unicode_escape')
print("\n转译后的响应内容：")
print(decoded_text)