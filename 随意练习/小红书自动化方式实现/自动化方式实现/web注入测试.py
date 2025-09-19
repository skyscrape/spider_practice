# simple_test.py
import asyncio
from playwright.async_api import async_playwright
import json

async def simple_test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # 访问小红书
        await page.goto("https://www.xiaohongshu.com")
        await page.wait_for_timeout(5000)

        # 检查和测试加密函数
        try:
            # 检查函数是否存在
            exists = await page.evaluate("() => typeof window._webmsxyw !== 'undefined'")
            print(f"函数存在: {exists}")

            if exists:
                # 测试调用
                result = await page.evaluate(
                    "([url, data]) => window._webmsxyw(url, data)",
                    ["/api/sns/web/v1/search/notes", {"keyword": "测试"}]
                )
                print(f"结果: {json.dumps(result, indent=2)}")
            else:
                print("函数不存在")

        except Exception as e:
            print(f"错误: {e}")

        input("按回车键关闭浏览器...")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(simple_test())
