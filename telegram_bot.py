 import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = 

openai.api_key = OPENAI_API_KEY

async def handle_message(update: Update, context) -> None:
    user_input = update.message.text
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ],
        )
        reply = response["choices"][0]["message"]["content"]
        await update.message.reply_text(reply)
    except openai.error.PermissionError:
        await update.message.reply_text("Извините, доступ к этому сервису запрещен в вашей стране.")
    except Exception as e:
        await update.message.reply_text(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот запущен и ожидает сообщений...")
    application.run_polling()
