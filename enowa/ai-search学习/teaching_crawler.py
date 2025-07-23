import asyncio
import random
import time
from typing import List
from fastapi import FastAPI, Request
import uvicorn

# =============== 模拟依赖组件 ================
class TokenBucket:
    """限流用令牌桶"""
    def __init__(self, rate: int, capacity: int):
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.last_refresh = asyncio.get_event_loop().time()

    async def get_token(self):
        while True:
            now = asyncio.get_event_loop().time()
            new_tokens = (now - self.last_refresh) * self.rate
            self.tokens = min(self.capacity, self.tokens + new_tokens)
            self.last_refresh = now
            if self.tokens >= 1:
                self.tokens -= 1
                return
            await asyncio.sleep(1 / self.rate)

# 模拟缓存（真实项目用 ES/Redis）
cache = set()

# 模拟数据库队列
class DBQueue:
    def __init__(self):
        self.queue = asyncio.Queue()

    async def put(self, item):
        await self.queue.put(item)

    async def worker(self):
        while True:
            item = await self.queue.get()
            print(f"✅ 数据写入数据库：{item}")
            await asyncio.sleep(0.1)  # 模拟写库耗时

# 模拟爬虫
async def fake_crawler(url: str):
    await asyncio.sleep(random.uniform(0.5, 1.5))  # 模拟抓取耗时
    return f"内容_{url}"

# ============ 核心业务逻辑 ==============

app = FastAPI()
token_bucket = TokenBucket(rate=5, capacity=10)
db_queue = DBQueue()

@app.on_event("startup")
async def startup():
    # 启动数据库写入后台任务
    asyncio.create_task(db_queue.worker())
    print("✅ 爬虫服务启动完成")

@app.post("/crawl/")
async def crawl_api(request: Request):
    data = await request.json()
    urls: List[str] = data.get("urls", [])

    print(f"🚀 收到新请求：{urls}")

    responses = []

    for url in urls:
        # 先查缓存
        if url in cache:
            responses.append(f"缓存命中: {url}")
            continue

        # 排队限流
        await token_bucket.get_token()

        # 爬取
        content = await fake_crawler(url)
        responses.append(content)
        cache.add(url)

        # 异步写库
        await db_queue.put({"url": url, "content": content})

    return {"results": responses}

# ============== 启动入口 ================
if __name__ == "__main__":
    uvicorn.run("teaching_crawler:app", host="0.0.0.0", port=8000, reload=True)