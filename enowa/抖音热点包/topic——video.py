import requests


headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",

}
cookies = {
    "sid_guard_douhot": "3ae42b5e628fc3dd7d1847e0ff8894cc%7C1751348662%7C5184000%7CSat%2C+30-Aug-2025+05%3A44%3A22+GMT",
}
url = "https://douhot.douyin.com/douhot/v1/challenge_analysis/data_summary/item_list"
params = {
    "challenge_id": "1606465689061379",
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)