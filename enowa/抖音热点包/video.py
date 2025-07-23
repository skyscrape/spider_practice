import requests
import json


headers = {

    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
}
cookies = {

    "sid_guard_douhot": "3ae42b5e628fc3dd7d1847e0ff8894cc%7C1751348662%7C5184000%7CSat%2C+30-Aug-2025+05%3A44%3A22+GMT",
}
url = "https://douhot.douyin.com/douhot/v1/material/video_billboard"
data = {
    "page": 1,
    "page_size": 30,
    "date_window": 24,
    "sub_type": 1001,
    "tag_version": "v2",
    "tags": [
        {
            "value": 628,
            "children": [
                {
                    "value": 62808
                }
            ]
        }
    ]
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)