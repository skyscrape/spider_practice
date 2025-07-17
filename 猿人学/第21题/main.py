import json
import subprocess

import requests



headers = {

    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",

}
cookies = {
    "sessionid": "6raruuswzazg6olw9pug7t3vquqfcjuj"
}
url = "https://www.python-spider.com/api/challenge21"

sum = 0
for i in range(1, 101):
    data = {
        "page": str(i),
        "s": "729fe4ac89c6a253d57fdbb4ba35d543",
        "t": "1752658935151"
    }
    result = subprocess.run(
        ["node", "index.js"],
        capture_output=True,
        text=True
    )

    pro_data = json.loads(result.stdout.strip())
    data['s'] = str(pro_data['s'])
    data['t'] = str(pro_data['t'])
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    datalist = response.json()['data']
    for data in datalist:
        sum += int(data['value'])
    print('page:::',  i,  'sum:::', sum, 'data:::', datalist)