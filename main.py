from fastapi import FastAPI, Request

app = FastAPI()  # <-- avvalgidek 'ilova' emas

@app.get("/")
async def ildiz():
    return {"message": "Pandora AI bot server ishlayapti."}

@app.post("/webhook")
async def webhook(iltimos: Request):
    ma'lumotlar = await iltimos.json()
    print("Telegram'dan kelgan webhook:")
    print(ma'lumotlar)
    return {"kelib tushdi": True}
