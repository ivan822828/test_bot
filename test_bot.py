import os
import logging
from flask import Flask
from telegram import Update
from telegram.ext import Updater, CommandHandler

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен из переменных окружения
TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    logger.error("❌ BOT_TOKEN не найден!")
    exit(1)

# Flask приложение
app = Flask(__name__)

# Обработчик команды /start
def start(update, context):
    update.message.reply_text("✅ Render работает! Бот запущен.")

# Настройка бота
updater = Updater(token=TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler("start", start))

# Запуск бота в фоновом режиме
updater.start_polling()
logger.info("✅ Бот запущен в режиме polling")

# Flask маршруты
@app.route('/')
def home():
    return "✅ Test Bot is running!"

@app.route('/health')
def health():
    return "OK", 200

# Запуск Flask
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)