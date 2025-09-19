import requests


headers = {

    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",

}
cookies = {
    # "BAIDUID_AQC": "A422B6F6840C7EF933D1FA4804F274D8:JS=20",
    # "_j47_ka8_": "57",
    # "Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf": "1753779920",
    # "HMACCOUNT": "4C48102E405E0541",
    "__jdg_yd": "lTM-TogKuTwn0mXPcGT6ZUbkAWWs3SFEHP05PPr75UKY2OYCaXKhwYn8cCFOFuAmw",
    # "ZX_UNIQ_UID": "55276140aa5bfb317ba375e85b2416fa",
    # "_fb537_": "xlTM-TogKuTwuahHcfnWbhqZmgs9U8cyp9NXAohntRoqmd",
    # "ZX_HISTORY": "%5B%7B%22visittime%22%3A%222025-07-29+17%3A11%3A03%22%2C%22pid%22%3A%22xlTM-TogKuTwzcJnGP0jxDDknK7qURq9UQmd%22%7D%5D",
    # "ab175377960": "833e5528390f031b5bbd4c94ec56ac1c17537802615c5",
    # "Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf": "1753780262",
    # "ab_sr": "1.0.1_ZjU0NGM5YjBhNWExMGU1NzIyZTU5NDBmMjM2MzQyNjk5MzQ1MGZlYzYyNzQwNzVhYTIwZjU1MWY2ZTUxYmM0ODBlOWFjOWQxOTFjYTI3ODdlYWRmY2EyYzk0Y2NhYWY4Y2JmNGQxZGU2N2ZjZTY4ZDcyODBlZjMxM2I2MzliNzMzNjM2NDc1NWUxNmUxMjM3ZTg2MDE5ODY0N2U3ZmRmMw==",
    # "_s53_d91_": "25688f88791ac3e0428a65e1763ba5fc46f8ced4ba5a3854309588c7a4b4fce5935857920b4f88f781c2f537576307f5e32408c645517323a90d457ebf87062599b8f558079e2b01b332435b3c79a8eb6c68e5f2fcc68de16784ac2e1226631aaf49a34266c1c4d5b0903eda0af76177cd606957574730775772656280eb01caf6e5f09acbe5ea36aa5daa8cb5ea23eca50d27cfd8d2f1a5d79d68bfd335c9dc7fd3384a738ab09147e13198206cd2ec270e41c90bc059372d9090c274b874f3b5c8b548fc1b521cfab36ab5fa59fa59",
    # "_y18_s21_": "1fbc5f3c",
    # "RT": "\"z=1&dm=aiqicha.com&si=7ea46284-1ea1-4b20-a0d1-b08e294157bd&ss=mdoba4e2&sl=5&tt=d9q&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=7gem&ul=81oi\""
}
url = "https://www.aiqicha.com/company_detail_31126242763719"
response = requests.get(url, headers=headers, cookies=cookies)

print(response.text)
print(response)