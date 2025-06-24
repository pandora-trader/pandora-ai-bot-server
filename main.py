from fastapi import FastAPI, Request
import requests

app = FastAPI()

# Telegram Bot Token (хақиқий токен қўйилган)
BOT_TOKEN = "8022008632:AAF0NyLr-ALlaJaZ-oNOt8qSaORouJc_QvM"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

# Webhook URL орқали POST сўровларини қабул қилади
@app.post("/webhook")
async def webhook_handler(req: Request):
    data = await req.json()
    print("Telegramдан сўров:", data)

    # Агар хабар бор бўлса, жавоб қайтарилади
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = "✅ Pandora AI бот ишга тушди!"
        requests.post(
            f"{TELEGRAM_API_URL}/sendMessage",
            json={"chat_id": chat_id, "text": text}
        )

    return {"ok": True}
