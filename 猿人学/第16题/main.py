import requests


headers = {

    "safe": "MTc1MzgzODg5OA==|AAAAAAAAAAUAAAACAAAACAAAAAMAAAAAAAAABgAAAAAAAAAEAAAAAAAAAAUAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAkAAAACAAAAAgAAAAAAAAACAAAAAAAAAAkAAAAAAAAAAAAAAAYAAAAEAAAAAwAAAAYAAAAAAAAAAAAAAAkAAAAEAAAABQAAAAAAAAACAAAABgAAAAAAAAAGAAAAAwDh+4Hry9vOHwohBZ9V2Z+YEnisM",

    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",

}
cookies = {
    "sessionid": "adkbveoxngd1m3omxhk3f5z0rnfrf8bo"
}
url = "https://www.python-spider.com/api/challenge16"
data = {
    "page": "2"
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)