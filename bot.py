import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💰 Заработок", callback_data="earn")],
        [InlineKeyboardButton("🔮 Эзотерика", callback_data="magic")],
        [InlineKeyboardButton("🤖 Технологии", callback_data="ai")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите категорию:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "earn":
        keyboard = [
            [InlineKeyboardButton("Менеджер маркетплейсов", url="https://site.ru/marketplace")],
            [InlineKeyboardButton("Специалист по нейросетям", url="https://site.ru/ai")],
            [InlineKeyboardButton("🔙 Назад", callback_data="back")]
        ]
        await query.edit_message_text("Курсы по заработку:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "magic":
        keyboard = [
            [InlineKeyboardButton("Таролог", url="https://site.ru/tarot")],
            [InlineKeyboardButton("Астролог", url="https://site.ru/astro")],
            [InlineKeyboardButton("🔙 Назад", callback_data="back")]
        ]
        await query.edit_message_text("Эзотерические курсы:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "ai":
        keyboard = [
            [InlineKeyboardButton("Специалист по нейросетям", url="https://site.ru/ai")],
            [InlineKeyboardButton("🔙 Назад", callback_data="back")]
        ]
        await query.edit_message_text("Технологические курсы:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "back":
        await start(update, context)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()
