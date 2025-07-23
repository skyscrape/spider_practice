import requests

import subprocess
import execjs
js_compile = execjs.compile(open('uuid.js').read())
proxy = {
    "http": "http://t12593394225924:jkke2jf7@k987.kdltpspro.com:15818",
    "https": "http://t12593394225924:jkke2jf7@k987.kdltpspro.com:15818"
}
def run_js_script():
    try:
        # 执行 JavaScript 文件 async_operation.js，使用 Node.js
        result = subprocess.run(['node', r'index.js'], capture_output=True, text=True, timeout=5)

        # 输出 JavaScript 进程的标准输出
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        print("JavaScript execution timed out.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing JavaScript: {e}")

cookies = {
    'mfw_uuid': '377817A9-05E6-462E-ABEA-1E174155B04C',
    'w_tsfp': 'ltv2UU8E3ewC6mwF46vukUusFDwvdT8ikAxsXqNmeJ94Q7ErU5mA0YR4usP3N3Pa5sxnt9jMsoszd3qAUdMlfxMQTcyWdYwVkB/Gy99yicxUQ0k5VYnWS1ZJIrNy6WZDKWpZIRTj3WotIIFJm7Bg2AtaunZ1zfxyXvFqL5kXjB0ZufzCkpxuDW3HlFWQRzaZciVfKr/c9OtwraxQ9z/c5Vv7LFt0A6hewgfHg31dWzox6wOpaPsYd0W/Kdz3HKlw7ibwsyz1HIWur1Fkpk5q4UhoXIKzhiuZcWNGVk8pNB7n3qNnKPv1b7U4+nFGGLlNPwRE/1pH4qVm7EY5DCi+YnWRXb4n6RIcVKEBqp73Om6YxJD+JV0NvIwuklpluJEEuW52Mz/zL9xSHDfPY3QHKIsBas6peQ==',
}

headers = {

    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    # 'cookie': 'PHPSESSID=e6evlua3pmbpj5c21edtnb1s17; mfw_uuid=68512acb-783a-6156-7bde-85570f008df3; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222025-06-17+16%3A43%3A55%22%3B%7D; __mfwc=direct; __mfwa=1750149868328.82795.1.1750149868328.1750149868328; __mfwlv=1750149868; __mfwvn=1; Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0=1750148200,1750149868; HMACCOUNT=7F51C13820CC1268; uva=s%3A130%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1750149868%3Bs%3A10%3A%22last_refer%22%3Bs%3A62%3A%22https%3A%2F%2Fwww.mafengwo.cn%2Ftravel-scenic-spot%2Fmafengwo%2F10065.html%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1750149868%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=68512acb-783a-6156-7bde-85570f008df3; __mfwlt=1750150485; Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0=1750150485; x-waf-captcha-referer=; w_tsfp=ltv2UU8E3ewC6mwF46vukUusFDwvdT8ikAxsXqNmeJ94Q7ErU5mA0YR4usP3N3Pa5sxnt9jMsoszd3qAUdMlfxMQTcyWdYwVkB/Gy99yicxUQ0k5VYnWS1ZJIrNy6WZDKWpZIRTj3WotIIFJm7Bg2AtaunZ1zfxyXvFqL5kXjB0ZufzCkpxuDW3HlFWQRzaZciVfKr/c9OtwraxQ9z/c5Vv7LFt0A6hewgfHg31dWzox6wOpaPsYd0W/Kdz3HKlw7ibwsyz1HIWur1Fkpk5q4UhoXIKzhiuZcWNGVk8pNB7n3qNnKPv1b7U4+nFGGLlNPwRE/1pH4qVm7EY5DCi+YnWRXb4n6RIcVKEBqp73Om6YxJD+JV0NvIwuklpluJEEuW52Mz/zL9xSHDfPY3QHKIsBas6peQ==',
}
url = 'https://m.mafengwo.cn/mdd/10198'
cook_value = run_js_script().split(';')[0].replace('w_tsfp: ', '')
uuid = js_compile.call('getUUID')


cookies['w_tsfp'] = cook_value
cookies['mfw_uuid'] = uuid

response = requests.get(url, headers=headers, cookies=cookies, proxies=proxy)

print(response.text)
print(response)