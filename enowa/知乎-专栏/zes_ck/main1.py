import requests,subprocess
from lxml import etree



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

url = "https://www.zhihu.com/tardis/zm/art/413238854"
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
print(response.text)


# tree = etree.HTML(response.text)
# content = tree.xpath('.//meta[@id="zh-zse-ck"]/@content')[0]
# jsUrl = tree.xpath('.//script/@src')[0]
# contentJs = f'contentc = "{content}";'
#
# with open('./content.js', 'w', encoding='utf-8') as f:
#     f.write(contentJs)
#
# with open('./w.js', 'w', encoding='utf-8') as f:
#     f.write(requests.get(jsUrl).text)
#
# cookies = {
#     '__zse_ck':run_js_script().split(';')[0].replace('__zse_ck=','')
# }
# print(cookies['__zse_ck'])
# response = requests.get(url, headers=headers,cookies=cookies)
# response.encoding = 'utf-8'

print(response.text)
print(response)