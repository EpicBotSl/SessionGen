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
from script import *
from helper.heroku_helper import HerokuHelper
from helper.fsub import forcesub
from root import *
from database.check_user import *
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
db = Database(DATABASE_URL, "session_bot")

#╔════╗────────╔═══╗
#║╔╗╔╗║────────║╔══╝
#╚╝║║╠╩═╦══╦╗╔╗║╚══╦══╦╦══╗
#──║║║║═╣╔╗║╚╝║║╔══╣╔╗╠╣╔═╝
#──║║║║═╣╔╗║║║║║╚══╣╚╝║║╚═╗
#──╚╝╚══╩╝╚╩╩╩╝╚═══╣╔═╩╩══╝
#──────────────────║║
#──────────────────╚╝
#---------------------------Commands Start Epic-------------------------------------#

client = Client

@Client.on_message(filters.command("start"))
async def start(client, message):
    if await forcesub(client, message):
       return
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await client.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        if -1001741009206:
            await client.send_message(
                -1001741009206,
                f"#NEWUSER: \n\n**User:** [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n\**ID:**{message.from_user.id}\n Started @{BOT_USERNAME} !!",
            )
        else:
            logging.info(f"#NewUser :- Name : {message.from_user.first_name} ID : {message.from_user.id}")
    await message.delete()
    file_id = "CAADBQADbgUAAsyaaFZB8CvoDrUN_AI"
    await client.send_sticker(message.chat.id, file_id)
    text = f"""
      ❣ʜɪ {message.from_user.mention} 
   ⏦ɪ ᴀᴍ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴇᴛᴏʀ ʙᴏᴛ ⏦
🍁ɪ ᴄᴀɴ ɢᴇɴᴇʀᴇʀᴀᴛᴇ :

        🌀**ᴘʏʀᴏɢʀᴀᴍ**
        🌀**ᴛᴇʟᴇᴛʜᴏɴ**
        🌀**ᴘʏʀᴏɢʀᴀᴍ ᴠ2**

ꜱᴇꜱꜱɪᴏɴꜱ✓

🌍ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ
☔ᴘʀᴏᴊᴇᴄᴛ ʙʏ : [ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ](https://t.me/EpicBotsSl)"""
    reply_markup = START_BUTTON  
    await message.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )

@Client.on_message(filters.command("logs"))
async def giblog(bot, message):
    if message.from_user.id not in AUTH_USERS:
        await message.delete()
        return
    process = await message.reply_text( "`Trying To Fetch Logs....`")
    herokuHelper = HerokuHelper(HEROKU_APP_NAME, HEROKU_API_KEY)
    logz = herokuHelper.getLog()
    with open("logs.txt", "w") as log:
        log.write(logz)
    await process.delete()
    await bot.send_document(
        message.chat.id, "logs.txt", caption=f"**Logs Of {HEROKU_APP_NAME}**"
    )
    os.remove("logs.txt")


@Client.on_message(filters.command("restart"))
async def restart_me(bot, message):
    if message.from_user.id not in AUTH_USERS:
        await message.delete()
        return
    herokuHelper = HerokuHelper(HEROKU_APP_NAME, HEROKU_API_KEY)
    await message.reply_text("`App is Restarting. This is May Take Upto 3Min.`", quote=True)
    herokuHelper.restart()


@Client.on_message(filters.command("usage"))
async def dyno_usage(bot, message):
    if message.from_user.id not in AUTH_USERS:
        await message.delete()
        return
    process = await message.reply_text( "`Trying To Fetch Dyno Usage....`")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await message.reply_text(
             "`Error: something bad happened`\n\n" f">.`{r.reason}`\n"
        )
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    """ - Used - """
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)

    """ - Current - """
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)

    await asyncio.sleep(1.5)

    return await process.edit(
        "**Dyno Usage Data**:\n\n"
        f"✗ **APP NAME =>** `{HEROKU_APP_NAME}` \n"
        f"✗ **Usage in Hours And Minutes =>** `{AppHours}h`  `{AppMinutes}m`"
        f"✗ **Usage Percentage =>** [`{AppPercentage} %`]\n"
        "\n\n"
        "✗ **Dyno Remaining This Months 📆:**\n"
        f"✗ `{hours}`**h**  `{minutes}`**m** \n"
        f"✗ **Percentage :-** [`{percentage}`**%**]",
    )


