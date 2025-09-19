import requests




session = requests.Session()

session.headers = {
    'Content-Length': '0',
    'Accept': '*/*',
    'Referer': 'https://match.yuanrenxue.cn/match/3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cookie': "sessionid=gca1b1ftj48s5vedwjnq95dcr3zgrm2y;"
}

session.post('https://match.yuanrenxue.cn/jssm')
pre_url = "https://match.yuanrenxue.com/jssm"
page = 1
api_url = f"https://match.yuanrenxue.com/api/match/3?page={page}"

print(session.get(api_url).text)






