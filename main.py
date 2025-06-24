from fastapi import FastAPI, Request
import requests

app = FastAPI()

BOT_TOKEN = "8022008632:AAG0mvhHUhLoWa52VmmnvvBndXqtubuvH1c"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.post("/webhook")
async def webhook_handler(req: Request):
    data = await req.json()
    print("📩 Telegramдан сўров:", data)

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = text = "Test: Pandora AI bot ishlayapti."

        try:
            response = requests.post(
                f"{TELEGRAM_API_URL}/sendMessage",
                json={"chat_id": chat_id, "text": text}
            )
            print("📤 Жавоб юборилди:", response.status_code, response.text)
        except Exception as e:
            print("❌ Telegram’га жавоб юборишда хатолик:", str(e))

    return {"ok": True}
