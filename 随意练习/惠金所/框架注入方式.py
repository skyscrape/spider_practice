import asyncio

from playwright.async_api import (
    BrowserContext,
    BrowserType,
    Page,
    Playwright,
    async_playwright,
)
from typing import Any, Dict, List, Optional, Tuple

import os


class HuiJS:
    def __init__(self):
        self.browser_context: BrowserContext
        self.context_page: Page
        self.index_url = "https://passport.yhd.com/"
    async def main(self):
        playwright_proxy_format, httpx_proxy_format = None, None
        async with async_playwright() as playwright:
            chromium = playwright.chromium
            self.browser_context = await self.launch_browser(
                chromium,
                playwright_proxy_format,
                user_agent=None,
                headless=True,
            )
            await self.browser_context.add_init_script(path="libs/stealth.min.js")
            self.context_page = await self.browser_context.new_page()
            await self.context_page.goto(self.index_url)

            password = await self.context_page.evaluate("""
            () => { 
                 var i = new JSEncrypt()
                return i.encrypt('15590455672')
            }
            """)
            print(password)



    async def launch_browser(
            self,
            chromium: BrowserType,
            playwright_proxy: Optional[Dict],
            user_agent: Optional[str],
            headless: bool = True,
    ) -> BrowserContext:
        user_data_dir = os.path.join(os.getcwd(), "browser_data", 'douyin_platform')  # type: ignore
        browser_context = await chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            accept_downloads=True,
            headless=headless,
            proxy=playwright_proxy,  # type: ignore
            viewport={
                "width": 1920,
                "height": 1080
            },
            user_agent=user_agent,
        )  # type: ignore
        return browser_context

if __name__ == "__main__":
    asyncio.run(HuiJS().main())