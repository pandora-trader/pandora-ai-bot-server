from fastapi import FastAPI, Request
import requests

app = FastAPI()

BOT_TOKEN = "8022008632:AAF0NyLr-ALlaJaZ-oNOI8qSAoROuoJc_Qw"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.post("/webhook")
async def webhook_handler(req: Request):
    data = await req.json()
    print("Telegramдан сўров:", data)

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = "✅ Pandora AI бот ишга тушди!"
        requests.post(f"{TELEGRAM_API_URL}/sendMessage", json={"chat_id": chat_id, "text": text})

    return {"ok": True}
