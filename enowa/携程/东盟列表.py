import requests
import json


headers = {

    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",

}
cookies = {


    "cticket": "8DC3F6BD4A2E81F5CB0712429496D561D4343460E260D986ABF2428A3E724032",


}
url = "https://m.ctrip.com/restapi/soa2/18109/json/getAttractionList"
params = {
    # "_fxpcqlniredt": "09031127217303646654",
    # "x-traceID": "09031127217303646654-1752628229856-1756055"
}
data = {
    "head": {
        "cid": "09031127217303646654",
        "ctok": "",
        "cver": "1.0",
        "lang": "01",
        "sid": "8888",
        "syscode": "999",
        "auth": "",
        "xsid": "",
        "extension": []
    },
    "scene": "online",
    "districtId": 53,
    "index": 2,
    "sortType": 1,
    "count": 10,
    "filter": {
        "filterItems": []
    },
    "coordinate": {
        "latitude": 39.79938506897685,
        "longitude": 116.54534149227766,
        "coordinateType": "WGS84"
    },
    "returnModuleType": "product"
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

print(response.text)
print(response)