import asyncio
import time


async def task(name):
    print(f"{name} 开始")
    await asyncio.sleep(2)  # 模拟IO操作
    print(f"{name} 结束")

async def main():
    current_time = time.time()
    await asyncio.gather(
        task("任务1"),
        task("任务2"),
    )
    print(time.time()-current_time)

asyncio.run(main())