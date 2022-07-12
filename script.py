from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

START_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton('🍁ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴇꜱꜱɪᴏᴏɴɴ🍁', callback_data="gen")
                 ],
                 [
                 InlineKeyboardButton('☔ ʜᴇʟᴘ ☔', callback_data="Help"),
                 InlineKeyboardButton(text="🎋 ᴀʙᴏᴜᴛ 🎋", callback_data="about")
                 ],
                 [
                 InlineKeyboardButton(text="</ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ</>🇱🇰", url="https://t.me/EpicBotsSl")
                 ]])

generate_single_button = [InlineKeyboardButton("🍁ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴇꜱꜱɪᴏɴ🍁", callback_data="generate")]

generate_button = [generate_single_button]

BACK_TXT = f"""
      ❣ʜɪ dear 
   ⏦ɪ ᴀᴍ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴇᴛᴏʀ ʙᴏᴛ ⏦
🍁ɪ ᴄᴀɴ ɢᴇɴᴇʀᴇʀᴀᴛᴇ :
        🌀**ᴘʏʀᴏɢʀᴀᴍ**
        🌀**ᴛᴇʟᴇᴛʜᴏɴ**
        🌀**ᴘʏʀᴏɢʀᴀᴍ ᴠ2**
ꜱᴇꜱꜱɪᴏɴꜱ✓
🌍ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ
☔ᴘʀᴏᴊᴇᴄᴛ ʙʏ : [ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ](https://t.me/EpicBotsSl)"""

#╔════╗────────╔═══╗
#║╔╗╔╗║────────║╔══╝
#╚╝║║╠╩═╦══╦╗╔╗║╚══╦══╦╦══╗
#──║║║║═╣╔╗║╚╝║║╔══╣╔╗╠╣╔═╝
#──║║║║═╣╔╗║║║║║╚══╣╚╝║║╚═╗
#──╚╝╚══╩╝╚╩╩╩╝╚═══╣╔═╩╩══╝
#──────────────────║║
#──────────────────╚╝
