# main_script.py
import asyncio
import json
import re
from playwright.async_api import async_playwright

response_json = None
response_event = asyncio.Event()

async def run():
    global response_json
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        async def on_prehandle_response(response):
            global response_json
            if "cap_union_prehandle" in response.url:
                try:
                    text = await response.text()
                    if text.startswith("_aq_"):
                        json_text = re.search(r"_aq_\d+\((.*)\)", text).group(1)
                        response_json = json.loads(json_text)
                        response_event.set()
                except:
                    pass

        async def on_bg_image_response(response):
            if "cap_union_new_getcapbysig" in response.url and "img_index=1" in response.url:
                try:
                    print("🎯 捕获滑块背景图链接:", response.url)
                    buffer = await response.body()
                    with open("bg.jpg", "wb") as f:
                        f.write(buffer)
                except:
                    pass

        page.on("response", on_prehandle_response)
        page.on("response", on_bg_image_response)

        await page.goto("file:///Users/liyongqi/PycharmProjects/spider/嗯哦哇/马蜂窝/slider/test.html")
        try:
            await page.wait_for_selector("button", timeout=5000)
            await page.click("button")
        except:
            await browser.close()
            return None

        try:
            await asyncio.wait_for(response_event.wait(), timeout=5)
        except asyncio.TimeoutError:
            await browser.close()
            return None

        await asyncio.sleep(1.5)
        await browser.close()
        return response_json