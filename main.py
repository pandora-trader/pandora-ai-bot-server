from fastapi import FastAPI, Request
import logging

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Pandora AI bot server ishlayapti."}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    logging.info(f"Kelgan webhook: {data}")
    return {"ok": True}
