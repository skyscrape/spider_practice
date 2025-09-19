import asyncio
import copy
import json
import traceback
import urllib

import execjs
import httpx
from tenacity import stop_after_attempt, wait_fixed, retry, RetryError
from config import PER_NOTE_MAX_COMMENTS_COUNT
from exception import DataFetchError
from help import CommonVerfiyParams
from typing import Any, Callable, Dict, List, Optional, Union
import config
from account_pool import AccountInfoModel
from tools import utils
import field
import urllib.parse

class DouYinApiClient:
    def __init__(
            self,
            timeout: int = 10,
            user_agent: str = None,
            common_verfiy_params: CommonVerfiyParams = None,
            account__pool = None,
    ):
        """
        dy client constructor
        Args:
            timeout: 请求超时时间配置
            user_agent: 自定义的User-Agent
            account__pool: 账号池管理器
            common_verfiy_params: 通用验证参数模型
        """
        self.timeout = timeout
        self._user_agent = user_agent or config.DOUYIN_FIXED_USER_AGENT
        self.common_verfiy_params = common_verfiy_params
        self.account_info: Optional[AccountInfoModel] = None
        self.account__pool = account__pool
        self.index_pool = 0


    @property
    def _headers(self):
        return {
            "Content-Type": "application/json;charset=UTF-8",
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9",
            "Cookie": self._cookies,
            "origin": "https://www.douyin.com",
            "referer": "https://www.douyin.com/discover/",
            "user-agent": self._user_agent,
        }

    @property
    def _common_params(self):
        return {
            "device_platform": "webapp",
            "aid": "6383",
            "channel": "channel_pc_web",
            "publish_video_strategy_type": 2,
            "update_version_code": 170400,
            "pc_client_type": 1,
            "version_code": 170400,
            "version_name": "17.4.0",
            "cookie_enabled": "true",
            "screen_width": 2560,
            "screen_height": 1440,
            "browser_language": "zh-CN",
            "browser_platform": "MacIntel",
            "browser_name": "Chrome",
            "browser_version": "135.0.0.0",
            "browser_online": "true",
            "engine_name": "Blink",
            "engine_version": "135.0.0.0",
            "os_name": "Mac+OS",
            "os_version": "10.15.7",
            "cpu_core_num": 8,
            "device_memory": 8,
            "platform": "PC",
            "downlink": 4.45,
            "effective_type": "4g",
            "round_trip_time": 100,
        }

    @property
    def _verify_params(self):
        return {
            "webid": self.common_verfiy_params.webid,
            "msToken": self.common_verfiy_params.ms_token,
        }

    @property
    def _cookies(self):
        return self.account_info.cookies

    async def update_account_info(self):

        # 如果有账号池，遍历所有账号进行测试
        if self.account__pool:  # 注意这里参数名是 account__pool（两个下划线）
            all_accounts = self.account__pool  # 假设AccountPool有此方法
            valid_accounts = []

            for account in all_accounts:

                # 临时设置当前账号进行测试
                self.account_info = account
                is_valid = await self.pong()

                if is_valid:
                    valid_accounts.append(account)
                    utils.logger.info(
                        f"[DouYinApiClient.update_account_info] Account {account.account_name} is valid"
                    )
                else:
                    utils.logger.info(
                        f"[DouYinApiClient.update_account_info] Account {account.account_name} is invalid"
                    )

            self.account__pool = valid_accounts
            self.account_info = self.account__pool[self.index_pool%len(self.account__pool)]
            self.index_pool += 1
            utils.logger.info(
                f"[DouYinApiClient.update_account_info] Valid accounts: {len(valid_accounts)}/{len(all_accounts)}"
            )

    async def change_account(self):
        self.account_info = self.account__pool[self.index_pool%len(self.account__pool)]
        self.index_pool += 1

    async def pong(self) -> bool:
        """
        测试接口是否可用，最多重试3次
        Returns:
            bool: 账号是否有效
        """
        try:
            res = await self.query_user_self_info()
            if res and res.get("user_uid") and res.get("id"):
                # 这个res中会返回当前登录用户的相关信息，其中包含了：user_agent,则更新当前的user_agent
                if res.get("user_agent"):
                    self._user_agent = res.get("user_agent")
                return True
        except Exception as e:
            utils.logger.error(
                f"[DouYinApiClient.pong] pong failed, query user self response: {e}"
            )
        return False


    @retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
    async def query_user_self_info(self) -> Dict:
        """
        查询用户自己的信息
        Returns:

        """
        uri = "/aweme/v1/web/query/user/"
        params = {}
        params.update(self._common_params)
        params.update(self._verify_params)
        # params = await self._pre_url_params(uri, params)
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{config.DOUYIN_API_URL}{uri}", params=params, headers=self._headers
            )

        return response.json()


    async def search_info_by_keyword(
            self,
            keyword: str,
            offset: int = 0,
            search_channel: field.SearchChannelType = field.SearchChannelType.GENERAL,
            sort_type: field.SearchSortType = field.SearchSortType.GENERAL,
            publish_time: field.PublishTimeType = field.PublishTimeType.UNLIMITED,
            search_id: str = "",
    ):
        """
        搜索信息
        Args:
            keyword: 搜索关键字
            offset: 分页偏移量
            search_channel: 搜索渠道
            sort_type: 排序类型
            publish_time: 发布时间
            search_id: 搜索ID

        Returns:

        """
        query_params = {
            "search_channel": search_channel.value,
            "enable_history": "1",
            "keyword": keyword,
            "search_source": "tab_search",
            "query_correct_type": "1",
            "is_filter_search": "0",
            "from_group_id": "7378810571505847586",
            "offset": offset,
            "count": "10",
            "need_filter_settings": "1",
            "list_type": "multi",
            "search_id": search_id,
        }
        if (
                sort_type.value != field.SearchSortType.GENERAL.value
                or publish_time.value != field.PublishTimeType.UNLIMITED.value
        ):
            query_params["filter_selected"] = json.dumps(
                {
                    "sort_type": str(sort_type.value),
                    "publish_time": str(publish_time.value),
                },
                separators=(",", ":"),
            )
            query_params["is_filter_search"] = 1
            query_params["search_source"] = "tab_search"
        return await self.get("/aweme/v1/web/general/search/single/", query_params)

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
    async def request(self, method, url, **kwargs):
        """
        封装httpx的公共请求方法，对请求响应做一些处理
        Args:
            method: 请求方法
            url: 请求的URL
            **kwargs: 其他请求参数，例如请求头、请求体等

        Returns:

        """
        # await self.check_ip_expired()
        need_return_ori_response = kwargs.get("return_response", False)
        if "return_response" in kwargs:
            del kwargs["return_response"]

        if "headers" not in kwargs:
            kwargs["headers"] = self._headers

        async with httpx.AsyncClient() as client:
            response = await client.request(method, url, timeout=self.timeout, **kwargs)

        if need_return_ori_response:
            return response

        try:
            if response.text == "" or response.text == "blocked":
                utils.logger.error(
                    f"request params incrr, response.text: {response.text}"
                )
                raise Exception("account blocked")
            return response.json()
        except Exception as e:
            raise DataFetchError(f"{e}, {response.text}")


    async def _pre_url_params(self, uri: str, url_params: Dict) -> Dict:
        """
        预处理URL参数，获取a_bogus参数
        Args:
            uri:
            url_params:

        Returns:

        """
        final_url_params = copy.copy(url_params)
        final_url_params.update(self._common_params)
        final_url_params.update(self._verify_params)
        query_params = urllib.parse.urlencode(final_url_params)

        dy_abogus = await self.gen_abogus(uri, query_params, self._user_agent, self._cookies)

        final_url_params["a_bogus"] = dy_abogus
        return final_url_params

    async def gen_abogus(self, uri, query_params, user_agent, cookies):
        """
        生成a_bogus参数
        Returns:

        """
        douyin_sign_obj = execjs.compile(open('douyin.js', encoding='utf-8').read())
        a_bogus = douyin_sign_obj.call('sign_datail', query_params, user_agent)
        return a_bogus

    async def get(self, uri: str, params: Optional[Dict] = None, **kwargs):
        """
        GET请求
        Args:
            uri: 请求的URI
            params: 请求参数

        Returns:

        """
        try:
            params = await self._pre_url_params(uri, params)
            return await self.request(
                method="GET", url=f"{config.DOUYIN_API_URL}{uri}", params=params, **kwargs
            )
        except RetryError as e:
            # 获取原始异常
            original_exception = e.last_attempt.exception()
            traceback.print_exception(
                type(original_exception),
                original_exception,
                original_exception.__traceback__,
            )
            utils.logger.error(
                f"[DouYinApiClient.get] 重试了3次: {uri} 请求，均失败了，尝试更换账号再次发起重试"
            )

            # 如果重试了3 次都还是异常了，那么尝试更换账号信息

            #
            self.index_pool = 0
            await self.update_account_info()

            params = await self._pre_url_params(uri, params)
            return await self.request(
                method="GET", url=f"{config.DOUYIN_API_URL}{uri}", params=params, **kwargs
            )
    async def get_aweme_all_comments(
            self,
            aweme_id: str,
            crawl_interval: float = 1.0,
            callback: Optional[Callable] = None,
    ):
        """
        获取视频的所有评论
        Args:
            aweme_id: 视频ID
            crawl_interval: 延时

        Returns:

        """
        # 分页游标
        comments_cursor = 0
        comments_res = await self.get_aweme_comments(aweme_id, comments_cursor)
        comments = comments_res.get("comments")

        if not comments:
            utils.logger.info(f"[DouYinApiClient.get_aweme_all_comments] aweme_id:{aweme_id} 获取的评论为空")
            return None

        results = await self.pre_comments(comments, aweme_id)
        await asyncio.sleep(crawl_interval)

        return results

    async def pre_comments(self, comments, aweme_id):
        result = []
        for comment_item in comments:
            result_item = {}
            user_info = comment_item.get("user", {})
            user_info_uid = user_info.get("uid")
            user_info_short_id = user_info.get("short_id")
            user_info_nickname = user_info.get("nickname")
            user_info_avatar_thumb = user_info.get("avatar_thumb", {})
            comment_id = comment_item.get("cid", 0)
            digg_count = comment_item.get("digg_count", 0)
            text = comment_item.get("text")
            create_time = comment_item.get("create_time")
            reply_comment_total = comment_item.get("reply_comment_total", 0)
            ip_label = comment_item.get("ip_label", "")
            result_item = {
                "aweme_id": aweme_id,
                "comment_id": comment_id,
                "content": text,
                "create_time": create_time,
                "ip_location": ip_label,
                "user_info_avatar_thumb": user_info_avatar_thumb,
                "digg_count": digg_count,
                "reply_comment_total": reply_comment_total,
                "user_id": user_info_uid,
                "short_user_id": user_info_short_id,
                "user_unique_id": user_info_nickname,
             }
            result.append(result_item)

        return result


    async def get_aweme_comments(self, aweme_id: str, cursor: int = 0):
        """
        获取帖子的评论
        Args:
            aweme_id: 视频ID
            cursor: 分页游标

        Returns:

        """
        uri = "/aweme/v1/web/comment/list/"
        params = {
            "aweme_id": aweme_id,
            "cursor": cursor,
            "count": 20,
            "item_type": 0,
            "verifyFp": self.common_verfiy_params.verify_fp,
            "fp": self.common_verfiy_params.verify_fp,
        }
        params.update(self._verify_params)
        keywords = ''
        referer_url = (
                "https://www.douyin.com/search/"
                + keywords
                + "?aid=3a3cec5a-9e27-4040-b6aa-ef548c2c1138&publish_time=0&sort_type=0&source=search_history&type=general"
        )
        headers = copy.copy(self._headers)
        headers["Referer"] = urllib.parse.quote(referer_url, safe=":/")
        return await self.get(uri, params, headers=headers)