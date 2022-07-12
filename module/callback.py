import traceback
from script import *
from module.main import *
from pyrogram import Client
from module.generate import *
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup
from module.generate import generate_session, ask_ques, buttons_ques


@Client.on_callback_query()  
async def tgm(bot, update):  
    if update.data == "add": 
        await update.answer(
             text="♻️Adding Soon.....",
        )
    elif update.data == "gen":
         await update.message.edit_text(
             text=ask_ques,
             reply_markup=InlineKeyboardMarkup(buttons_ques),
             disable_web_page_preview=True
         )
         await update.answer(
             text="🐥 Send Me your Choice 🐥",
         )
    elif update.data == "back":
         await update.message.edit_text(
             text=BACK_TXT,
             reply_markup=START_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🕊️ Welcome Back 🕊️",
         )
