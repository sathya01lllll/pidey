# file: bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import json

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text and "videy.co" in text:
        with open("videos.json", "r+") as f:
            data = json.load(f)
            data.append({"user": update.effective_user.username, "text": text})
            f.seek(0)
            json.dump(data, f, indent=2)

app = ApplicationBuilder().token("7770257728:AAEJC6s80zxJaKRZRu8HZOSwx3UhXItf9ww").build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
