import os

print("✅ ENV variables:", dict(os.environ))  # 👈 bu terminalda TOKEN ko‘rinadimi tekshiradi

TOKEN = "7523554808:AAHJqaAd59NndnsjAUk9XfnitlviHDFVM-I"  # ← Tokenni shu yerga yozing (qo‘shtirnoq ichida)

print("TOKEN:", TOKEN)


KINOLAR = {
    "1": "BAACAgIAAxkBAAMvaH4hiOAUwaM6EqjB8i4RW_BZHJMAAlV2AAIP9PFL4MoQwuLSHcc2BA",
    "2": "BAACAgIAAxkBAAMvaH4hiOAUwaM6EqjB8i4RW_BZHJMAAlV2AAIP9ayqV-ckfI",
    "3": "BAACAgQAAxkBAAIEeWZp3"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎬 Salom! Kino kodini yozing (1, 2, 3).")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = update.message.text.strip()
    if txt in KINOLAR:
        await update.message.reply_video(video=KINOLAR[txt], caption="🎥 Mana kino!")
    else:
        await update.message.reply_text("🚫 Kod topilmadi.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("✅ Bot ishga tushdi.")
app.run_polling()
