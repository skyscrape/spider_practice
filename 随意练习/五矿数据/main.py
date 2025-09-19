import requests
import json


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://ec.minmetals.com.cn",
    "Pragma": "no-cache",
    "Referer": "https://ec.minmetals.com.cn/open/home/purchase-info?tabIndex=0",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    # "__jsluid_s": "616c4aabe725eac4a09c06cc8f79ae42",
    # "SUNWAY-ESCM-COOKIE": "f07685c4-56cc-4745-9d4e-31308d421b5a",
    # "JSESSIONID": "9FBC7A3A94BA41F46098D85042E8D8B9"
}
url = "https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page"
data = {
    "param": "MQiAz0lABo+O8vSFR6mDGmmN1XXd9dHo4KiZh+1a/Tu25NmDiE6/38WChYAC9A32S5dgL1N3eoA6hckB3vodM97Q4XRl2Oap2X4SUS/NAs/fBleWrybhGsN8ot4q8Gjv5Wyc+RltdqjrIwaLHhmA2w4IRdoN0f7PYnJZZO47rVtfnG5gYJz3JhcpOwiSoOPiEJahLGgZi8er0BXPKPxYaFBQAnoLbuoxjmrP5AZFgUPbL8D8NEuRTNQ2xTxSxuUpNY2jQVTcNqBr9Sq7KVobboii+Rp9qzSjNjntoRREZnLON4t/VRdRh2VcPtcOcOQWO8rTRIoJ9o0JApym1e289Skbx6takZ2VxNVZ+N4vDRLTxe3XazAfaV65ZUxSsFOrnc0nuQ0FsTFvzFCz9+h79rMHfHrz2JDNyWXLG5SaiKwsS5UBLXEDGMggOBMaEr8Q6Us7rQeznkAvONpM21Aenn4lbeEV5zP+4xB5OBn+HyyjH8IuAk261i0REGXzJJz8QiIOk38fNgOQdiuO0pcCSbIKwoXohiWOSSqpNcrENYjieoq6les8Nsx1q2SmYv3Js5k+kLznYsBpnX54kT1nBrNf5mkckjpBk9l3EQXYJLOaR7DLFtotyKt3AsOyOQFVMsnImMUrfCXkBU6in3HlzcAliHQ78o4KFt13q2Qtd9M="
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)