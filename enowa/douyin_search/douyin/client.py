import copy
import json
import random
import urllib

import execjs
import httpx
from playwright.async_api import (
    BrowserContext,
    BrowserType,
    Page,
    Playwright,
    async_playwright,
)
from typing import Any, Dict, List, Optional, Tuple

from field import PublishTimeType, SearchChannelType, SearchSortType
from tools import utils


class DouYinClient:


    def __init__(
            self,
            timeout=60,  # 若开启爬取媒体选项，抖音的短视频需要更久的超时时间
            proxy=None,
            *,
            headers: Dict,
            playwright_page: Optional[Page],
            cookie_dict: Dict,
    ):
        self.proxy = proxy
        self.timeout = timeout
        self.headers = headers
        self._host = "https://www.douyin.com"
        self.playwright_page = playwright_page
        self.cookie_dict = cookie_dict

    async def search_info_by_keyword(
            self,
            keyword: str,
            offset: int = 0,
            search_channel: SearchChannelType = SearchChannelType.GENERAL,
            sort_type: SearchSortType = SearchSortType.GENERAL,
            publish_time: PublishTimeType = PublishTimeType.UNLIMITED,
            search_id: str = "",
    ):
        """
        DouYin Web Search API
        :param keyword:
        :param offset:
        :param search_channel:
        :param sort_type:
        :param publish_time: ·
        :param search_id: ·
        :return:
        """
        query_params = {
            'search_channel': search_channel.value,
            'enable_history': '1',
            'keyword': keyword,
            'search_source': 'tab_search',
            'query_correct_type': '1',
            'is_filter_search': '0',
            'from_group_id': '7378810571505847586',
            'offset': offset,
            'count': '15',
            'need_filter_settings': '1',
            'list_type': 'multi',
            'search_id': search_id,
        }
        if sort_type.value != SearchSortType.GENERAL.value or publish_time.value != PublishTimeType.UNLIMITED.value:
            query_params["filter_selected"] = json.dumps({"sort_type": str(sort_type.value), "publish_time": str(publish_time.value)})
            query_params["is_filter_search"] = 1
            query_params["search_source"] = "tab_search"
        referer_url = f"https://www.douyin.com/search/{keyword}?aid=f594bbd9-a0e2-4651-9319-ebe3cb6298c1&type=general"
        headers = copy.copy(self.headers)
        headers["Referer"] = urllib.parse.quote(referer_url, safe=':/')
        return await self.get("/aweme/v1/web/general/search/single/", query_params, headers=headers)

    async def get(self, uri: str, params: Optional[Dict] = None, headers: Optional[Dict] = None):
        """
        GET请求
        """
        await self.__process_req_params(uri, params, headers)
        headers = headers or self.headers
        return await self.request(method="GET", url=f"{self._host}{uri}", params=params, headers=headers)

    async def request(self, method, url, **kwargs):
        async with httpx.AsyncClient(proxy=self.proxy) as client:
            response = await client.request(method, url, timeout=self.timeout, **kwargs)
        if response.text == "" or response.text == "blocked":
            utils.logger.error(f"request params incrr, response.text: {response.text}")
            raise Exception("account blocked")
        return response.json()


    async def __process_req_params(
            self,
            uri: str,
            params: Optional[Dict] = None,
            headers: Optional[Dict] = None,
            request_method="GET",
    ):

        if not params:
            return
        headers = headers or self.headers
        local_storage: Dict = await self.playwright_page.evaluate("() => window.localStorage")  # type: ignore
        common_params = {
            "device_platform": "webapp",
            "aid": "6383",
            "channel": "channel_pc_web",
            "version_code": "190600",
            "version_name": "19.6.0",
            "update_version_code": "170400",
            "pc_client_type": "1",
            "cookie_enabled": "true",
            "browser_language": "zh-CN",
            "browser_platform": "MacIntel",
            "browser_name": "Chrome",
            "browser_version": "125.0.0.0",
            "browser_online": "true",
            "engine_name": "Blink",
            "os_name": "Mac OS",
            "os_version": "10.15.7",
            "cpu_core_num": "8",
            "device_memory": "8",
            "engine_version": "109.0",
            "platform": "PC",
            "screen_width": "2560",
            "screen_height": "1440",
            'effective_type': '4g',
            "round_trip_time": "50",
            "webid": self.get_web_id(),
            "msToken": local_storage.get("xmst"),
        }
        params.update(common_params)
        query_string = urllib.parse.urlencode(params)

        # 20240927 a-bogus更新（JS版本）
        post_data = {}
        if request_method == "POST":
            post_data = params
        a_bogus = await self.get_a_bogus(uri, query_string, post_data, headers["User-Agent"], self.playwright_page)
        params["a_bogus"] = a_bogus

    async def get_a_bogus(self, url: str, params: str, post_data: dict, user_agent: str, page: Page = None):
        """
        获取a_bogus
        Returns:

        """
        sign_js_name = "sign_datail"
        douyin_sign_obj = execjs.compile(open('libs/douyin.js', encoding='utf-8-sig').read())
        if "/reply" in url:
            sign_js_name = "sign_reply"
        return douyin_sign_obj.call(sign_js_name, params, user_agent)

    async def pong(self, browser_context: BrowserContext) -> bool:
        local_storage = await self.playwright_page.evaluate("() => window.localStorage")
        if local_storage.get("HasUserLogin", "") == "1":
            return True

        _, cookie_dict = utils.convert_cookies(await browser_context.cookies())
        return cookie_dict.get("LOGIN_STATUS") == "1"

    def get_web_id(self):
        """
        生成随机的webid
        Returns:

        """

        def e(t):
            if t is not None:
                return str(t ^ (int(16 * random.random()) >> (t // 4)))
            else:
                return ''.join(
                    [str(int(1e7)), '-', str(int(1e3)), '-', str(int(4e3)), '-', str(int(8e3)), '-', str(int(1e11))]
                )

        web_id = ''.join(
            e(int(x)) if x in '018' else x for x in e(None)
        )
        return web_id.replace('-', '')[:19]