#╔════╗────────╔═══╗
#║╔╗╔╗║────────║╔══╝
#╚╝║║╠╩═╦══╦╗╔╗║╚══╦══╦╦══╗
#──║║║║═╣╔╗║╚╝║║╔══╣╔╗╠╣╔═╝
#──║║║║═╣╔╗║║║║║╚══╣╚╝║║╚═╗
#──╚╝╚══╩╝╚╩╩╩╝╚═══╣╔═╩╩══╝
#──────────────────║║
#──────────────────╚╝
#---------------------------Gen Logo Epic-------------------------------------#

@Client.on_message(filters.command("stats")) 
async def startprivate(client, message):
    countb = await db.total_users_count()
    countb = await db.total_users_count()
    count = await client.get_chat_members_count(-1001620454933)
    counta = await client.get_chat_members_count(-1001620454933)
    text=f"""**😂𝘾𝙪𝙧𝙧𝙚𝙣𝙩 𝙎𝙩𝙖𝙩𝙨😂**
▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰
 **❑ 𝐄𝐏𝐈𝐂 𝐃𝐄𝐕𝐒 ❑** : `{count}`
 **❍ 𝐒𝐄𝐒𝐒𝐈𝐎𝐍 𝐁𝐎𝐓 𝐔𝐒𝐄𝐑𝐒 ❍**: `{countb}`
▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰
 """
    await client.send_sticker(message.chat.id, random.choice(STAT_STICKER))
    await client.send_message(message.chat.id, text=text)

STAT_STICKER = ["CAACAgQAAxkBAAEFHRditZFgRBAPm-9bkFJUQKOjSEgxoQACfwsAAmgpeVF2roP_0GLhzykE",
                "CAACAgQAAxkBAAEFHRVitZFYQ_EPOF7Y1GenAAHZOfu6xNIAAj4MAAKd3llQRh5-qJlCwa0pBA",
                "CAACAgQAAxkBAAEFHRNitZFVEBwdq0uFJDOvDRx2IzdoCwAC5wwAAubdSFEk6BkQ4EbQ1ikE",
                "CAACAgQAAxkBAAEFHRFitZFRwzQPYrVUQkxVP4yxF2Uw3gAC4AkAAu9GYFGTgHavjO_HLikE",
                "CAACAgQAAxkBAAEFHQ9itZFNixLf7fEZICaK8DF-Li967wACUAwAAmEq4VF8xFsUvkvQXSkE"              
         ]


@Client.on_message(filters.command("help"))
async def help(bot, message):
    if await forcesub(bot, message):
       return
    await bot.send_sticker(message.chat.id, HTCR)
    await message.reply_text(
        text=HELP_TXT,
        reply_markup=M_back,
        disable_web_page_preview=True
         )

@Client.on_message(filters.command("about"))
async def about(bot, message):
    if await forcesub(bot, message):
       return
    await bot.send_sticker(message.chat.id, HTCR)
    await message.reply_text(
        text=ABOUT_TXT,
        reply_markup=M_back,
        disable_web_page_preview=True
         )

HTCR = "CAADBQADxAMAAntRCFe3FiUGmlQcYAI"


#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
   

@Client.on_message(filters.incoming & filters.chat(-1001609244993))
async def bchanl(bot, update, broadcast_ids={}): 
    all_users = await database.get_all_users()
    broadcast_msg= update
    while True:
        broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if not broadcast_ids.get(broadcast_id):
            break

    out = await bot.send_message(-1001741009206,f"Ads Broadcast Started! You will be notified with log file when all the users are notified.")
    start_time = time.time()
    total_users = await database.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(total = total_users, current = done, failed = failed, success = success)
        
    async with aiofiles.open('broadcastlog.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(user_id = int(user['id']), message = broadcast_msg)
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await database.delete_user(user['id'])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(dict(current = done, failed = failed, success = success))
        
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    
    completed_in = datetime.timedelta(seconds=int(time.time()-start_time))
    await asyncio.sleep(3)
    await out.delete()
    
    if failed == 0:
        await bot.send_message(-1001741009206, f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.")
    else:
        await bot.send_document(-1001741009206, 'broadcastlog.txt', caption=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.")
    os.remove('broadcastlog.txt') 

print("Broadcast py Started Successfully 🌟")
