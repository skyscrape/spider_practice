import asyncio
import time
from fastapi import FastAPI, HTTPException
import uvicorn
from typing import List

# FastAPI app初始化
app = FastAPI()

# === 全局状态预留 ===
class GlobalState:
    request_queue: asyncio.Queue
    db_queue: asyncio.Queue
    token_bucket: dict
    semaphore: asyncio.Semaphore
    db_pool: None

# ============ 生命周期初始化 ============
@app.on_event("startup")
async def startup_event():
    app.state.request_queue = asyncio.Queue(maxsize=20)
    app.state.db_queue = asyncio.Queue(maxsize=100)
    app.state.semaphore = asyncio.Semaphore(5)

    # 初始化令牌桶
    app.state.token_bucket = {
        "rate": 3, "capacity": 10,
        "tokens": 10,
        "last_refill": time.time()
    }

    # 启动核心worker
    for _ in range(3):
        asyncio.create_task(request_worker())

    asyncio.create_task(db_worker())
    asyncio.create_task(queue_alert_monitor())

# ============ 令牌桶控制 ============
async def get_token():
    tb = app.state.token_bucket
    while True:
        now = time.time()
        new_tokens = (now - tb['last_refill']) * tb['rate']
        tb['tokens'] = min(tb['capacity'], tb['tokens'] + new_tokens)
        tb['last_refill'] = now

        if tb['tokens'] >= 1:
            tb['tokens'] -= 1
            return
        await asyncio.sleep(0.05)

# ============ 爬虫逻辑 ============
async def do_spider_task(url):
    print(f"正在爬取: {url}")
    await asyncio.sleep(2)
    print(f"完成爬取: {url}")
    return {"url": url, "result": "模拟爬虫内容"}

# ============ 请求执行 worker ============
async def request_worker():
    while True:
        url = await app.state.request_queue.get()
        await get_token()
        async with app.state.semaphore:
            result = await do_spider_task(url)
            await app.state.db_queue.put(result)
        app.state.request_queue.task_done()

# ============ 模拟数据库入库 worker ============
async def db_worker():
    while True:
        batch = []
        try:
            for _ in range(5):
                result = await asyncio.wait_for(app.state.db_queue.get(), timeout=1)
                batch.append(result)
        except asyncio.TimeoutError:
            pass

        if batch:
            await write_to_db(batch)

async def write_to_db(batch):
    print(f"数据库写入 {len(batch)} 条: {batch}")
    await asyncio.sleep(0.5)

# ============ 积压监控 ============
async def queue_alert_monitor():
    while True:
        await asyncio.sleep(5)
        req_size = app.state.request_queue.qsize()
        db_size = app.state.db_queue.qsize()
        if req_size >= 15:
            print(f"⚠️ 请求队列积压: {req_size}")
        if db_size >= 80:
            print(f"⚠️ 数据库积压: {db_size}")

# ============ 对外API入口 ============
@app.post("/crawl")
async def crawl(urls: List[str]):
    if app.state.request_queue.qsize() + len(urls) > app.state.request_queue.maxsize:
        raise HTTPException(status_code=429, detail="排队已满")

    for url in urls:
        await app.state.request_queue.put(url)
    return {"message": f"成功加入 {len(urls)} 个任务"}

# ============ 启动服务 ============
if __name__ == "__main__":
    uvicorn.run("final_crawler:app", host="0.0.0.0", port=8000, reload=True)