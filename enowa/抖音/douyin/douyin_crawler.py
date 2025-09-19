
from playwright.async_api import (
    BrowserContext,
    BrowserType,
    Page,
    Playwright,
    async_playwright,
)
from typing import Any, Dict, List, Optional, Tuple

class DouYinCrawler:
    context_page: Page
    dy_client: DouYinClient
    browser_context: BrowserContext

    def __init__(self) -> None:
        self.index_url = "https://www.douyin.com"


    async def start(self) -> None:
        playwright_proxy_format, httpx_proxy_format = None, None
        async with async_playwright() as playwright:
            print("[DouYinCrawler] 使用标准模式启动浏览器")
            # Launch a browser context.
            chromium = playwright.chromium
            self.browser_context = await self.launch_browser(
                chromium,
                playwright_proxy_format,
                user_agent=None,
                headless=False,
            )
            await self.browser_context.add_init_script(path="libs/stealth.min.js")
            self.context_page = await self.browser_context.new_page()
            await self.context_page.goto(self.index_url)
            self.dy_client = await self.create_douyin_client(httpx_proxy_format)
            await self.search()

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

    async def create_douyin_client(self, httpx_proxy: Optional[str]) -> DouYinClient:
            """Create douyin client"""
        cookie_str, cookie_dict = utils.convert_cookies(await self.browser_context.cookies())  # type: ignore
        douyin_client = DouYinClient(
            proxy=httpx_proxy,
            headers={
                "User-Agent": await self.context_page.evaluate("() => navigator.userAgent"),
                "Cookie": cookie_str,
                "Host": "www.douyin.com",
                "Origin": "https://www.douyin.com/",
                "Referer": "https://www.douyin.com/",
                "Content-Type": "application/json;charset=UTF-8",
            },
            playwright_page=self.context_page,
            cookie_dict=cookie_dict,
        )
        return douyin_client