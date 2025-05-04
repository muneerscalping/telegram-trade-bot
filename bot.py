from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8108406151:AAHHNEm0ppv_0RRbGqpJiK21wwYp3nEjXWg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً بك في Scalpingtrade_bot!\nأرسل /signal للحصول على توصية اليوم.")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "توصية اليوم:\n\n"
        "الذهب (XAUUSD)\n"
        "شراء من: 2325\n"
        "TP1: 2330\n"
        "TP2: 2336\n"
        "TP3: 2345\n"
        "SL: 2318\n\n"
        "داوجونز (US30)\n"
        "بيع من: 39100\n"
        "TP1: 39000\n"
        "TP2: 38900\n"
        "TP3: 38800\n"
        "SL: 39250"
    )
    await update.message.reply_text(message)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))
app.run_polling()
