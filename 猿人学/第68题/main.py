import requests


headers = {

    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",

}
cookies = {
    "sessionid": "n096lfi8ft9lrzioon334rjcj2u58fat"
}
url = "https://www.python-spider.com/api/challenge68"
response = requests.post(url, headers=headers, cookies=cookies)

print(response.text)
print(response)