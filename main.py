import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ✅ Token .env yoki Railway Environment Variables ichida saqlanadi
TOKEN = os.getenv("7523554808:AAE_G1oCYGVGbwwvOtjiCQFDBrUVcTlrdUY")

# Kino kodlari va file_id'lari
KINOLAR = {
    "1": "BAACAgIAAxkBAAMvaH4hiOAUwaM6EqjB8i4RW_BZHJMAAlV2AAIP9PFL4MoQwuLSHcc2BA",
    "2": "BAACAgIAAxkBAAMvaH4hiOAUwaM6EqjB8i4RW_BZHJMAAlV2AAIP9PFL4MoQwuLSHcc2BA",  # ← 2-kino
    "3": "BAACAgQAAxkBAAIEeWZp3"  # ← 3-kino
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎬 Salom! Kanaldagi kino kodini yozing (masalan: 1, 2, 3)")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if text in KINOLAR:
        file_id = KINOLAR[text]
        await update.message.reply_video(video=file_id, caption="🎥 Mana siz so‘ragan kino!")
    else:
        await update.message.reply_text("🚫 Kod topilmadi. To‘g‘ri kod yozganingizga ishonch hosil qiling.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("✅ Bot ishga tushdi.")
app.run_polling()
