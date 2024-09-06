from flask import Flask, request
from telegram import Bot

app = Flask(__name__)


TELEGRAM_BOT_TOKEN = '6429026610:AAF7ys0lji3PVPYHX9oRC-MAOjC3Dha_6B4'
CHAT_ID = '4599006896'  

bot = Bot(token=TELEGRAM_BOT_TOKEN)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/webhook", methods=["POST"])
def webhook():
    if request.method == "POST":
        data = request.json
        print(f"Received webhook data: {data}")

        # Пример сообщения, отправляемого в Telegram
        message = f"Webhook received:\n{data}"
        bot.send_message(chat_id=CHAT_ID, text=message)

        return "Webhook received!", 200

if __name__ == "__main__":
    app.run(debug=True)


