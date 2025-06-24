from fastapi import FastAPI, Request

ilova = FastAPI()

@ilova.get("/")
async def ildiz():
    return {"message": "Pandora AI bot server ishlayapti."}

@ilova.post("/webhook")
async def webhook(iltimos: Request):
    ma_lumotlar = await iltimos.json()
    print("Telegram'dan kelgan webhook:")
    print(ma_lumotlar)
    return {"kelib tushdi": True}
