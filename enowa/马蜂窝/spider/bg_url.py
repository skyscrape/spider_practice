import requests


url ='https://t.captcha.qq.com/cap_union_new_getcapbysig?img_index=1&amp;image=02bd27000000004600000009dcd7dc2c3f13&amp;sess=s0xDGkNQbW7xHY3148qtjVOwyia08gwa2IbVK_pe7jbbPGlUNfohTu9_AgHc76ZBRWIk7hV2IYNbSGhOp6_Zk1-tXerwNFveUiP_uSBQ5FapmHBF7FqtlqlD7eyGcEl6mvrLgDJqLlFvCEwGyVpy4ZOJ5gX2-TX6wR1L2C9jtSbpetXOcpCfsVz8B5utsicnCfDzv879Li_PARaDU7JdhPQvZ1t4rnqqLmdoKxwHB-O_BTZVDlizqzdLqppb3bIu5xKwRF_Ou_fe1MAwS3KMXklPjJE001p9NatCwuaRF9-Fsr441dPgVJHMVHmDSF8e74WYB3NyLEtQUhYk47prEMvTJoPEK1ZcFDpDT8OAo8BVXz1Gn7EJzLbfHZVZRbX31u0bbED6qlnJRc8ASyH0Omw3FeaWIfLIEyapOMy-RYrNE7C49tb_9KeiUPKFf6i0UiAiL24j-wBog*'
cookies = {
    'w_tsfp': 'ltvuV0MF2utBvS0Q7aPolEmpFzwjczk4h0wpEaR0f5thQLErU5mB2Id6vMz2NXbW6sxnvd7DsZoyJTLYCJI3dwMGWd7AIddOzlDBzpMvzo4UARBnEZvcWVcfI7t17DBGfGpeJUXmjG9+JdRBzbVgmEUe4HsgnvE0CbBqdNlB01hH7KaCy9s6CWzGwAeXEmPNd3FWLuuKpup3pKsC/y2R',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    # 'cookie': 'w_tsfp=ltvuV0MF2utBvS0Q7aPpnUqpETsgczE4h0wpEaR0f5thQLErU5mB2IZzv8zwM3zf68xnvd7DsZoyJTLYCJI3dwMXTJ6Wc90Yi1uTlYF0iY4UUkJkR5qNXlNKJbomvzZAenhCNxS00jA8eIUd379yilkMsyN1zap3TO14fstJ019E6KDQmI5uDW3HlFWQRzaLbjcMcuqPr6g18L5a5T6IsQj6eV0lUrMR00CW0C4eWHty5BO/c+0MZBj/JcyrSqA=',
}
resp = requests.get(url, headers=headers)
if resp.status_code == 200:
    with open("bg.jpg", "wb") as f:
        f.write(resp.content)
else:
    print("访问失败:", resp.status_code)
# response = requests.get('https://www.mafengwo.cn/wenda/detail-18342660.html', headers=headers, cookies=cookies, verify=False)
# print(response.text)