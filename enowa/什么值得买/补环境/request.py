import requests

import subprocess
def run_js_script():
    try:
        # 执行 JavaScript 文件 async_operation.js，使用 Node.js
        result = subprocess.run(['node', r'env.js'], capture_output=True, text=True, timeout=5)

        # 输出 JavaScript 进程的标准输出
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        print("JavaScript execution timed out.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing JavaScript: {e}")


url = "https://post.smzdm.com/p/azo4vrl0/"
headers = {

    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}
cookies = {
    "w_tsfp": 'ltvuV0MF2utBvS0Q7aPulUyrFz4hcT04h0wpEaR0f5thQLErU5mB2IF7uc72N3Pb68xnvd7DsZoyJTLYCJI3dwMGWd7AIddOzlDBzpMvzo4UARBnEZvcWVcfI7t17DBGfGpeJUXmjG9+JdRBzbVgmEUe4HsgnvE0CbBqdNlKgV4S6/XRzYo9C2mSxVPERTaQcnBZKuvfor8j/KtVoy2R'
}

cook_value = run_js_script().split(';')[0].replace('w_tsfp: ', '')
cookies['w_tsfp'] = cook_value

response = requests.get(url, headers=headers, cookies=cookies)

print(response.text)
print(response)