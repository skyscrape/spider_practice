import pychrome
import time
import json
from bs4 import BeautifulSoup

# 启动浏览器
browser = pychrome.Browser(url="http://127.0.0.1:9222")
tabs = browser.list_tab()
tab = tabs[0] if tabs else browser.new_tab()

def on_response_received(**kwargs):
    response = kwargs.get("response", {})
    url = response.get("url", "")
    if "api.zhihu.com/v4/questions/" in url and "answers" in url:
        print(f"✅ 捕获知乎回答接口: {url}")

def on_loading_finished(**kwargs):
    print("✅ 页面加载完成")
    # 获取页面 HTML
    html = tab.Runtime.evaluate(expression="document.documentElement.outerHTML")["result"]["value"]
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("title").text
    print("📌 页面标题：", title)

# 启动事件监听
tab.Network.responseReceived = on_response_received
tab.Page.loadEventFired = on_loading_finished

tab.start()
tab.Network.enable()
tab.Page.enable()

# 你可以换成你想采集的问题 URL
question_url = "https://www.zhihu.com/question/59946668"
tab.Page.navigate(url=question_url)
tab.wait(10)

# 等待手动滑块处理或加载完成
print("⏳ 等待页面交互完成...")
time.sleep(8)

# 截图或提取页面数据等后续操作可加在这里

tab.stop()