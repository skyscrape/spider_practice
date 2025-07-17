import httpx

client = httpx.Client(http2=True)



headers = {

    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
}
cookies = {
    "sessionid": "6raruuswzazg6olw9pug7t3vquqfcjuj"
}
url = "https://www.python-spider.com/api/challenge24"

sum = 0
for i in range(1, 101):
    data = {
        "page": str(i),
    }
    response = client.post(url, data=data, cookies=cookies, headers=headers).json()
    datalist = response["data"]
    for data in datalist:
        sum += int(data["value"])
    print('page:::',  i,  'sum:::', sum, 'data:::', datalist)