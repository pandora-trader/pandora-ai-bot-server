from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

BOT_TOKEN = os.getenv("BOT_TOKEN", "8022008632:AAF0NyLr-ALlaJaZ-oNOI8qSAoROuoJc_Qw")
URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.get("/")
async def root():
    return {"message": "Pandora AI bot server ishlayapti."}

@app.post("/webhook")
async def telegram_webhook(update: Request):
    data = await update.json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # Oddiy reply
        if text == "/start":
            reply = "👋 Assalomu alaykum! Pandora AI Trading bot ishga tushди."
        else:
            reply = "Siz yuborgan: " + text

        requests.post(f"{URL}/sendMessage", json={
            "chat_id": chat_id,
            "text": reply
        })

    return {"ok": True}
