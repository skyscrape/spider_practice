# ws_server.py
import asyncio
import websockets
import json

# 可选：记录接收到的 cookie
received_cookies = []

# 客户端连接后的处理逻辑
async def handler(websocket, path):
    print("✅ 新客户端已连接")

    try:
        async for message in websocket:
            print(f"📩 收到消息: {message}")

            try:
                data = json.loads(message)
                if data.get("type") == "zse_ck":
                    zse_value = data["value"]
                    received_cookies.append(zse_value)
                    print(f"🎯 捕获到 __zse_ck: {zse_value}")

                    # 可选：回传确认信息
                    await websocket.send("✅ 已接收到 __zse_ck")
                else:
                    await websocket.send("⚠️ 未知数据类型")
            except Exception as parse_err:
                print(f"❌ JSON 解析失败: {parse_err}")
                await websocket.send(f"[ERROR] JSON parse error: {str(parse_err)}")

    except websockets.ConnectionClosed:
        print("🔌 客户端已断开连接")

# 启动 WebSocket 服务
async def main():
    async with websockets.serve(handler, "127.0.0.1", 8080):
        print("🚀 WebSocket 服务器启动中，监听地址: ws://127.0.0.1:8080")
        await asyncio.Future()  # 永久挂起，等待连接

if __name__ == "__main__":
    asyncio.run(main())