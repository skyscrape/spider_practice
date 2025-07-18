import requests


headers = {

    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",

}
cookies = {
    # "cookiesu": "321733297270836",
}
url = "https://xueqiu.com/8768643388/301981148"
response = requests.get(url, headers=headers, cookies=cookies)

print(response.text)
print(response)