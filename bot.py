import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Token vindo das variáveis do Railway
TOKEN = os.getenv("BOT_TOKEN")

# Função para ler conteúdos
def ler_conteudo(nome):
    caminho = f"conteudos/{nome}.txt"
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            return f.read()
    return "❌ Conteúdo não encontrado."

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 *Bot de Estudos*\n\n"
        "Escolha uma matéria:\n\n"
        "📐 Matemática\n"
        "/matematica_basica\n"
        "/matematica_intermediaria\n\n"
        "⚛️ Física\n"
        "/fisica_basica\n"
        "/fisica_intermediaria\n\n"
        "📖 Português\n"
        "/portugues_basico\n"
        "/portugues_intermediario",
        parse_mode="Markdown"
    )

# ===== MATEMÁTICA =====
async def matematica_basica(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ler_conteudo("matematica_basica"))

async def matematica_intermediaria(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ler_conteudo("matematica_intermediaria"))

# ===== FÍSICA =====
async def fisica_basica(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ler_conteudo("fisica_basica"))

async def fisica_intermediaria(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ler_conteudo("fisica_intermediaria"))

# ===== PORTUGUÊS =====
async def portugues_basico(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ler_conteudo("portugues_basico"))

async def portugues_intermediario(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ler_conteudo("portugues_intermediario"))

# ===== APP =====
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Comandos principais
    app.add_handler(CommandHandler("start", start))

    # Matemática
    app.add_handler(CommandHandler("matematica_basica", matematica_basica))
    app.add_handler(CommandHandler("matematica_intermediaria", matematica_intermediaria))

    # Física
    app.add_handler(CommandHandler("fisica_basica", fisica_basica))
    app.add_handler(CommandHandler("fisica_intermediaria", fisica_intermediaria))

    # Português
    app.add_handler(CommandHandler("portugues_basico", portugues_basico))
    app.add_handler(CommandHandler("portugues_intermediario", portugues_intermediario))

    print("🤖 Bot de estudos rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
