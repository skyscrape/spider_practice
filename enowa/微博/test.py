import requests


headers = {

    'referer': "https://weibo.com/u/7989402868",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",

}
cookies = {
    "SUB": "_2AkMf2m3Bf8NxqwFRmvkSzGPrbI13zAzEieKphpwaJRMxHRl-yj9xqhYLtRB6NFpDLkXFU1jRU2-pwX03STwS39iaH9Am",

}
url = "https://weibo.com/ajax/statuses/mymblog"
params = {
    "uid": "7989402868",
    "page": "1",
    "feature": "0"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)