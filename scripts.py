import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

FORCESUB_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton('🍁ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴇꜱꜱɪᴏᴏɴɴ🍁', callback_data="")
                 ],
                 [
                 InlineKeyboardButton('☔ ʜᴇʟᴘ ☔', callback_data="Help"),
                 InlineKeyboardButton(text="🎋 ᴀʙᴏᴜᴛ 🎋", callback_data="about")
                 ],
                 [
                 InlineKeyboardButton(text="</ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ</>🇱🇰", url="https://t.me/EpicBotsSl")
                 ]])
