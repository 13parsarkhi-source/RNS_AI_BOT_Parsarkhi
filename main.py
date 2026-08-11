import os
from flask import Flask
from rubka import Robot

app = Flask(__name__)

TOKEN = os.environ.get("RUBIKA_TOKEN")

if not TOKEN:
    raise RuntimeError("RUBIKA_TOKEN is not set")

bot = Robot(token=TOKEN)


@app.route("/")
def home():
    return "Rubika Bot is running!"


@bot.on_message()
def handle_message(bot, message):
    text = getattr(message, "text", "") or ""

    if text == "/start":
        message.reply(
            "سلام 👋\n"
            "ربات روبیکا با موفقیت فعال شد."
        )

    elif text == "/test":
        message.reply("✅ ربات فعال است.")


if __name__ == "__main__":
    bot.run()
