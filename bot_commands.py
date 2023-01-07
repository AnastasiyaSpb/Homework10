from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import json
import data_base as bd
import methods as m

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/search и имя для поиска информации\n/add и фамилию, имя, телефон комментарий через пробел для добавления информации')

async def add_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    add_info = msg.split()
    res = add_info[1] + "\n" + add_info[2] + "\n" + add_info[3] + "\n" + add_info[4] + "\n"
    bd.add_data(res)
    await update.message.reply_text(f'Информация добавлена')

async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    lets_find = msg.split()
    res = m.search_data(bd.create_dict(), lets_find[1])
    await update.message.reply_text(f'{res[0][0]}\n{res[0][1]}\n{res[0][2]}\n{res[0][3]}')