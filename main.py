from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def ildiz():
    return {"message": "Pandora AI bot server ishlayapti."}

@app.post("/webhook")
async def webhook(iltimos: Request):
    ma_lumotlar = await iltimos.json()
    print("Telegram'dan kelgan webhook:")
    print(ma_lumotlar)
    return {"kelib_tushdi": True}
