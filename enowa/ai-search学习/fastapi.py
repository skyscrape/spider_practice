import asyncio
from fastapi import FastAPI, HTTPException
import uvicorn
from typing import List

# 初始化 FastAPI 应用
app = FastAPI()

# 初始化核心控制器
request_queue = asyncio.Queue(maxsize=10)  # 请求排队最大容量
semaphore = asyncio.Semaphore(3)           # 最大并发 3 个任务
rate = 2                                    # 每秒放 2 个令牌
capacity = 5
tokens = capacity
last_refill = asyncio.get_event_loop().time()

# 简化令牌桶限流逻辑
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
        await asyncio.sleep(0.1)

# 模拟爬虫任务
async def do_spider_task(url):
    print(f"开始爬取: {url}")
    await asyncio.sleep(2)  # 爬虫耗时模拟
    print(f"完成爬取: {url}")
    return {"url": url, "status": "done"}

# 核心调度逻辑：从队列中取任务执行
async def worker():
    while True:
        url = await request_queue.get()
        await get_token()  # 拿令牌限速
        async with semaphore:  # 控并发
            await do_spider_task(url)
        request_queue.task_done()

# 启动背景任务 worker
@app.on_event("startup")
async def startup_event():
    for _ in range(3):  # 启动3个worker并发处理
        asyncio.create_task(worker())

# 提供外部请求接口
@app.post("/crawl")
async def crawl(urls: List[str]):
    if request_queue.qsize() + len(urls) > request_queue.maxsize:
        raise HTTPException(status_code=429, detail="排队已满，稍后重试")

    for url in urls:
        await request_queue.put(url)
    return {"message": f"已加入队列: {len(urls)} 个任务"}

# 运行服务
if __name__ == "__main__":
    uvicorn.run("simple_crawler:app", host="0.0.0.0", port=8000, reload=True)