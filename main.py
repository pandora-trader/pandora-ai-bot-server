if "message" in data:
    chat_id = data["message"]["chat"]["id"]
    text = data["message"]["text"]

    if text.upper() == "BTC":
        signal_text = "📈 BTC Сигнали: 4H timeframe — Брейкаут кузатиляпти! 🟢"
    else:
        signal_text = "✅ Pandora AI бот ишга тушди!"

    requests.post(
        f"{TELEGRAM_API_URL}/sendMessage",
        json={"chat_id": chat_id, "text": signal_text}
    )
