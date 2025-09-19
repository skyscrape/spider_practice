import re
import time

import requests
import subprocess



import random

import os


class SMZDMSpider(object):
    def __init__(self):
        self.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        }
        self.cookies = {
            "w_tsfp": 'ltvuV0MF2utBvS0Q7KnqlkmrEzkjdDs4h0wpEaR0f5thQLErU5mA0oV4vM7yMnHd48xnvd7DsZoyJTLYCJI3dwMGWd7AIddOzlDBzpMvzo4UARBnEZvcWVcfI7t17DBGfGpeJUXmjG9+JdRBzbVgmEUe4HsgnvE0CbBqdNkb0A5B6qbWzIpmBGWUwl2QQGfLI3RYKr3b/el4//5Wpi2R'
        }
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

    def run_js_script(self):
        js_script_path = os.path.join(self.base_dir, 'env1.js')
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

    def get_smzdm_content(self, url, proxies=None):

        self.get_cookies()
        time.sleep(1)
        response = requests.get(url, headers=self.headers, cookies=self.cookies, proxies=proxies, timeout=10)
        response.encoding = 'utf-8'
        print(f"*****smzdm content: {response.text}")
        # return response.text


if __name__ == '__main__':
    smzdm = SMZDMSpider()
    # 调用代码
    urls = ['https://post.m.smzdm.com/p/agw9e9o6']

    for url in urls:
        smzdm.get_smzdm_content( url)
