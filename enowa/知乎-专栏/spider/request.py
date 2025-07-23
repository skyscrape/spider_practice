import requests

cookies = {
    '_xsrf': 'kFmmSxl49jUb4wBtX4hEz78qlJg69ZVP', #session 携带
    #-之后后半部分为初始发送携带的content值
    '__zse_ck': '004_kR=g2dKoInSTcoaSzy/h2fziPdPK5wO8Nd9vQV5OxYybgsGAW7szrUpS7otvtkDzXZuZdO0pzyBgSzP4wFJUSCTBmBk2vlsoduSbgDes1KAKFN0ciCymQVSCMLvlWWA7-ZJhxugZK81c6FHxO2bFtahRUNn83zkDwDM8H+s8K4aYXMs8IwqsUKQOGr1EIOuLiQgBbXte/zXdivoh3EQTYai+sIQbbpNLhFeyfz1xHuaeyPDWZ8T02CB2X00OcDac7',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://zhuanlan.zhihu.com/p/252861467',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    # 'cookie': '_xsrf=kFmmSxl49jUb4wBtX4hEz78qlJg69ZVP; __zse_ck=004_kR=g2dKoInSTcoaSzy/h2fziPdPK5wO8Nd9vQV5OxYybgsGAW7szrUpS7otvtkDzXZuZdO0pzyBgSzP4wFJUSCTBmBk2vlsoduSbgDes1KAKFN0ciCymQVSCMLvlWWA7-ZJhxugZK81c6FHxO2bFtahRUNn83zkDwDM8H+s8K4aYXMs8IwqsUKQOGr1EIOuLiQgBbXte/zXdivoh3EQTYai+sIQbbpNLhFeyfz1xHuaeyPDWZ8T02CB2X00OcDac7',
}

response = requests.get('https://zhuanlan.zhihu.com/p/252861467', cookies=cookies, headers=headers)
print(response.text)