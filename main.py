from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("TOKEN").build()

app.add_handler(CommandHandler('search', search_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('add', add_command))

print('server start')

app.run_polling()

