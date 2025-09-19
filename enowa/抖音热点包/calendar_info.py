import requests
import json


headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
cookies = {
    "sid_guard_douhot": "3ae42b5e628fc3dd7d1847e0ff8894cc%7C1751348662%7C5184000%7CSat%2C+30-Aug-2025+05%3A44%3A22+GMT",
}
url = "https://douhot.douyin.com/douhot/v1/calendar/query_list"
data = {
    "start_date": 1754755200,
    "end_date": 1755100800,

}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)
print(response.json())

data = response.json()['data']
event_list = data['event_list']
#
# for item in event_list:
#     print( item['tags'], item['event_ids'])


