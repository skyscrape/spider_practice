import asyncio

from playwright.async_api import (
    BrowserContext,
    BrowserType,
    Page,
    Playwright,
    async_playwright,
)
from typing import Any, Dict, List, Optional, Tuple
from client import DouYinClient
import os
from tools import utils
from exception import DataFetchError
from field import PublishTimeType


class DouYinCrawler:
    context_page: Page
    dy_client: DouYinClient
    browser_context: BrowserContext

    def __init__(self) -> None:
        self.index_url = "https://www.douyin.com"
        self.CRAWLER_MAX_NOTES_COUNT = 20
        self.START_PAGE = 1
        # 关键词搜索配置，以英文逗号分隔
        self.KEYWORDS = "北海旅游"


    async def start(self) -> None:
        playwright_proxy_format, httpx_proxy_format = None, None
        async with async_playwright() as playwright:
            utils.logger.info("[DouYinCrawler] 使用标准模式启动浏览器")
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

    async def search(self) -> None:
        utils.logger.info("[DouYinCrawler.search] Begin search douyin keywords")
        dy_limit_count = 10  # douyin limit page fixed value
        if self.CRAWLER_MAX_NOTES_COUNT < dy_limit_count:
            self.CRAWLER_MAX_NOTES_COUNT = dy_limit_count
        start_page = self.START_PAGE  # start page number
        for keyword in self.KEYWORDS.split(","):
            utils.logger.info(f"[DouYinCrawler.search] Current keyword: {keyword}")
            aweme_list: List[str] = []
            page = 0
            dy_search_id = ""
            while (page - start_page + 1) * dy_limit_count <= self.CRAWLER_MAX_NOTES_COUNT:
                if page < start_page:
                    utils.logger.info(f"[DouYinCrawler.search] Skip {page}")
                    page += 1
                    continue
                try:
                    utils.logger.info(f"[DouYinCrawler.search] search douyin keyword: {keyword}, page: {page}")
                    posts_res = await self.dy_client.search_info_by_keyword(
                        keyword=keyword,
                        offset=page * dy_limit_count - dy_limit_count,
                        publish_time=PublishTimeType(0),
                        search_id=dy_search_id,
                    )
                    print(posts_res)
                    if posts_res.get("data") is None or posts_res.get("data") == []:
                        utils.logger.info(f"[DouYinCrawler.search] search douyin keyword: {keyword}, page: {page} is empty,{posts_res.get('data')}`")
                        break
                except DataFetchError:
                    utils.logger.error(f"[DouYinCrawler.search] search douyin keyword: {keyword} failed")
                    break

                page += 1
                if "data" not in posts_res:
                    utils.logger.error(f"[DouYinCrawler.search] search douyin keyword: {keyword} failed，账号也许被风控了。")
                    break
            utils.logger.info(f"[DouYinCrawler.search] keyword:{keyword}，检索完成")


if __name__ == "__main__":
    asyncio.run(DouYinCrawler().start())