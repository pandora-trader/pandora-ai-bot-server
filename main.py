import requests

TOKEN = "8022008632:AAF0NyLr-ALlaJaZ-oNOI8qSAoROuoJc_Qw"
API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@ilova.post("/webhook")
async def webhook(iltimos: Request):
    ma_lumotlar = await iltimos.json()
    print("Telegram'dan kelgan webhook:")
    print(ma_lumotlar)

    # Telegram'dан хабар юборган фойдаланувчини ID си
    user_id = ma_lumotlar["message"]["from"]["id"]
    msg = ma_lumotlar["message"]["text"]

    # Жавоб тайёрлаш
    javob = f"Салом! Сиз ёздингиз: {msg}"

    # Жавобни Telegram'га юбориш
    requests.post(API_URL, json={
        "chat_id": user_id,
        "text": javob
    })

    return {"kelib tushdi": True}
