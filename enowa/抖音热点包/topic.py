import requests

cookies = {
    'sid_guard_douhot': 'dbcb73772d1af293055acb0aaa1dfe6f%7C1751419217%7C5184000%7CSun%2C+31-Aug-2025+01%3A20%3A17+GMT',
}

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}


json_data = {
    'page': 2,
    'page_size': 10,
    'date_window': 24,
    'sub_type': 2001,
    'tag_version': 'v2',
    # 'tags': [
    #     {
    #         'value': 628,
    #         'children': [
    #             {
    #                 'value': 62808,
    #             },
    #         ],
    #     },
    # ],
}

response = requests.post(
    'https://douhot.douyin.com/douhot/v1/material/challenge_billboard',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
print(response.text)