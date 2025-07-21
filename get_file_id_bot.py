from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "7523554808:AAE_G1oCYGVGbwwvOtjiCQFDBrUVcTlrdUY"

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.video:
        file_id = update.message.video.file_id
        await update.message.reply_text(f"🎥 file_id:\n{file_id}")
        print("📁 Terminalda file_id:", file_id)
    else:
        await update.message.reply_text("❗ Iltimos, kinoni video sifatida yuboring!")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.VIDEO, get_file_id))
print("✅ Bot ishga tushdi. Video yuboring — file_id chiqadi.")
app.run_polling()
