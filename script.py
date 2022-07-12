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

HELP_TXT = f"""
☙ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʜᴇʟᴘ ᴍᴇɴᴜ☙
◐ ɪ ᴀᴍ **ꜰᴀꜱᴛ & 100% ꜱᴀꜰᴇ** ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ɢᴇɴ ʙᴏᴛ
◐ ɪ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴛᴇʟᴇᴛʜᴏɴ & ᴘʏʀᴏɢʀᴀᴍ ᴠ2 ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴꜱ

┎ᴀʟʟ ᴀᴠᴀɪʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ┑

⍣⍣ /start - ⍟ꜰᴏʀ ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
⍣⍣ /generate - ⍟ɢᴇɴᴇʀᴀᴛᴇ ʏᴏᴜ ᴄʜᴏɪᴄᴇᴅ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ
⍣⍣ /help - ⍟ꜰᴏʀ ʜᴇʟᴘꜱ
⍣⍣ /about - ⍟ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ʙᴏᴛ
    
   ᴘᴏᴡᴇʀᴅ ʙʏ : [ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ](https://t.me/EpicBotsSl)"""

M_back = InlineKeyboardMarkup([[
                 InlineKeyboardButton('⏎', callback_data="mback")
                 ]])
ABOUT_TXT = f""
⍣⍣ᴅᴇᴠᴇʟᴏᴘᴇʀ : [𝔫𝔞𝔳𝔞𝔫𝔧𝔞𝔫𝔞](https://t.me/AboutNavanjana)
⍣⍣ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [GITᕼᑌᗷ](https://github.com/EpicBotSl/SessionGen)
⍣⍣ᴘᴏᴡᴇʀᴅ ʙʏ : [ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ](https://t.me/EpicBotsSl)
⍣⍣ʙᴀꜱᴇᴅ ᴏɴ : [ᴘʏʀᴏɢʀᴀᴍ](https://pyrogram.org)
⍣⍣ᴍᴀᴅᴇ ᴡɪᴛʜ : [ᴘʏᴛʜᴏɴ](https://python.org)

      [ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ 🇱🇰](https://t.me/EpicBotsSl)
"""
#╔════╗────────╔═══╗
#║╔╗╔╗║────────║╔══╝
#╚╝║║╠╩═╦══╦╗╔╗║╚══╦══╦╦══╗
#──║║║║═╣╔╗║╚╝║║╔══╣╔╗╠╣╔═╝
#──║║║║═╣╔╗║║║║║╚══╣╚╝║║╚═╗
#──╚╝╚══╩╝╚╩╩╩╝╚═══╣╔═╩╩══╝
#──────────────────║║
#──────────────────╚╝
