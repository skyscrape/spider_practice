import asyncio
import random
from typing import List, Dict
from asyncio import Task
from client import DouYinApiClient
from douyin.field import PublishTimeType
from tools import utils
import config
from help import get_common_verify_params
from account_pool import AccountPool
from exception import DataFetchError

class DouYinCrawler:
    def __init__(self) -> None:
        self.dy_client = DouYinApiClient()

    async def main(self):
        utils.logger.info("[DouYinCrawler.async_initialize] Begin async initialize")
        # 风控参数生成
        self.dy_client.common_verfiy_params = await get_common_verify_params(
            config.DOUYIN_FIXED_USER_AGENT
        )

        # 账号池信息加载
        account_pool = AccountPool('dy')
        account_pool.load_accounts_from_xlsx("accounts_cookies.xlsx")
        # 从池子里拿账号
        accounts = account_pool.all_accounts()

        # 赋值给 client
        self.dy_client.account__pool = accounts

        await self.dy_client.update_account_info()
        await self.start()


    async def start(self) :
        utils.logger.info("[DouYinCrawler.search] Begin search douyin keywords")
        dy_limit_count = 10  # douyin limit page fixed value
        if config.CRAWLER_MAX_NOTES_COUNT < dy_limit_count:
            config.CRAWLER_MAX_NOTES_COUNT = dy_limit_count
        start_page = config.START_PAGE
        for keyword in config.KEYWORDS.split(","):
            utils.logger.info(f"[DouYinCrawler.search] Current keyword: {keyword}")
            page = 1
            dy_search_id = ""
            while (
                    page - start_page + 1
            ) * dy_limit_count <= config.CRAWLER_MAX_NOTES_COUNT:
                if page < start_page:
                    utils.logger.info(f"[DouYinCrawler.search] Skip {page}")
                    page += 1
                    continue
                try:
                    aweme_list: List[str] = []
                    utils.logger.info(
                        f"[DouYinCrawler.search] search douyin keyword: {keyword}, page: {page}"
                    )

                    # posts_res 即为搜索返还值
                    posts_res = await self.dy_client.search_info_by_keyword(
                        keyword=keyword,
                        offset=(page - 1) * dy_limit_count,
                        publish_time=PublishTimeType(config.PUBLISH_TIME_TYPE),
                        search_id=dy_search_id,
                    )


                    page += 1
                    if "data" not in posts_res:
                        utils.logger.error(
                            f"[DouYinCrawler.search] search douyin keyword: {keyword} failed，账号也许被风控了。"
                        )
                        # 更换账号信息
                        await self.dy_client.change_account()
                        continue

                    dy_search_id = posts_res.get("extra", {}).get("logid", "")
                    for post_item in posts_res.get("data"):
                        try:
                            aweme_info: Dict = (
                                    post_item.get("aweme_info")
                                    or post_item.get("aweme_mix_info", {}).get("mix_items")[
                                        0
                                    ]
                            )
                        except TypeError:
                            continue
                        aweme_list.append(aweme_info.get("aweme_id", ""))
                        # await douyin_store.update_douyin_aweme(aweme_item=aweme_info)

                    utils.logger.info(
                        f"[DouYinCrawler.search] keyword:{keyword}, aweme_list:{aweme_list}"
                    )
                    # await self.batch_get_note_comments(aweme_list)
                    # 更换账号信息
                    await self.dy_client.change_account()


                except Exception as ex:
                    utils.logger.error(
                        f"[DouYinCrawler.search] Search videos error: {ex}"
                    )
    async def batch_get_note_comments(self, aweme_list: List[str]) -> None:
        """
        Batch get note comments
        """
        if not config.ENABLE_GET_COMMENTS:
            utils.logger.info(
                f"[DouYinCrawler.batch_get_note_comments] Crawling comment mode is not enabled"
            )
            return

        task_list: List[Task] = []
        semaphore = asyncio.Semaphore(config.MAX_CONCURRENCY_NUM)
        for aweme_id in aweme_list:
            utils.logger.info(
                f"[DouYinCrawler.batch_get_note_comments] aweme_id: {aweme_id}"
            )
            task = asyncio.create_task(
                self.get_comments_async_task(aweme_id, semaphore), name=aweme_id
            )
            task_list.append(task)
        if len(task_list) > 0:
            await asyncio.wait(task_list)

    async def get_comments_async_task(
            self, aweme_id: str, semaphore: asyncio.Semaphore
    ) -> None:
        async with semaphore:
            try:
                # 将关键词列表传递给 get_aweme_all_comments 方法
                comments = await self.dy_client.get_aweme_all_comments(
                    aweme_id=aweme_id,
                    crawl_interval=random.random(),
                    callback=None,
                )
                utils.logger.info(
                    f"[DouYinCrawler.get_comments_async_task] comments: {comments} comments have all been obtained and filtered ..."
                )
            except DataFetchError as e:
                utils.logger.error(
                    f"[DouYinCrawler.get_comments_async_task] aweme_id: {aweme_id} get comments failed, error: {e}"
                )

if __name__ == "__main__":
    crawler = DouYinCrawler()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(crawler.main())