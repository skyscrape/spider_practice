import requests

cookies = {

    'sid_guard_douhot': '3ae42b5e628fc3dd7d1847e0ff8894cc%7C1751348662%7C5184000%7CSat%2C+30-Aug-2025+05%3A44%3A22+GMT',

}

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',

}

params = {
    'option': '7',
    'date_window': '1',
    'msToken': '',
    # 'X-Bogus': 'DFSzswVY-u2ANGP5CSdiCGlUrn8E',
    # '_signature': '_02B4Z6wo00001R6RXNwAAIDAN5XCoZsbYRkekVhAAC.Tvx73owHW7xxdFy05Ytye91-YV5ClQj77fw6K.qgx5GCfbchQbRdSdukX83.Nzh7KYLxRcqZURXz2qnQhZiQRoIGmdz9OzUH0bn8T1c',
}

response = requests.get(
    'https://douhot.douyin.com/douhot/v1/item_analysis/7526036101098933562/data_trends/trends',
    params=params,
    cookies=cookies,
    headers=headers,
)
print(response.text)