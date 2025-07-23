import asyncio
from fastapi import FastAPI, HTTPException
import uvicorn
from typing import List
import time

# 创建 FastAPI 应用
app = FastAPI()

# --------- 核心组件初始化 ----------
request_queue = asyncio.Queue(maxsize=20)  # 请求排队区
semaphore = asyncio.Semaphore(5)           # 控并发
rate = 3
capacity = 10
tokens = capacity
last_refill = asyncio.get_event_loop().time()

# 模拟数据库写入缓冲队列
db_queue = asyncio.Queue(maxsize=100)

# --------- 令牌桶 ----------
async def get_token():
    global tokens, last_refill
    while True:
        now = asyncio.get_event_loop().time()
        new_tokens = (now - last_refill) * rate
        tokens = min(capacity, tokens + new_tokens)
        last_refill = now

        if tokens >= 1:
            tokens -= 1
            return
        await asyncio.sleep(0.05)

# --------- 爬虫逻辑 ----------
async def do_spider_task(url):
    print(f"开始爬取: {url}")
    await asyncio.sleep(2)
    print(f"完成爬取: {url}")
    return {"url": url, "content": "模拟爬虫结果"}

# --------- worker：处理 request_queue ----------
async def request_worker():
    while True:
        url = await request_queue.get()
        await get_token()
        async with semaphore:
            result = await do_spider_task(url)
            await db_queue.put(result)
        request_queue.task_done()

# --------- db_worker：模拟异步批量入库 ----------
async def db_worker():
    while True:
        batch = []
        try:
            for _ in range(5):  # 每批最多取 5 个
                result = await asyncio.wait_for(db_queue.get(), timeout=1)
                batch.append(result)
        except asyncio.TimeoutError:
            pass

        if batch:
            await write_to_db(batch)

async def write_to_db(batch):
    print(f"批量写入数据库: {len(batch)} 条")
    await asyncio.sleep(0.5)  # 模拟数据库IO耗时

# --------- FastAPI接口 ----------
@app.post("/crawl")
async def crawl(urls: List[str]):
    if request_queue.qsize() + len(urls) > request_queue.maxsize:
        raise HTTPException(status_code=429, detail="排队已满")

    for url in urls:
        await request_queue.put(url)
    return {"message": f"已加入 {len(urls)} 个任务"}

# --------- 启动时初始化后台worker ----------
@app.on_event("startup")
async def startup():
    for _ in range(3):  # 启动3个爬虫worker
        asyncio.create_task(request_worker())
    asyncio.create_task(db_worker())  # 启动数据库worker

# --------- 启动服务 ----------
if __name__ == "__main__":
    uvicorn.run("crawler_half_prod:app", host="0.0.0.0", port=8000, reload=True)