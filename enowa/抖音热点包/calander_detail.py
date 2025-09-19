import requests

cookies = {
    'sid_guard_douhot': '3ae42b5e628fc3dd7d1847e0ff8894cc%7C1751348662%7C5184000%7CSat%2C+30-Aug-2025+05%3A44%3A22+GMT',
}

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
}


response = requests.get(
    'https://douhot.douyin.com/douhot/v1/calendar/446/detail',
    # params=params,
    cookies=cookies,
    headers=headers,
)
print(response.json())