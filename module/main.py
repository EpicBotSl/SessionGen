import re
import uuid
import socket
import platform
import os
import random
import time
import math
import json
import string
import traceback
import psutil
import asyncio
import wget
import motor.motor_asyncio
import pymongo
import aiofiles
import datetime
from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *
from helper.decorators import humanbytes
from config import *
from database.db import Database
from asyncio import *
import heroku3
import requests
from helper.heroku_helper import HerokuHelper
from helper.fsub import forcesub
#--------------------------------------------------Db-------------------------------------------------#


async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : user is blocked\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"
        
#------------------------------Db End---------------------------------------------------------#       
        
Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"

DATABASE_URL=MONGO_URI
db = Database(DATABASE_URL, "Ss_bot"")

#╔════╗────────╔═══╗
#║╔╗╔╗║────────║╔══╝
#╚╝║║╠╩═╦══╦╗╔╗║╚══╦══╦╦══╗
#──║║║║═╣╔╗║╚╝║║╔══╣╔╗╠╣╔═╝
#──║║║║═╣╔╗║║║║║╚══╣╚╝║║╚═╗
#──╚╝╚══╩╝╚╩╩╩╝╚═══╣╔═╩╩══╝
#──────────────────║║
#──────────────────╚╝
#---------------------------Commands Start Epic-------------------------------------#


@app.on_message(filters.command("start"))
async def start(app, message):
    if await forcesub(app, message):
       return
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await app.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        if -1001741009206:
            await app.send_message(
                -1001741009206,
                f"#NEWUSER: \n\n**User:** [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n\**ID:**{message.from_user.id}\n Started @{BOT_USERNAME} !!",
            )
        else:
            logging.info(f"#NewUser :- Name : {message.from_user.first_name} ID : {message.from_user.id}")
    await message.delete()
    file_id = "CAADAgADuQIAAladvQq6Ay8ze3xA6gI"
    await app.send_sticker(message.chat.id, file_id)
    text = f"""
      ❣ᴍʏ ᴅᴇᴀʀ {message.from_user.mention} ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴇᴘɪᴄ ꜱᴛɪᴄᴋᴇʀ ʙᴏᴛ ⬗
    ❦ᴄʟɪᴄᴋ ᴛᴏ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴀʙᴏᴜᴛ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴍᴇ"""
    reply_markup = START_BUTTON  
    await message.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )
