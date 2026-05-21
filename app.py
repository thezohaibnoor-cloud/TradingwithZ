from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/")
def home():
    return "🚀 TradingView Telegram Bot Running"

@app.route("/test")
def test():

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": "✅ Test message from Render bot"
    }

    response = requests.post(url, json=payload)

    return jsonify(response.json())

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.get_json(silent=True) or {}

    message = data.get(
        "message",
        "📈 TradingView Alert Triggered"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, json=payload)

    return jsonify({
        "status": "success",
        "telegram_status": response.status_code
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
