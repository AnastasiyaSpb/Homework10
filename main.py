from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5925647760:AAHvsVdgAlRk7Nk3dbZOfIqs9USjd1FkkV8").build()

app.add_handler(CommandHandler('search', search_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('add', add_command))

print('server start')

app.run_polling()

