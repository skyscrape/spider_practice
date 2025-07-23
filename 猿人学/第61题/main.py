import asyncio
import json
import shutil
import subprocess
import websockets

async def process_page(websocket, i):
    """构造 JS、运行 Node、发送数据、处理响应"""
    # 1. 替换 JS 中的变量值
    shutil.copyfile("source.js", "temp.js")
    with open("temp.js", "r", encoding="utf-8") as f:
        js_code = f.read()
    js_code = js_code.replace("window.key_value = 1", f"window.key_value = '{i}'")
    with open("temp.js", "w", encoding="utf-8") as f:
        f.write(js_code)

    # 2. 执行 Node.js 脚本
    result = subprocess.run(["node", "index.js"], capture_output=True, text=True)

    if result.returncode != 0:
        print(f"[!] 第{i}页 Node 脚本执行失败：{result.stderr.strip()}")
        return 0  # 本页跳过

    payload = result.stdout.strip()
    if not payload:
        print(f"[!] 第{i}页输出为空，跳过")
        return 0

    await websocket.send(payload)
    response = await websocket.recv()
    print(f"Received: {response}", "page:::", i)

    try:
        Data = json.loads(response)
        return sum(int(d["value"].strip()) for d in Data["data"])
    except Exception as e:
        print(f"[!] 第{i}页解析失败：", e)
        return 0

async def main():
    uri = "wss://www.python-spider.com/api/challenge61"
    sum_total = 0
    current_page = 1

    while current_page <= 100:
        try:
            async with websockets.connect(uri) as websocket:
                print(f"[+] 建立连接成功，准备从第 {current_page} 页开始")
                while current_page <= 100:
                    await asyncio.sleep(0.5)
                    page_sum = await process_page(websocket, current_page)
                    sum_total += page_sum
                    print(f"[√] 当前累计总和：{sum_total}")
                    current_page += 1

        except websockets.exceptions.ConnectionClosedError:
            print(f"[!] 连接在第 {current_page} 页中断，尝试重新连接...")
            await asyncio.sleep(2)
            continue
        except Exception as e:
            print("[!] 未知错误：", e)
            break

    print("[✅] 最终总和：", sum_total)

# 启动事件循环
asyncio.run(main())