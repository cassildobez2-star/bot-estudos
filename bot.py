import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

def ler_conteudo(nome):
    caminho = f"conteudos/{nome}.txt"
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            return f.read()
    return "Conteúdo não encontrado."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 Bot de Estudos\n\n"
        "Use:\n"
        "/matematica\n"
        "/fisica\n"
        "/portugues"
    )

async def matematica(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ler_conteudo("matematica"))

async def fisica(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ler_conteudo("fisica"))

async def portugues(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ler_conteudo("portugues"))

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("matematica", matematica))
app.add_handler(CommandHandler("fisica", fisica))
app.add_handler(CommandHandler("portugues", portugues))

app.run_polling()
