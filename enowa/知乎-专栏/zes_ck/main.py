import requests,subprocess
from lxml import etree
import random

proxy = {
    "http": "http://t12593394225924:jkke2jf7@k987.kdltpspro.com:15818",
    "https": "http://t12593394225924:jkke2jf7@k987.kdltpspro.com:15818"
}

ua_pool = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.70 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.92 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; JiSu) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.3.1.7 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"
]


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; JiSu) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.3.1.7 Safari/537.36"
}

def run_js_script():
    try:
        # 执行 JavaScript 文件 async_operation.js，使用 Node.js
        result = subprocess.run(['node', r'__zse_ck_env.js'], capture_output=True, text=True, timeout=5)

        # 输出 JavaScript 进程的标准输出
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        print("JavaScript execution timed out.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing JavaScript: {e}")


with open('zhihu.txt', 'r', encoding='utf-8') as f:
    urls = [line.strip() for line in f if line.strip()]

for url in urls:
    print(f"处理 URL: {url}")

    headers = {
        "user-agent": random.choice(ua_pool)
    }

    try:
        # 第一次访问
        response = requests.get(url, headers=headers, proxies=proxy, timeout=10)
        response.encoding = 'utf-8'

        tree = etree.HTML(response.text)
        content = tree.xpath('.//meta[@id="zh-zse-ck"]/@content')[0]
        jsUrl = tree.xpath('.//script/@src')[0]
        contentJs = f'contentc = "{content}";'

        with open('./content.js', 'w', encoding='utf-8') as f:
            f.write(contentJs)

        js_content = requests.get(jsUrl, headers=headers, proxies=proxy, timeout=10).text
        with open('./emo.js', 'w', encoding='utf-8') as f:
            f.write(js_content)

        # 执行JS，生成cookie
        cookie_value = run_js_script().split(';')[0].replace('__zse_ck=', '')
        print('cookie_value:::', cookie_value)
        cookies = {'__zse_ck': cookie_value}

        # 第二次请求，带cookie
        response_final = requests.get(url, headers=headers, cookies=cookies, proxies=proxy, timeout=10)
        response_final.encoding = 'utf-8'

        print(f"✅ 成功获取: {url}")
        print(response_final.status_code)
        # 这里可以把内容保存或者做别的处理
        # print(response_final.text)

    except Exception as e:
        print(f"❌ 处理失败: {url}，错误信息: {e}")