import asyncio
import subprocess
import os
import time
import psutil
from playwright.async_api import async_playwright

CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DEBUG_PORT = 9222
USER_DATA_DIR = "/tmp/zhihu_cdp"
ZH_URL = "https://zhuanlan.zhihu.com/p/252861467"

#/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/tmp/zhihu_profile" 每次启动需先在命令行输入以手动启动，不同电脑chrome路径不同，本程序使用mac默认chrome地址

def launch_chrome():
    for proc in psutil.process_iter(['name', 'cmdline']):
        cmdline = proc.info['cmdline']
        if cmdline and f'--remote-debugging-port={DEBUG_PORT}' in ' '.join(cmdline):
            print("✅ Chrome 已经在运行")
            return

    print("🚀 正在通过 open 启动 Chrome...")
    cmd = [
        "open", "-a", CHROME_PATH,
        "--args",
        f'--remote-debugging-port={DEBUG_PORT}',
        f'--user-data-dir={USER_DATA_DIR}',
        '--no-first-run',
        '--no-default-browser-check',
        '--disable-popup-blocking'
    ]
    subprocess.Popen(cmd)
    time.sleep(5)

async def extract_elements():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(f"http://localhost:{DEBUG_PORT}")
        context = browser.contexts[0] if browser.contexts else await browser.new_context()
        page = await context.new_page()

        print(f"🌐 正在打开: {ZH_URL}")
        await page.goto(ZH_URL, timeout=60000)

        await page.wait_for_timeout(5000)


        title_el = await page.query_selector("h1.Post-Title")
        title = await title_el.inner_text() if title_el else "❌ 标题未找到"

        # 提取正文
        content_el = await page.query_selector("div.RichText.ztext.Post-RichText")
        content = await content_el.inner_text() if content_el else "❌ 正文未找到"

        # 提取作者名
        author_el = await page.query_selector("#root > div > main > div > div.Post-Row-Content > div.Post-Row-Content-left > div > article > header > div.Post-Author > div > div > div > div.AuthorInfo-head > span > div > a")
        author = await author_el.inner_text() if author_el else "❌ 作者未找到"

        # 提取互动信息
        content_el = await page.query_selector("div.ContentItem-actions")
        star = await content_el.inner_text() if content_el else "❌ 互动信息未找到"

        # 提取发布时间
        content_el = await page.query_selector("div.ContentItem-time")
        publish_time = await content_el.inner_text() if content_el else "❌ 发布时间未找到"

        # 提取评论数量
        content_el = await page.query_selector("div.css-r4op92")
        comment_num = await content_el.inner_text() if content_el else "❌ 评论数量未找到"

        # 提取评论数据
        content_el = await page.query_selector("div.css-18ld3w0")
        comment = await content_el.inner_text() if content_el else "❌ 评论数量未找到"

        print("\n📄 标题:", title.strip())
        print("\n📝 正文:", content.strip(), "...")
        print("\n👤 作者:", author.strip())
        print("\n⭐ 互动信息:", star.strip())
        print("\n📅 发布时间:", publish_time.strip())
        print("\n💬 评论数量:", comment_num.strip())
        print("\n💬 评论:", comment.strip())

        await browser.close()

if __name__ == "__main__":
    # launch_chrome()
    asyncio.run(extract_elements())

