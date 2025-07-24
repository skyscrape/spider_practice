import re
import time
import execjs
import requests
import subprocess



import random

import os


class MfwWendaSpider(object):
    def __init__(self):
        self.headers = {
            # 固定ua 需与js中ua保持一致
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        }
        self.cookies = {
            'mfw_uuid': '377817A9-05E6-462E-ABEA-1E174155B04C',
            "w_tsfp": 'ltvuV0MF2utBvS0Q7aPulUyrFz4hcT04h0wpEaR0f5thQLErU5mB2IF7uc72N3Pb68xnvd7DsZoyJTLYCJI3dwMGWd7AIddOzlDBzpMvzo4UARBnEZvcWVcfI7t17DBGfGpeJUXmjG9+JdRBzbVgmEUe4HsgnvE0CbBqdNlKgV4S6/XRzYo9C2mSxVPERTaQcnBZKuvfor8j/KtVoy2R'
        }
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

    def run_js_script(self):
        js_script_path = os.path.join(self.base_dir, 'index1.js')
        # 启 node，拿 stdout（多行）
        result = subprocess.run(
            ['node', js_script_path],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout

    def get_cookies(self):
        out = self.run_js_script()
        # 按行找 WTSFP_TOKEN=
        for line in out.splitlines():
            m = re.match(r'WTSFP_TOKEN=(.+)', line)
            if m:
                token = m.group(1).strip()
                self.cookies['w_tsfp'] = token
                return

        raise RuntimeError("没在 JS 输出里找到 WTSFP_TOKEN")

    def get_mafengwo_content(self, url, proxies=None):

        self.get_cookies()
        # log.info(f"*****smzdm cookies: {cookies}")
        time.sleep(1)
        response = requests.get(url, headers=self.headers, cookies=self.cookies, proxies=proxies, timeout=10)
        response.encoding = 'utf-8'
        # print(f"*****smzdm content: {response.text}")
        return response.text


if __name__ == '__main__':
    mafengwo = MfwWendaSpider()
    # 调用代码
    # urls = ['https://www.mafengwo.cn/gonglve/ziyouxing/407258.html', 'https://www.mafengwo.cn/gonglve/ziyouxing/407258.html',
    #         'https://m.mafengwo.cn/gonglve/ziyouxing/75198.html']
    urls = ['https://www.mafengwo.cn/i/919238.html']
    for url in urls:
        result = mafengwo.get_mafengwo_content(url)
        print(f"***********result: {result}")

