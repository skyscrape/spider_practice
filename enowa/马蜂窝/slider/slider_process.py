# caller_script.py
import asyncio
from sliderDate_generate import run

async def main():
    result = await run()
    if result:
        print("✅ 获取 JSON 成功：")
        print(result)
    else:
        print("❌ 未成功获取 JSON")

asyncio.run(main())