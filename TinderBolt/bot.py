from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler

from gpt import *
from util import *

async def start(update, context):
    text = load_message("main")
    await send_photo(update, context, "main")
    await send_text(update, context, text)


async def hello(update, context):
    await send_text(update, context, "*Привет*")
    await send_text(update, context, "_Как дела?_")
    await send_text(update, context, "Вы написали: " + update.message.text)
    await send_photo(update, context, "avatar_main")
    await send_text_buttons(update, context, "Запустить процесс?",
                            {"start":"Запустить", "stop":"Остановить"})


async def hello_buttons(update, context):
    query = update.callback_query.data
    if query == "start":
        await send_text(update, context, "*Процесс запущен*")
    else:
        await send_text(update, context, "_Процесс остановлен_")


app = ApplicationBuilder().token("6954969829:AAGl8j9a5agzkM8U9s8TQCcIvgYDkYTwAfI").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello))
app.add_handler(CallbackQueryHandler(hello_buttons))
app.run_polling()
