import requests

cookies = {
    'sid_guard_douhot': '8e804bd0544f24713969a02dfc0d8d6e%7C1750902499%7C5184000%7CMon%2C+25-Aug-2025+01%3A48%3A19+GMT',

}

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}

json_data = {
    'page': 1,
    'page_size': 30,
    'date_window': 24,
    'sub_type': 1001,
    'tag_version': 'v2',
}

response = requests.post(
    'https://douhot.douyin.com/douhot/v1/material/video_billboard',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

print(response.text)