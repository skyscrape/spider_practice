from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def home():
    return {"user_id": 1002}

@app.get("/shop")
async def shop():
    return {"shop": "商品信息"}

if __name__ == "__main__":
    uvicorn.run("quick_start:app", host="127.0.0.1", port=8080, reload=True)
