from fastapi import FastAPI, Request

ilova = FastAPI()

@ilova.get("/")
async def ildiz():
    return {"message": "Pandora AI bot server ishlayapti."}

@ilova.post("/webhook")
async def webhook(iltimos: Request):
    ma'lumotlar = await iltimos.json()
    print("Telegram'dan kelgan webhook:")
    print(ma'lumotlar)
    return {"kelib tushdi": True}
