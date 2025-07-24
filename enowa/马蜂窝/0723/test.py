import requests


headers = {

    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

cookies = {
    "mfw_uuid": "683fa86e-f3be-bdfb-553d-dbfc0727591a",
    "w_tsfp": "ltv2UU8E3ewC6mwF46vukUisFT8vfTotlgtsXqNmeJ94Q7ErU5mA0oR5ucP/Mnzc4cxnt9jMsoszd3qAUdMmfxITTcSTeooSkB/Gy99yicxUQ0k5VYnWS1ZKJu515TJBejxYIEazimZ/JodFyLdojVsP5ycgy/ghXvFqL5kXjB0ZufzCkpxuDW3HlFWQRzaZciVfKr/c9OtwraxQ9z/c5Vv7LFt0A6hewgfHg31dWzox6wOpaPsYd0W/Kdz3HKlw7ibwsyz1HIWur1Fkpk5q4UhoXIKzhiuZcWNGVk8pNB7n3qNnKPv1b7U4+nFGGLlNPwRE/1pH4qVm7EY5DCu9Y3aRXb4n6RIcVKEBqp73Om6YxJD+IwtQvtQtkFkz7ZRX7m11NWz1e9cLQDOabHpZeIQIPcqpeQ=="
}
url = "https://www.mafengwo.cn/travel-scenic-spot/mafengwo/13033.html"
response = requests.get(url, headers=headers, cookies=cookies)

print(response.text)
print(response)