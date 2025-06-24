from fastapi import FastAPI, Request
import requests

app = FastAPI()

BOT_TOKEN = "8022008632:AAG0mvhHUhLoWa52VmmnvvBndXqtubuvH1c"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.post("/webhook")
async def webhook_handler(req: Request):
    data = await req.json()
    print("Telegramдан сўров:", data)

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]

        if text.upper() == "BTC":
            signal_text = "📈 BTC Сигнали: 4H timeframe — Брейкаут назоратда! 🟢"
        else:
            signal_text = "✅ Pandora AI бот ишга тушди!"

        requests.post(
            f"{TELEGRAM_API_URL}/sendMessage",
            json={"chat_id": chat_id, "text": signal_text}
        )

    return {"ok": True}
